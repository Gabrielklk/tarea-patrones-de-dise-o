# Sistema E-Commerce - Tarea de Patrones de Diseño

Hola profe, este es el repositorio para la tarea de la materia de POO y Patrones de Diseño. Aquí le implementé los 5 patrones que pidió en la rúbrica sobre un caso de un carrito de compras.

## Reflexión Teórica sobre los Patrones de Diseño

Bueno, según lo que estuve investigando, los patrones de diseño son super importantes para la orientación a objetos. Básicamente son como recetas o plantillas que ya inventó alguien más listo para no tener que pensar tanto en cómo armar las clases desde cero. Decidí meterle 5 patrones que vi en un blog y me pareció que quedaban bien para el tema del e-commerce.

En mi experiencia haciendo esto, fue medio desesperante pero interesante. Dicen que los patrones sirven para no repetir código y que el sistema sea más "escalable" para el futuro. Supongo que sí funciona, aunque la verdad ahora hay como el triple de archivos que antes, pero al final compila y no da errores, así que creo que se logró el objetivo principal de desacoplar, o al menos eso creo. También traté de que se apliquen los principios SOLID, creo que el de Responsabilidad Única sí quedó porque cada modulito Python hace solo una cosa. 

## Explicación Técnica de qué hice (Implementaciones)

Hice una carpeta `src/` donde separé todo por archivos para que se vea más organizado. Lo que hice fue:

### 1. Singleton (en `database.py`)
- **Qué hace:** Es un patrón creacional que te asegura que la clase DatabaseConnection solo pueda instanciarse una única vez.
- **Por qué:** Lo puse porque si no, cada vez que hacías una venta se abría otra conexión a PostgreSQL y un amigo me dijo que eso tumba el servidor de la universidad. Vi por internet que había que modificar el `__new__` con un `_instance = None` loco ahí, así que lo sobreescribí, ¡y funcionó a la primera!

### 2. Strategy (en `discount_strategy.py`)
- **Qué hace:** Es un patrón de comportamiento. Sirve para elegir qué descuento le vas a dar al cliente.
- **Por qué:** Pasa que hacer una cadena de 10 `Ifs` gigantes para ver si el cliente es VIP o si es Navidad se veía feo. Así que hice varias subclases. Entonces si el man es VIP, el código le inyecta esa estrategia. Medio que no entendí demasiado cómo es que la Orden adivina qué estrategia usar por sí sola, pero en el `main.py` yo se la pasé a mano y sí calculó bien el 15%, así que ahí quedó.

### 3. Factory Method (en `payment_factory.py`)
- **Qué hace:** Una fábrica para crear los pagos.
- **Por qué:** Era necesario para los pagos con tarjeta o con PayPal. Básicamente la fábrica te crea el pago sin que yo tenga que poner `new PayPalPayment()` directo en el main. Le mandas un string con el nombre del método y el Factory te lo "fabrica" y te lo devuelve. Dicen que esto cumple la regla de Abierto para Extensión.

### 4. State (en `order_state.py`)
- **Qué hace:** Este sirve para manejar en qué estatus está el paquete, si en Preparación o Enviado.
- **Por qué:** La verdad con este me trabé un buen rato. La orden empieza en "Pendiente", y ese mismo estado tiene un método que literalmente le cambia la clase a la Orden entera para que pase a ser "Procesando". O sea, el objeto muta por dentro mientras corre el programa. Está rarísimo pero vi que es súper útil para evitar comprar algo que ya está cancelado, por ejemplo.

### 5. Observer (en `order_notifier.py`)
- **Qué hace:** Manda los mensajitos y los correos al cliente.
- **Por qué:** Es para no ensuciar la Orden. Hice que la orden sea algo llamado "Subject" y las clases de mandar mails sean "Observers". Ellos se quedan ahí pasivos esperando, y cuando la orden llama al `notify()`, PUM, se disparan e imprimen en consola simulando que mandaron el mensaje. De esta forma la Orden no tiene que tener código de servidores de correo adentro.

---

## Cómo ejecutar profe

Para probarlo nomás métase al root y ponga esto en la terminal:
```bash
python -m src.main
```
Ahí corre todo solito del tirón. ¡Espero salvar la nota del corte con esto, un saludo!