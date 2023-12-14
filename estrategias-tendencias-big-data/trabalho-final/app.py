import flask
from flask import Flask, request, jsonify
from joblib import load
import boto3

app = Flask(__name__)


@app.route('/predict_turismo', methods=['POST', 'GET'])
def predict_turismo():
    if flask.request.method == 'GET':
        with open("front.html") as front:
            conteudo = front.read()
        return conteudo, 200

    else:  # POST

        try:
            if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
                request_data = request.get_json()
                cod_pais = int(request_data['cod_pais'])
                cod_uf = int(request_data['cod_uf'])
                ano = int(request_data['ano'])
                cod_mes = int(request_data['cod_mes'])
            else:
                cod_pais = int(request.form['cod_pais'])
                cod_uf = int(request.form['cod_uf'])
                ano = int(request.form['ano'])
                cod_mes = int(request.form['cod_mes'])
        except (KeyError, ValueError) as e:
            return jsonify({'error': 'Campos inválidos ou ausentes.'}), 400

        s3_client = boto3.client('s3')
        s3_client.download_file('bucket-turismo', 'modelo_turismo.joblib', 'modelo_turismo.joblib')
    
        mr = load('modelo_turismo.joblib')
        resultado_predict = mr.predict([[cod_pais, cod_uf, ano, cod_mes]])
        chegadas_previsto = resultado_predict[0]

        resultado = {'previsto': chegadas_previsto}
        return jsonify(resultado), 200


if __name__ == '__main__':
    debug = False  # com essa opção como True, ao salvar, o "site" recarrega automaticamente."
    app.run(host='0.0.0.0', port=8888, debug=debug)
