import pika
import random

from faker import Faker

from connect import session_hw
from models import Contact
#docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

fake = Faker()
key = 'hello_world'

def create_contacts():
    contacts = []
    for _ in range(10):
        fullname = fake.name()
        email = fake.email()
        sent = False
        phone_number = fake.phone_number()
        communication_method = random.choice(["email", "sms"])
        
        contact = Contact(
            fullname=fullname,
            email=email,
            sent=sent,
            phone_number=phone_number,
            communication_method=communication_method
        )
        contact.save()
        contacts.append(contact)
    return contacts

def main():
    session_hw
    contacts = create_contacts()
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue=key)
    
    for contact in contacts:
        contact_id = str(contact.id)
        channel.basic_publish(exchange="", routing_key=contact.communication_method, body=contact_id)
        print(f"Contact ID published to the email queue: {contact_id}")
        
    connection.close()
    

if __name__ == '__main__':
    main()