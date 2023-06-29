from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ReferenceField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Autor(EmbeddedDocument):
    name = StringField(max_length=100)
    born_date = DateTimeField()
    born_location = StringField(max_length=50)
    description = StringField()

class Tag(EmbeddedDocument):
    name = StringField()

class Post(Document):
    quote = StringField(required=True)
    author = ReferenceField(Autor)
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'allow_inheritance': True}
