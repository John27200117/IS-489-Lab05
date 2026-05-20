class Ecommerce:

    def calcular_total(self, precio, cantidad):
        return precio * cantidad

    def aplicar_descuento(self, total, descuento):
        if descuento < 0 or descuento > 100:
            raise ValueError("Descuento inválido")

        return total - (total * descuento / 100)

    def validar_pago(self, metodo_pago):
        metodos_validos = ["visa", "mastercard", "paypal"]

        return metodo_pago.lower() in metodos_validos

    def generar_factura(self, cliente, total):
        if total <= 0:
            raise ValueError("Total inválido")

        return f"Factura generada para {cliente}: S/. {total}"