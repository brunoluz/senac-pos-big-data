#!/bin/bash

# limpeza
rm funcao.zip
if [ -e funcao.zip ]; then
    # Se o arquivo existir, exclua-o
    rm funcao.zip
fi


rm -rf package/
rm -rf temp_venv/

# criando ambiente virtual e instalando dependencias
mkdir package
python3 -m venv temp_venv
source temp_venv/bin/activate
pip install --target ./package -r requirements.txt
  
# criando arquivo zip
cd package
zip -r ../funcao.zip .
cd ..
rm -rf temp_venv/
rm -rf package/

zip -r funcao.zip . -x .venv/**\* make-lambda-package.sh .venv/

aws lambda update-function-code --function-name senac-tpabd-projeto-final-lambda --zip-file "fileb://funcao.zip"

rm funcao.zip