# Marianita

Un sitio para Mariana, hecho con **Python + Flask**, HTML, CSS y un poco de JavaScript.

## Páginas

| Ruta | Archivo | Qué es |
|---|---|---|
| `/` | `templates/index.html` | La portada con los mensajes |
| `/nosotros` | `templates/nosotros.html` | Nuestra galería de fotos |
| `/carta` | `templates/carta.html` | Un sobre que se abre al hacer clic |
| 404 | `templates/404.html` | Página de error |

## Estructura

```
.
├── app.py                  # Crea la app y registra el blueprint
├── paginas/
│   ├── rutas.py            # Las rutas (/, /nosotros, /carta)
│   └── datos.py            # La lista de fotos de la galería (edítala aquí)
├── templates/
│   ├── base.html           # Esqueleto: lo que se repite en todas las páginas
│   ├── partials/
│   │   └── header.html     # El header y el menú
│   ├── index.html
│   ├── nosotros.html
│   ├── carta.html
│   └── 404.html
├── static/
│   ├── css/
│   │   ├── base.css        # Paleta, header y menú (compartido)
│   │   ├── styles.css      # Portada
│   │   ├── carta.css       # La carta
│   │   └── nosotros.css    # La galería
│   ├── js/
│   │   ├── carta.js        # El sobre y los corazones
│   │   └── galeria.js      # La foto en grande
│   └── img/
│       ├── fotos/          # Las fotos originales (para procesar)
│       └── galeria/        # Las versiones optimizadas que se ven en la web
└── optimizar_fotos.py      # Convierte las originales en las de la web
```

## Cómo funciona el "header en todas las páginas"

`base.html` es el esqueleto común. Cada página lo extiende con `{% extends %}` y
rellena solo los bloques que necesita:

```html
{% extends 'base.html' %}

{% block content %}
    ...contenido de la página...
{% endblock %}
```

El header y el menú viven en `templates/partials/header.html` y `base.html` los
incluye con `{% include %}`, así que cambian en un solo sitio.

Los enlaces usan `url_for()`, nunca rutas escritas a mano:

```html
<a href="{{ url_for('paginas.carta') }}">Una carta para ti...</a>
```

## La galería

La lista de fotos está en `paginas/datos.py`:

```python
GALERIA = [
    {"archivo": "IMG-20260918-WA0104.webp", "titulo": ""},
]
```

- `archivo` → el nombre dentro de `static/img/galeria/`
- `titulo` → el texto bajo la foto (déjalo vacío si no quieres texto)

**Para añadir una foto:**

1. Copia el archivo a `static/img/fotos/`
2. Ejecuta `python optimizar_fotos.py` (lo reduce a 1600px de ancho y lo pasa a WebP)
3. Añade una línea a la lista de `paginas/datos.py`

## Poner en marcha

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abre <http://localhost:5000>.

## Desplegar en Vercel

El repo ya trae `vercel.json` y `requirements.txt` con `gunicorn`, así que:

```bash
vercel --prod
```

O directamente desde Vercel: importa el repositorio de GitHub y listo. Cada
`git push` actualiza el sitio.

## Paleta

Los colores están definidos como variables CSS en `static/css/base.css`:

```css
--rosa-fondo:  #e8d1c5;   /* fondo */
--rosa-panel:  #eddcd2;   /* header y menú */
--texto:       #4a2b36;   /* texto normal */
--rosa-fuerte: #d81b60;   /* textos resaltados */
--rosa-hondo:  #902960;   /* títulos */
--vino:        #6e1b40;   /* fechas y avisos */
```

Las fuentes son Cormorant Garamond, Dancing Script, Montserrat y Playfair Display,
cargadas desde Google Fonts.

## En producción

https://marianita-six.vercel.app

