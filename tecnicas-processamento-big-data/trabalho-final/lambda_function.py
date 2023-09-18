import json
import boto3
import requests


def lambda_handler(event, context):
    print(f"event: {event}")
    print(f"event: {context}")

    response = requests.get('https://raw.githubusercontent.com/edsonfell/csv_datasets/main/GamingStudy_Dataset.csv')
    print(f"response: {response}")

    s3 = boto3.resource('s3')
    bucket_name = 'senac-tpabd-projeto-final-s3'
    file_name = 'GamingStudy_Dataset.csv'
    file_content = response.text
    
    object = s3.Object(bucket_name, file_name)
    object.put(Body=file_content)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

