# Import the 'pika' library for RabbitMQ communication.
import pika
import time

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Define the queue name.
queue_name = 'my_queue'

# Declare the queue.
channel.queue_declare(queue=queue_name)

# Function to process received messages.
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    # You can add your processing logic here

# Set up the consumer to receive messages.
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit, press CTRL+C")

# Start consuming messages in a loop.
while True:
    connection.process_data_events()
    time.sleep(2)  # Wait for 2 seconds before checking for the next message.

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()
