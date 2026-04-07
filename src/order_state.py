"""
=========================================
PATRÓN DE COMPORTAMIENTO: STATE
=========================================
Propósito:
Permitir a un objeto alterar su comportamiento cuando su estado interno cambia.
Al observar este objeto, parecerá que mudó completamente de clase.

Aplicación en este Sistema (E-Commerce):
La línea de vida de los paquetes (y por consiguiente de la Orden) es lineal 
pero secciona diferentes mundos (Esperando Pago, Sellándose, Cargándose al Barco). 
Si el sistema actual es "Enviado", ¿Qué pasa si el usuario aprieta 'Pagar'? Falla. 
Este patrón encapsula los estados y asume el control del progreso en forma 
de pequeñas clases autónomas, evitando lidiar con lógicas caóticas.
"""
from abc import ABC, abstractmethod

# Interfaz abstracta del Patrón de Estado
class OrderState(ABC):
    @abstractmethod
    def next_state(self, order):
        """Intenta mover el paquete hacia la siguiente parada logística"""
        pass
    
    @abstractmethod
    def status(self) -> str:
        """Consultar estado en lenguaje natural"""
        pass

# =================== TRANSICIONES Y ESTADOS ===================

class PendingState(OrderState):
    def next_state(self, order):
        print("[Estado] El pago fue validado. Pasando la orden al departamento de ensamblaje (Procesando).")
        order.set_state(ProcessingState())

    def status(self) -> str:
        return "Pendiente de Pago"


class ProcessingState(OrderState):
    def next_state(self, order):
        print("[Estado] El paquete se selló y se entregó a la transportadora FedEx. Pasando a (Enviado).")
        order.set_state(ShippedState())

    def status(self) -> str:
        return "Procesando Paquetes"


class ShippedState(OrderState):
    def next_state(self, order):
        print("[Estado] Error Lógico - Ignorado: El pedido ya se ha enviado y está en manos del cliente.")
        
    def status(self) -> str:
        return "Enviado/Concluido"
