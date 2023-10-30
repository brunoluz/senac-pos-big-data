import os

import functions_framework
from google.cloud import bigquery

PROJECT = os.environ["PROJECT"]
DATASET = os.environ["DATASET"]
client = bigquery.Client()


def create_and_ingest_table(bucket, filename, table_id):
    # Create a table with the same file that was uploadeD
    file_uri = f"gs://{bucket}/{filename}"

    client.delete_table(table_id, not_found_ok=True)  # delete table if exists

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )
    job_config.field_delimiter = ";"
    load_job = client.load_table_from_uri(
        job_config=job_config,
        source_uris=file_uri,
        destination=table_id
    )
    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)
    print(f"Loaded {destination_table.num_rows} rows.")


# Triggered by a change in a storage bucket
def get_year_from_filename(filename):
    value = filename \
        .replace("chegadas_", "") \
        .replace(".csv", "")
    return int(value)


def consolidate_data_into_final_table(year):
    query = f"""
CREATE TABLE IF NOT EXISTS `{PROJECT}.{DATASET}.TURISMO_CONSOLIDADO` (
  continente STRING,
  cod_continente INT64,
  pais STRING,
  cod_pais INT64,
  uf STRING,
  cod_uf INT64,
  via STRING,
  cod_via INT64,
  ano INT64,
  mes STRING,
  cod_mes INT64,
  chegadas INT64
);
DELETE FROM `{PROJECT}.{DATASET}.TURISMO_CONSOLIDADO` WHERE ano = {year};
    """
    if year > 2015:
        query += f"""
        INSERT INTO `{PROJECT}.{DATASET}.TURISMO_CONSOLIDADO` (continente, cod_continente, 
        pais, cod_pais, uf, cod_uf, via, cod_via, ano, mes, cod_mes, chegadas)
        SELECT UPPER(Continente) as continente, 
        cod_continente, 
        UPPER(Pa__s) as pais, 
        cod_pais, 
        UPPER(UF) as uf, 
        cod_uf, 
        UPPER(Via) as via, 
        cod_via, 
        ano, 
        UPPER(M__s) as mes, 
        cod_mes, 
        Chegadas as chegadas
        from `{PROJECT}.{DATASET}.chegadas_{year}`;
        """
    else:
        query += f"""
        INSERT INTO `{PROJECT}.{DATASET}.TURISMO_CONSOLIDADO` (continente, cod_continente, 
        pais, cod_pais, uf, cod_uf, via, cod_via, ano, mes, cod_mes, chegadas)
        SELECT UPPER(Continente) as continente,
        Ordem_continente as cod_continente,
        UPPER(Pa__s) as pais, 
        Ordem_pa__s as cod_pais, 
        UPPER(UF) as uf, 
        Ordem_UF as cod_uf, 
        UPPER(Via_de_acesso) as via, 
        Ordem_via_de_acesso as cod_via, 
        ano, 
        UPPER(M__s) as mes,
        Ordem_m__s as cod_mes, 
        Chegadas as chegadas
        from `{PROJECT}.{DATASET}.chegadas_{year}`;
        """

    client.query(query)


@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    bucket = data["bucket"]
    filename = data["name"]
    metageneration = data["metageneration"]
    time_created = data["timeCreated"]
    updated = data["updated"]

    try:

        year = get_year_from_filename(filename)
        table_name = data["name"].replace(".csv", "")
        table_id = f"{PROJECT}.{DATASET}.{table_name}"

        create_and_ingest_table(bucket, filename, table_id)
        consolidate_data_into_final_table(year)

    except Exception as ex:
        print(f"erro: {ex}")

    return event_id, event_type, bucket, filename, metageneration, time_created, updated
