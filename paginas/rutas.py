from flask import Blueprint, render_template

from paginas.datos import GALERIA
# Importamos la lista de fotos de la galería (edítala en paginas/datos.py)

# Creamos el Blueprint llamado 'paginas'
paginas_bp = Blueprint('paginas', __name__)


@paginas_bp.route('/')
def index():
    return render_template('index.html')


@paginas_bp.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', galeria=GALERIA)


@paginas_bp.route('/carta')
def carta():
    return render_template('carta.html')
