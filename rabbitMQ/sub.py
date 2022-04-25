import pika, sys, os
import mysql.connector
import psycopg2
import psycopg2.extras
import requests

def save_to_db(user, value):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mine963258741",
        database="testdb",
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO info (name, message) VALUES (%s, %s)"
    val = (user, value)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        save_to_db("Mine", str(body))


    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


