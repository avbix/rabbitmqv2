# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Function to process received messages.
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    # You can add your processing logic here

def consume():
    # Устанавливаем функцию обратного вызова для обработки сообщений
    channel.basic_consume(queue='your_queue_name', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')

    # Начинаем получать сообщения из очереди
    channel.start_consuming()

consume()

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()