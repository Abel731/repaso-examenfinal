from flask import Flask, render_template, request, redirect, url_for,flash
from dao.NacionalidadDao import NacionalidadDao
app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route('/nacionalidades-index')
def nacionalidadesIndex():
    # Creacion de la instancia de nacionalidaddao
    nacionalidadDao = NacionalidadDao()
    lista_nacionalidades = nacionalidadDao.getCiudades()
    return render_template('nacionalidades-index.html', lista_nacionalidades=lista_nacionalidades)



# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)