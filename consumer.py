import pika

class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"  # Modificadores privados
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host= self.__host,
            port= self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        # Abriu um canal ao rabbitmq
        channel = pika.BlockingConnection(connection_parameters).channel()

        # Mapear a Queue
        channel.queue_declare(
            queue=self.__queue,
            durable=True,
            #arguments={
                #"x-overflow" : "reject-publish"
            #}
        )

        # Consumindo a Queue
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            # Para onde vao essas informacoes consumidas
            on_message_callback=self.__callback  # acao condicional
        )

        return channel
    
    def start(self):
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()


def minha_callback(ch, method, properties, body):
    print(body)


rabbitmq_consumer = RabbitmqConsumer(minha_callback)
rabbitmq_consumer.start()

