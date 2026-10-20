"""
GALERÍA DE FOTOS
================

Este es el ÚNICO archivo que tienes que tocar para cambiar la galería.

Cada línea de la lista es una foto:

    {"archivo": "nombre.webp", "titulo": "El texto que sale debajo"}

  - "archivo": el nombre del archivo dentro de  static/img/galeria/
  - "titulo":  el texto que aparece bajo la foto.
               Si lo dejas como "" la foto sale sin texto.

El orden de la lista es el orden en que se ven las fotos.

PARA AÑADIR UNA FOTO NUEVA:
  1. Copia el archivo en  static/img/fotos/
  2. Ejecuta  python optimizar_fotos.py   (crea la versión ligera en static/img/galeria/)
  3. Añade aquí una línea con el nombre del archivo resultante
"""

GALERIA = [
    {"archivo": "IMG-20260918-WA0104.webp",          "titulo": ""},
    {"archivo": "IMG_20260919_203415533_HDR_1.webp", "titulo": ""},
    {"archivo": "IMG_20261002_213751379_HDR.webp",   "titulo": ""},
    {"archivo": "IMG_20261013_142052969_HDR.webp",   "titulo": ""},
]
