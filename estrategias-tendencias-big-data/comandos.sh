## da máquina local
ssh -i EC2-KEY-PAIR-2.pem ubuntu@ec2-15-228-28-56.sa-east-1.compute.amazonaws.com

## da máquina na nuvem
conda activate jupyter
jupyter notebook --ip 0.0.0.0 --port 8888 
# Este comando retornada a url para entrar no notebook. 
# Para acessar de um computador qualquer, é necessário 
# substituir o nome do domínio pelo que é indicano via painel EC2 da AWS, ex:
# http://ec2-15-228-28-56.sa-east-1.compute.amazonaws.com:8888/?token=7e42393bafc12bf2c16e0218ecd86fdf3227c7365499cab4

## copiar aquivo para o servidor
scp -i EC2-KEY-PAIR-2.pem ~/Downloads/rest.zip ubuntu@ec2-54-207-65-77.sa-east-1.compute.amazonaws.com:/home/ubuntu/restp.zip

# GET /
curl http://ec2-15-228-28-56.sa-east-1.compute.amazonaws.com:8080/

# GET /echo/mensagem_teste
curl http://ec2-15-228-28-56.sa-east-1.compute.amazonaws.com:8080/echo/mensagem_teste

# GET /echo2?msg=oi
curl http://ec2-15-228-28-56.sa-east-1.compute.amazonaws.com:8080/echo2?msg=oi

# POST /echo2
curl -X POST http://ec2-15-228-28-56.sa-east-1.compute.amazonaws.com:8080/echo2 -d "msg=oi"

# POST /json-example
curl -X POST http://ec2-15-228-28-56.sa-east-1.compute.amazonaws.com:8080/json-example -H "Content-Type: application/json" -d '{"msg": "oi"}'

# POST /predict_turismo
curl -X POST http://ec2-54-164-189-176.compute-1.amazonaws.com:8888/predict_turismo -H "Content-Type: application/json" -d '{
    "cod_pais": 69,
    "cod_uf": 25,
    "ano": 2024,
    "cod_mes": 1
}'