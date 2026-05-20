import pytest
from ecommerce import Ecommerce

ecommerce = Ecommerce()

# ==========================
# PRUEBA 1
# ==========================

def test_calcular_total():
    
    # Arrange
    precio = 50
    cantidad = 2

    # Act
    resultado = ecommerce.calcular_total(precio, cantidad)

    # Assert
    assert resultado == 100


# ==========================
# PRUEBA 2
# ==========================

def test_aplicar_descuento():

    # Arrange
    total = 200
    descuento = 10

    # Act
    resultado = ecommerce.aplicar_descuento(total, descuento)

    # Assert
    assert resultado == 180


# ==========================
# PRUEBA 3
# ==========================

def test_descuento_invalido():

    with pytest.raises(ValueError):
        ecommerce.aplicar_descuento(100, 150)


# ==========================
# PRUEBA 4
# ==========================

def test_validar_pago():

    resultado = ecommerce.validar_pago("visa")

    assert resultado is True


# ==========================
# PRUEBA 5
# ==========================

def test_pago_invalido():

    resultado = ecommerce.validar_pago("bitcoin")

    assert resultado is False


# ==========================
# PRUEBA 6
# ==========================

def test_generar_factura():

    resultado = ecommerce.generar_factura("Juan", 300)

    assert "Factura generada" in resultado
    