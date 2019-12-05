from flask import Flask, render_template, request
import script as sp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods = ['GET'])
def predict():
    #Obtención y transformación de datos del paciente y pruebas
    dp1 = int(request.args.get('edad'))
    dp2 = str(request.args.get('sexo'))
    dp3 = str(request.args.get('multiple'))
    dp4 = int(request.args.get('gcs'))
    dp5 = int(request.args.get('wfns_p'))
    dp6 = int(request.args.get('wfns_i'))
    dp7 = int(request.args.get('fisher'))
    dp8 = int(request.args.get('tamano'))
    dp9 = str(request.args.get('uci'))
    dp10 = int(request.args.get('oct12'))
    dp11 = int(request.args.get('momento'))
    dp12 = str(request.args.get('localizacion'))
    #Obtención y transformación de datos históricos
    dh1 = int(request.args.get('hta'))
    dh2 = int(request.args.get('tabaq'))
    dh3 = int(request.args.get('obesidad'))
    dh4 = int(request.args.get('diabetes'))
    dh5 = int(request.args.get('alcohol'))
    dh6 = int(request.args.get('drogas'))
    dh7 = int(request.args.get('familiares'))
    #Almacenamiento de datos del paciente y pruebas y datos históricos
    datos_paciente = [dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, dp11, dp12]
    datos_historicos = [dh1, dh2, dh3, dh4, dh5, dh6, dh7]
    #Predicción del paciente
    resultado = sp.runPatient(datos_paciente, datos_historicos)
    return render_template("result.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
