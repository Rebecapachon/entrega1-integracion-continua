# Validación del clon público

Fecha: 31 de octubre de 2026.

Cloné el repositorio en la carpeta `C:\Users\jurep\Proyecto-integracion-clon`.

Desde esa carpeta construí la imagen con:

`docker build -t entrega1-clon .`

Luego ejecuté las pruebas con:

`docker run --rm entrega1-clon python -m unittest discover -s tests -v`

Resultado: se ejecutaron 8 pruebas y todas finalizaron correctamente (`OK`).
