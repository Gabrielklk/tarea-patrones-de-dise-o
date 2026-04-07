from src.database import DatabaseConnection
from src.payment_factory import PaymentFactory
from src.discount_strategy import VIPDiscount, NoDiscount
from src.order import Order
from src.order_notifier import EmailNotifier, SMSNotifier

def main():
    print("====================================")
    print("      SISTEMA E-COMMERCE DEMO       ")
    print("====================================")
    
    # 1. Singleton: Conexión segura a la base de datos central en toda la aplicación.
    db = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db is db2, "Error de Singleton: Las conexiones no son la misma instancia."
    
    # Se genera una nueva orden en el carrito
    base_amount = 150.00
    order = Order(base_amount)
    
    # 2. Observer: Los usuarios se suscriben desde sus preferencias de usuario a las alertas
    email_notif = EmailNotifier()
    sms_notif = SMSNotifier()
    order.attach(email_notif)
    order.attach(sms_notif)
    
    # 3. Strategy: Verificamos dinámicamente si el cliente tiene programas de lealtad
    print(f"\nGenerando la compra de la orden #{order.order_id}...")
    strategy = VIPDiscount()  # Este mes el cliente activó su membresía VIP
    discount = strategy.calculate_discount(order.amount)
    final_amount = order.amount - discount
    print(f"[Calculadora] Subtotal: ${order.amount:.2f} | Descuento: -${discount:.2f} | Total: ${final_amount:.2f}")
    
    # 4. Factory Method: Procesar el pago dependiendo de lo que elija en la pasarela web
    # Aquí podríamos fácilmente estar recibiendo "credit_card" desde el frontend
    payment_method = PaymentFactory.get_payment_processor("paypal")
    success = payment_method.process_payment(final_amount)
    
    # 5. State: Evolución orgánica de la orden basada en el sistema físico de inventario
    if success:
        print("\n--> Evento: El procesador de pago reportó éxito de fondos.")
        order.proceed() # Internamente cambiará de Pendiente a Procesando y notificará
        db.save_order(order.order_id)
        
        print("\n--> Evento: Bodega reporta que subió la caja al camión de correos.")
        order.proceed() # Pasa de Procesando a Enviado automáticamente

if __name__ == "__main__":
    main()
