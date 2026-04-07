"""
=========================================
PATRÓN DE COMPORTAMIENTO: STRATEGY
=========================================
Propósito:
Definir una familia entera de algoritmos, encapsular cada uno de ellos por
separado y hacerlos intercambiables entre sí libremente.

Aplicación en este Sistema (E-Commerce):
El carrito hace descuentos, pero es inestable depender de bloques de código condicionales
con decenas de "If día = Festivo" o "If cliente = VIP". Usando Strategy extraemos cada uno 
de los posibles cálculos en archivos/estrategias individuales.
La Orden (o el Checkout) es solo un "Contexto": Al cobrar, el sistema mira qué
estrategia está activa y la aplica. Añadir un nuevo descuento significa simplemente
añadir otro archivo de estrategia sin romper el código antiguo.
"""
from abc import ABC, abstractmethod

# Interfaz General Estratégica
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass

# Estrategia 1: Público Común
class NoDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        return 0.0

# Estrategia 2: Programa de Lealtad
class VIPDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        # Los clientes leales reciben un 15% de reducción monetaria.
        return amount * 0.15  

# Estrategia 3: Estacionalidades (Navidad, Viernes Negro)
class HolidayDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        # En épocas navideñas regalamos el 20%
        return amount * 0.20  
