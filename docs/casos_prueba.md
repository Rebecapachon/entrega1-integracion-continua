# Especificación y casos esperados (antes del código)

Regla: validar todas las líneas; rechazar pedido vacío, cantidad no positiva, producto sin registro de existencias o cantidad superior al inventario. Después, sumar cantidad × precio unitario. Si el subtotal es estrictamente mayor a $200.000 COP, descontar una sola vez el 10 %, truncando al peso entero.

| Caso | Entrada resumida | Resultado esperado |
|---|---|---|
| Pedido vacío | líneas=[] | Error: pedido sin líneas |
| Cantidad cero | producto A, cantidad 0 | Error: cantidad debe ser mayor que cero |
| Producto no registrado | producto Z no existe en inventario | Error: producto sin existencias registradas |
| Inventario insuficiente | 4 unidades; existencia 3 | Error: existencias insuficientes |
| Límite exacto | 2 × $100.000 | Subtotal $200.000; total $200.000 |
| Descuento básico | 3 × $100.000, tres productos/líneas válidos | Subtotal $300.000; descuento $30.000; total $270.000 |
| Redondeo hacia abajo | subtotal $200.001 | descuento $20.000; total $180.001 |
| Varias líneas | 2 × $40.000 + 1 × $50.000 | Subtotal y total $130.000 |
