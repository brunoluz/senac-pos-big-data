import functions_framework
from google.cloud import bigquery

PROJECT = "senac-dados-turismo"
DATASET = "senac_dados_turismo_conjunto_dados"
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
    query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name, state
        ORDER BY total_people DESC
        LIMIT 20
    """
    query_job = client.query(query)  # Make an API request.


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
