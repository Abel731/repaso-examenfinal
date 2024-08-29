from flask import Flask, render_template, request, url_for, flash, redirect
from dao.NacionalidadDao import NacionalidadDao
app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route('/nacionalidades-index')
def nacionalidades_index():
    # Creacion de la instancia de nacionalidaddao
    nacionalidadDao = NacionalidadDao()
    lista_nacionalidades = nacionalidadDao.getNacionalidades()
    return render_template('nacionalidades-index.html', lista_nacionalidades=lista_nacionalidades)

@app.route('/nacionalidades')
def nacionalidades():
    return render_template('nacionalidades.html')

@app.route('/guardar-nacionalidad', methods=['POST'])
def guardarNacionalidad():
    nacionalidad = request.form.get('txtDescripcion').strip()
    if nacionalidad == None or len(nacionalidad) < 1:
        # mostrar un mensaje al usuario
        flash('Debe escribir algo en la descripcion', 'warning')

        # redireccionar a la vista ciudades
        return redirect(url_for('nacionalidades'))

    nacionalidadDao = NacionalidadDao()
    nacionalidadDao.guardarNacionalidad(nacionalidad.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades
    return redirect(url_for('nacionalidades_index'))

@app.route('/nacionalidades-editar/<id>')
def nacionalidadesEditar(id):
    nacionalidadDao = NacionalidadDao()
    return render_template('nacionalidades-editar.html', nacionalidad=nacionalidadDao.getNacionalidadById(id))

@app.route('/actualizar-nacionalidad', methods=['POST'])
def actualizarNacionalidad():
    id = request.form.get('txtIdNacionalidades')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('nacionalidadesEditar', id=id))

    # actualizar
    nacionalidadDao = NacionalidadDao()
    nacionalidadDao.updateNacionalidad(id, descripcion.upper())

    return redirect(url_for('nacionalidades_index'))

@app.route('/nacionalidades-eliminar/<id>')
def nacionalidadesEliminar(id):
    nacionalidadDao = NacionalidadDao()
    nacionalidadDao.deleteNacionalidad(id)
    return redirect(url_for('nacionalidades_index'))

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)