from django.test import TestCase

from .models import Producto


class ProductoModelTests(TestCase):
    def test_string_representation_is_product_name(self):
        producto = Producto(
            nombre="Teclado",
            precio="49.90",
            stock=5,
            categoria="Accesorios",
        )

        self.assertEqual(str(producto), "Teclado")

    def test_product_is_available_by_default(self):
        producto = Producto(
            nombre="Teclado",
            precio="49.90",
            stock=5,
            categoria="Accesorios",
        )

        self.assertTrue(producto.disponible)

    def test_product_can_be_saved(self):
        producto = Producto.objects.create(
            nombre="Teclado",
            precio="49.90",
            stock=5,
            categoria="Accesorios",
        )

        self.assertEqual(Producto.objects.get(pk=producto.pk).nombre, "Teclado")