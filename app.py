from flask import Flask, request, render_template, url_for, jsonify
from flask.globals import session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = 'Mi_llave_secreta'


@app.route('/')
# Decorador que modifica el metodo que viene despues
def funcion_inicio():
    app.logger.debug('Mensaje desde debug')
    app.logger.info('Mensaje desde debug entrando al path {}'.format(request.path))
    app.logger.warning('Mensaje desde warning')
    app.logger.error('Mensaje desde error')
    if 'username' in session:
        return 'El usuario ya he hecho login'
    else:
        return 'No ha hecho login'
    #return f'Hola Mundo desde Flask'

@app.route('/saludar/<nombre>')
def funcion_saludar(nombre):
    app.logger.warn(f'en el path {request.path}')
    return f'Hola como estas {nombre}'

@app.route('/edad/<int:edad>')
def funcion_edad(edad):
    app.logger.warn(f'en el path {request.path}')
    return f'Hola tu edad +1  es {edad + 1}'

@app.route('/mostrar/<nombre>', methods = ['GET','POST'])
def funcion_mostrarnombre(nombre):
    app.logger.warn(f'en el path {request.path}')
    return f'Tu nombre es: {nombre}'

@app.route('/mostrar2/<nombre>', methods = ['GET','POST'])
def funcion_mostrarnombre2(nombre):
    app.logger.warn(f'en el path {request.path}')
    return render_template('mostrar.html', nombre= nombre)

@app.route('/redireccionar', methods = ['GET','POST'])
def funcion_redireccionar():
    app.logger.warn(f'en el path {request.path}')
    return redirect(url_for('funcion_inicio'))

@app.route('/redireccionar2/<nombre>', methods = ['GET','POST'])
def funcion_redireccionar2(nombre):
    app.logger.warn(f'en el path {request.path}')
    return redirect(url_for('funcion_mostrarnombre2', nombre = nombre))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error = error), 404

# REST Representational state transfer
@app.route('/api/mostrar/<nombre>')
def funcion_mostrarnombre_json(nombre):
    valores = {'nombre': nombre}
    return jsonify(valores)

