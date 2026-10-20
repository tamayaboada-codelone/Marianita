from flask import Flask, render_template

from paginas.rutas import paginas_bp
# Importamos tu Blueprint

app = Flask(__name__)

# Registramos el Blueprint en la aplicación principal.
# Las rutas (/, /nosotros, /carta) están definidas en paginas/rutas.py
app.register_blueprint(paginas_bp)


# Página de error cuando alguien pide una ruta que no existe
@app.errorhandler(404)
def no_encontrado(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # debug=True solo en desarrollo (recarga el código al guardar).
    # En producción hay que quitarlo o usar un servidor WSGI.
    app.run(debug=True)
