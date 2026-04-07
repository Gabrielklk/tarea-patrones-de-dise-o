"""
=========================================
PATRÓN DE COMPORTAMIENTO: OBSERVER
=========================================
Propósito:
Definir de manera limpia una dependencia uno-a-muchos entre objetos de manera 
que, cuando uno de ellos cambie su estado, todos sus dependientes sean advertidos 
e invoquen sus algoritmos de manera automática.

Aplicación en este Sistema (E-Commerce):
El cliente exige conocer qué sucede con su paquete, y para eso usamos Notificaciones.
Para que la base principal esté libre de acoplamiento no le inyectamos a Order 
un pedazo de código de Twilio o de Correos de Google. Solo le pedimos asuma
el rol de "Sujeto / Subject" (Quien tiene algo qué contar) y definimos Notificadores
como "Observadores" (Quienes escuchan al Sujeto).
Al hacer algún cambio, el Sujeto levanta su bandera y los Observadores reaccionan.
"""
from abc import ABC, abstractmethod

# Interfaz base de todo aquel que pretenda "Observar"
class Observer(ABC):
    @abstractmethod
    def update(self, order_id: str, status: str):
        pass

# Observador Concreto 1
class EmailNotifier(Observer):
    def update(self, order_id: str, status: str):
        # La lógica simula el SMTP Client Tool...
        print(f"[Notificación Email ✉️] ¡Hola! Tu pedido {order_id} ahora se encuentra: {status}")

# Observador Concreto 2
class SMSNotifier(Observer):
    def update(self, order_id: str, status: str):
        # La lógica simula APIs como Twilio o AWS SNS...
        print(f"[Notificación SMS 📱] E-Commerce: Pedido {order_id} cambió a estado '{status}'")

# Objeto Base Transmisor (Subject / Sujeto Activo)
class OrderSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        """Asocia y matricula nuevos vigilantes de cambios"""
        self._observers.append(observer)

    def notify(self, order_id: str, status: str):
        """Dispara en cascada la ejecución de lo que los testigos deben reportar"""
        for observer in self._observers:
            observer.update(order_id, status)
