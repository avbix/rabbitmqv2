# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Define the exchange name and type (in this case, "direct").
exchange_name = 'direct_logs'
exchange_type = 'direct'

# Declare the exchange.
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

# Define the queue name.
queue_name = 'my_queue'

# Declare the queue.
channel.queue_declare(queue=queue_name)

# Bind the queue to the exchange with a specific routing key.
routing_key = 'info'  # This can be any key that matches the routing.
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Send a message to the exchange with the specified routing key.
message = 'Hello, RabbitMQ!'
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

print(f"Sent: '{message}' with routing key '{routing_key}'")

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()
