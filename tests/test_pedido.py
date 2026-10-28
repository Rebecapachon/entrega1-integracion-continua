import unittest
from app.pedido import calcular_total

class CalcularTotalTests(unittest.TestCase):
    def test_rechaza_pedido_vacio(self):
        with self.assertRaisesRegex(ValueError, "sin líneas"):
            calcular_total([], {})
    def test_rechaza_cantidad_no_positiva(self):
        with self.assertRaisesRegex(ValueError, "mayor que cero"):
            calcular_total([{"producto":"A", "cantidad":0, "precio_unitario":100}], {"A":3})
    def test_rechaza_producto_sin_existencias(self):
        with self.assertRaisesRegex(ValueError, "no tiene existencias registradas"):
            calcular_total([{"producto":"A", "cantidad":1, "precio_unitario":100}], {})
    def test_rechaza_cantidad_superior_al_inventario(self):
        with self.assertRaisesRegex(ValueError, "insuficientes"):
            calcular_total([{"producto":"A", "cantidad":4, "precio_unitario":100}], {"A":3})
    def test_no_descuenta_en_umbral_exacto(self):
        self.assertEqual(calcular_total([{"producto":"A", "cantidad":2, "precio_unitario":100000}], {"A":2}), {"subtotal":200000,"descuento":0,"total":200000})
    def test_reproduce_error_del_caso_tres_lineas(self):
        lineas=[{"producto":p,"cantidad":1,"precio_unitario":100000} for p in ("A","B","C")]
        inv={p:1 for p in ("A","B","C")}
        self.assertEqual(calcular_total(lineas, inv), {"subtotal":300000,"descuento":30000,"total":270000})
    def test_descuento_se_redondea_hacia_abajo(self):
        self.assertEqual(calcular_total([{"producto":"A","cantidad":1,"precio_unitario":200001}], {"A":1}), {"subtotal":200001,"descuento":20000,"total":180001})
    def test_suma_varias_lineas_sin_descuento(self):
        lineas=[{"producto":"A","cantidad":2,"precio_unitario":40000},{"producto":"B","cantidad":1,"precio_unitario":50000}]
        self.assertEqual(calcular_total(lineas, {"A":2,"B":1}), {"subtotal":130000,"descuento":0,"total":130000})

if __name__ == "__main__": unittest.main()
