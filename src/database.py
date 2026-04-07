"""
=========================================
PATRÓN CREACIONAL: SINGLETON
=========================================
Propósito:
Garantizar que una clase tenga solo una instancia y proporcionar un punto
de acceso global a ella.

Aplicación en este Sistema (E-Commerce):
La base de datos maneja la persistencia de las órdenes. Las conexiones a bases
de datos son recursos valiosos y de alto costo para el sistema. Al aplicar el
patrón Singleton, nos aseguramos de que todos los sectores de nuestra app (pagos,
inventarios, etc) compartan y apunten exactamente a la misma conexión en memoria
en lugar de crear varias saturando el servidor.
"""

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        # Si la instancia no ha sido creada, la creamos y reservamos en memoria.
        if cls._instance is None:
            print("[Database] Iniciando conexión persistente a la base de datos principal...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection_string = "PostgreSQL_Produccion"
        
        # Si ya había sido creada, devolvemos la existente, sin volver a instanciar.
        return cls._instance

    def save_order(self, order_id: str):
        print(f"[Database] Orden {order_id} guardada exitosamente en {self.connection_string}.")
