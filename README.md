# Entrega 1 - Integración continua

Aplicación de línea de comandos para validar líneas de pedido y calcular el descuento de acuerdo con el caso. No tiene interfaz gráfica ni base de datos.

## Requisitos
Python 3.12 o Docker Desktop con motor Linux activo.

## Ejecutar pedido de ejemplo
`python app/pedido.py examples/pedido.json`

## Ejecutar pruebas
`python -m unittest discover -s tests -v`

## Construir y ejecutar con Docker
`docker build -t entrega1-pedidos .`
`docker run --rm entrega1-pedidos`
`docker run --rm entrega1-pedidos python -m unittest discover -s tests -v`

## Flujo
GitHub Actions ejecuta las pruebas en cada push y pull request. La evidencia de ejecución local debe registrarse con fecha; no se deben agregar capturas ficticias.
