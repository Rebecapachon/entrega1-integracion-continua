FROM python:3.12-slim
WORKDIR /proyecto
COPY app ./app
COPY tests ./tests
COPY examples ./examples
COPY docs ./docs
CMD ["python", "app/pedido.py", "examples/pedido.json"]
