#!/usr/bin/env python
import pika

def send_to_queue(message):
    
    connection_parameters = pika.ConnectionParameters(host='localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    message="mine jung"
    channel.basic_publish(exchange='', routing_key='hello',body=message)
    connection.close()
    return "Message Sent!  "



send_to_queue("You've been Visited")