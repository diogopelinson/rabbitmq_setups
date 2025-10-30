import pika
# Publisher Cru

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Abriu um canal ao rabbitmq
channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="estouMandandoUmaMensagem2",
    #Delivery Mode 2 = Modo de entrega 2 eh um modo de persistencia de dados
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)
