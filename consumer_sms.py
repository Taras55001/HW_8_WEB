import pika
import sys

from connect import session_hw
from models import Contact

key = 'sms'


def send_sms(contact):
    print(f"SMS sent for contact: {contact.fullname}")


def main():
    session_hw
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=key)

    def callback(ch, method, properties, body):
        contact_id = body.decode()
        contact = Contact.objects.get(id=contact_id)

        send_sms(contact)

        contact.sent = True
        contact.save()

    channel.basic_consume(queue=key, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for SMS messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
