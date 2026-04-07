"""
=========================================
PATRÓN CREACIONAL: FACTORY METHOD
=========================================
Propósito:
Proporcionar una interfaz para crear objetos en una superclase, permitiendo
a las subclases alterar o definir el tipo de objeto específico que se creará.

Aplicación en este Sistema (E-Commerce):
Nuestra tienda procesa pagos a través de variadas plataformas (Tarjetas, PayPal).
El cliente del código no debe construir ('instanciar') dichas plataformas, porque
lo ataría al flujo base. Por lo tanto recurrimos a un Factory, un "Creador de Entidades",
donde simplemente pasamos el "tipo" de pago por texto, y la fábrica gestiona 
absolutamente todos los detalles, retornando así un Procesador genérico listo para su uso.
"""
from abc import ABC, abstractmethod

# 1. Producto Abstracto (Interfaz Base)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

# 2. Productos Concretos A
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"[Pago] Validando y procesando ${amount:.2f} con Tarjeta de Crédito Segura.")
        return True

# 3. Productos Concretos B
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"[Pago] Redirigiendo y procesando ${amount:.2f} interactuando con la API de PayPal.")
        return True

# 4. Constructor / Creador (La Fábrica)
class PaymentFactory:
    @staticmethod
    def get_payment_processor(method_type: str) -> PaymentProcessor:
        # Determina, estructura y despacha el producto concreto correcto.
        if method_type.lower() == "credit_card":
            return CreditCardPayment()
        elif method_type.lower() == "paypal":
            return PayPalPayment()
        else:
            raise ValueError(f"El método de pago '{method_type}' no está registrado.")
