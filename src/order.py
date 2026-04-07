"""
=========================================
MODELO: ORDEN CENTRAL (CONTEXTO INTEGRADOR)
=========================================
Explicación Técnica:
Este es el modelo de dominio central (`Context` en POO) que engloba y ejecuta 
la interoperabilidad fundamental entre los 2 patrones de comportamiento principales: 
- Hereda integralmente de 'OrderSubject' (Módulo de Observer) con la misión de ser audible.
- Empieza en la vida en un 'PendingState' (Módulo de State) absorbiendo su ciclo vital.

Este caso materializa cómo los Patrones de diseño no son excluyentes sino cooperativos.
"""
import uuid
from src.order_state import PendingState
from src.order_notifier import OrderSubject

class Order(OrderSubject):
    def __init__(self, amount: float):
        super().__init__()
        self.order_id = str(uuid.uuid4())[:8].upper()
        self.amount = amount
        # Inicialización del Patrón State (Se delega totalmente)
        self._state = PendingState()

    def set_state(self, state):
        self._state = state
        # Aplicación del Patrón Observer (Aprovechamos que acabamos de cambiar
        # de Estado internamente para Notificar externamente a los oyentes)
        self.notify(self.order_id, self._state.status())

    def proceed(self):
        # Transición transparente a cargo del Objeto Estado subyacente.
        # En POO: Self delegation
        self._state.next_state(self)

    def get_status(self):
        return self._state.status()
