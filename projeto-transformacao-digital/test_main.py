import pytest
from cloudevents.http import CloudEvent

import main


def test_functions_eventsource_storage_2010(capsys: pytest.LogCaptureFixture) -> None:

    attributes = {
        'specversion': '1.0',
        'id': '9517119584681131',
        'source': '//storage.googleapis.com/projects/_/buckets/senac-dados-turismo',
        'type': 'google.cloud.storage.object.v1.finalized',
        'datacontenttype': 'application/json',
        'subject': 'objects/chegadas_2010.csv',
        'time': '2023-10-29T18:00:48.483983Z',
        'bucket': 'senac-dados-turismo'
    }

    data = {
        'kind': 'storage#object',
        'id': 'senac-dados-turismo/chegadas_2010.csv/1698602448406883',
        'selfLink': 'https://www.googleapis.com/storage/v1/b/senac-dados-turismo/o/chegadas_2010.csv',
        'name': 'chegadas_2010.csv',
        'bucket': 'senac-dados-turismo',
        'generation': '1698602448406883',
        'metageneration': '1',
        'contentType': 'text/csv',
        'timeCreated': '2023-10-29T18:00:48.483Z',
        'updated': '2023-10-29T18:00:48.483Z',
        'storageClass': 'STANDARD',
        'timeStorageClassUpdated': '2023-10-29T18:00:48.483Z',
        'size': '1575721',
        'md5Hash': 'VilJ8Oc2XfsRwSO4amKIQQ==',
        'mediaLink': 'https://storage.googleapis.com/download/storage/v1/b/senac-dados-turismo/o/chegadas_2010.csv?generation=1698602448406883&alt=media',
        'crc32c': 'ROhf9Q==',
        'etag': 'COOStZzrm4IDEAE='
    }

    event = CloudEvent(attributes, data)

    (
        event_id,
        event_type,
        bucket,
        name,
        metageneration,
        time_created,
        updated,
    ) = main.hello_gcs(event)

    out, _ = capsys.readouterr()
    assert "9517119584681131" in event_id
    assert "google.cloud.storage.object.v1.finalized" in event_type
    assert "senac-dados-turismo" in bucket
    assert "chegadas_2010.csv" in name
    assert metageneration == '1'
    assert "2023-10-29T18:00:48.483Z" in time_created
    assert "2023-10-29T18:00:48.483Z" in updated


def test_functions_eventsource_storage_2020(capsys: pytest.LogCaptureFixture) -> None:

    attributes = {
        'specversion': '1.0',
        'id': '9517119584681131',
        'source': '//storage.googleapis.com/projects/_/buckets/senac-dados-turismo',
        'type': 'google.cloud.storage.object.v1.finalized',
        'datacontenttype': 'application/json',
        'subject': 'objects/chegadas_2020.csv',
        'time': '2023-10-29T18:00:48.483983Z',
        'bucket': 'senac-dados-turismo'
    }

    data = {
        'kind': 'storage#object',
        'id': 'senac-dados-turismo/chegadas_2020.csv/1698602448406883',
        'selfLink': 'https://www.googleapis.com/storage/v1/b/senac-dados-turismo/o/chegadas_2020.csv',
        'name': 'chegadas_2020.csv',
        'bucket': 'senac-dados-turismo',
        'generation': '1698602448406883',
        'metageneration': '1',
        'contentType': 'text/csv',
        'timeCreated': '2023-10-29T18:00:48.483Z',
        'updated': '2023-10-29T18:00:48.483Z',
        'storageClass': 'STANDARD',
        'timeStorageClassUpdated': '2023-10-29T18:00:48.483Z',
        'size': '1575721',
        'md5Hash': 'VilJ8Oc2XfsRwSO4amKIQQ==',
        'mediaLink': 'https://storage.googleapis.com/download/storage/v1/b/senac-dados-turismo/o/chegadas_2020.csv?generation=1698602448406883&alt=media',
        'crc32c': 'ROhf9Q==',
        'etag': 'COOStZzrm4IDEAE='
    }

    event = CloudEvent(attributes, data)

    (
        event_id,
        event_type,
        bucket,
        name,
        metageneration,
        time_created,
        updated,
    ) = main.hello_gcs(event)

    out, _ = capsys.readouterr()
    assert "9517119584681131" in event_id
    assert "google.cloud.storage.object.v1.finalized" in event_type
    assert "senac-dados-turismo" in bucket
    assert "chegadas_2020.csv" in name
    assert metageneration == '1'
    assert "2023-10-29T18:00:48.483Z" in time_created
    assert "2023-10-29T18:00:48.483Z" in updated
