"""
Optimiza las fotos para la web.

Qué hace:
  1. Lee cada foto de  static/img/fotos/     (tus originales, NO se tocan)
  2. La redimensiona a un máximo de 1600px de ancho
  3. La guarda en    static/img/galeria/    (la versión que se ve en la web)

Uso:
  python optimizar_fotos.py

Cuando añadas una foto nueva en static/img/fotos/, ejecuta esto otra vez
y después añade una línea a la GALERIA en paginas/datos.py
"""

import os
from PIL import Image

# --- CONFIGURACIÓN (edítala si quieres) ---
ORIGENES = os.path.join("static", "img", "fotos")
DESTINO = os.path.join("static", "img", "galeria")
ANCHO_MAX = 1600      # ancho máximo en píxeles
CALIDAD = 82          # calidad del WebP (70-90 es un buen rango)
FORMATO = "WEBP"

EXTENSIONES = (".jpg", ".jpeg", ".png", ".webp")


def limpiar(nombre):
    """Quita espacios y paréntesis para que la URL quede legible."""
    for caracter in " ()":
        nombre = nombre.replace(caracter, "_")
    while "__" in nombre:
        nombre = nombre.replace("__", "_")
    return nombre.strip("_")


def main():
    if not os.path.isdir(ORIGENES):
        print(f"No existe la carpeta: {ORIGENES}")
        return

    os.makedirs(DESTINO, exist_ok=True)
    fotos = sorted(f for f in os.listdir(ORIGENES) if f.lower().endswith(EXTENSIONES))

    if not fotos:
        print("No hay fotos en", ORIGENES)
        return

    for nombre in fotos:
        ruta_origen = os.path.join(ORIGENES, nombre)
        nombre_limpio = limpiar(os.path.splitext(nombre)[0]) + ".webp"
        ruta_destino = os.path.join(DESTINO, nombre_limpio)

        imagen = Image.open(ruta_origen).convert("RGB")

        if imagen.width > ANCHO_MAX:
            alto = round(imagen.height * ANCHO_MAX / imagen.width)
            imagen = imagen.resize((ANCHO_MAX, alto), Image.LANCZOS)

        imagen.save(ruta_destino, FORMATO, quality=CALIDAD, method=6)

        antes = os.path.getsize(ruta_origen) // 1024
        despues = os.path.getsize(ruta_destino) // 1024
        print(f"  {nombre_limpio:42} {imagen.width}x{imagen.height}  {antes} KB -> {despues} KB")


if __name__ == "__main__":
    print("Optimizando fotos...")
    main()
    print("Listo. Revisa static/img/galeria/ y actualiza paginas/datos.py")
