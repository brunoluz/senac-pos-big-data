## da máquina local
ssh -i EC2-KEY-PAIR-2.pem ubuntu@ec2-54-94-243-180.sa-east-1.compute.amazonaws.com

## da máquina na nuvem
conda activate jupyter
jupyter notebook --ip 0.0.0.0 --port 8888 
# Este comando retornada a url para entrar no notebook. 
# Para acessar de um computador qualquer, é necessário 
# substituir o nome do domínio pelo que é indicano via painel EC2 da AWS, ex:
# http://ec2-15-228-7-24.sa-east-1.compute.amazonaws.com:8888/?token=76111e0953ec22945c3e59365aa8bbac03eb21344519fdd4
