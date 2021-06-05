from flask import Flask, request

app = Flask(__name__)

@app.route('/')
# Decorador que modifica el metodo que viene despues
def funcion_inicio():
    app.logger.debug('Mensaje desde debug')
    app.logger.info('Mensaje desde debug entrando al path {}'.format(request.path))
    app.logger.warning('Mensaje desde warning')
    app.logger.error('Mensaje desde error')
    return f'Hola Mundo desde Flask'

@app.route('/saludar/<nombre>')
def funcion_saludar(nombre):
    app.logger.warn(f'en el path {request.path}')
    return f'Hola como estas {nombre}'

@app.route('/edad/<int:edad>')
def funcion_edad(edad):
    app.logger.warn(f'en el path {request.path}')
    return f'Hola tu edad +1  es {edad + 1}'