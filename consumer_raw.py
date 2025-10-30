import pika
# Consumer Cru

def minha_callback(ch, method, properties, body):
    print(body)
    #print(type(body)) #Le como Byte 


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

# Mapear a Queue
channel.queue_declare(
    queue="data_queue",
    durable=True
)

# Consumindo a Queue
channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    # Para onde vao essas informacoes consumidas
    on_message_callback=minha_callback  # acao condicional
)

print(f'Listen RabbitMQ on Port 5672')
channel.start_consuming()
