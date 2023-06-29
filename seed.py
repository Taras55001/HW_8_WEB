
from mongoengine import EmbeddedDocument, Document


from connect import session_hw
from models import Autor, Tag, Post

def create(name, age, features):
    autor = Autor(name=name, age=age, features=features)
    autor.save()
    return autor

if __name__ == '__main__':
    session_hw.save()
