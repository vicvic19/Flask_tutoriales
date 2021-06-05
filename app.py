from flask import Flask, 

app = Flask(__name__)

@app.route('/')
# Decorador que modifica el metodo que viene despues
def funcion_inicio():
    return f'Hola Mundo desde Flask'