import boto3
import requests

print("criando requisicao para download")
response = requests.get('https://github.com/brunoluz/senac-pos-big-data/raw/master/tecnicas-processamento-big-data/trabalho-final/gaminganxiety.avro')
print(f"response: {response}")
print("download efetuado")


s3 = boto3.resource('s3')
bucket_name = 'senac-tpabd-projeto-final-s3'
file_name = 'gaming_anxiety/gaminganxiety.avro'
file_content = response.content

print("salvando arquivo no s3")
s3_object = s3.Object(bucket_name, file_name)
s3_object.put(Body=file_content)
print("arquivo 's3://senac-tpabd-projeto-final-s3/gaming_anxiety/gaminganxiety.avro' salvo")