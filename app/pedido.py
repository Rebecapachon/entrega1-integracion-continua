"""Cálculo mínimo de pedidos para demostrar validación y pruebas CI."""
import json
import sys
from pathlib import Path

def calcular_total(pedido, existencias):
    if not pedido:
        raise ValueError("El pedido no puede estar sin líneas.")
    for i, linea in enumerate(pedido, 1):
        producto=linea.get("producto")
        cantidad=linea.get("cantidad")
        precio=linea.get("precio_unitario")
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError(f"La cantidad de la línea {i} debe ser un entero mayor que cero.")
        if not isinstance(precio, int) or isinstance(precio, bool) or precio < 0:
            raise ValueError(f"El precio de la línea {i} debe ser un entero no negativo en pesos.")
        if producto not in existencias:
            raise ValueError(f"El producto {producto!r} no tiene existencias registradas.")
        if not isinstance(existencias[producto], int) or existencias[producto] < cantidad:
            raise ValueError(f"Existencias insuficientes para el producto {producto!r}.")
    subtotal=sum(linea["cantidad"]*linea["precio_unitario"] for linea in pedido)
    descuento=(subtotal*10)//100 if subtotal > 200000 else 0
    return {"subtotal": subtotal, "descuento": descuento, "total": subtotal-descuento}

def main():
    ruta=Path(sys.argv[1]) if len(sys.argv)>1 else Path("examples/pedido.json")
    datos=json.loads(ruta.read_text(encoding="utf-8"))
    resultado=calcular_total(datos["pedido"],datos["existencias"])
    print(json.dumps(resultado,ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
