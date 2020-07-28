from mongoengine import Document, fields, EmbeddedDocument
from datetime import datetime
from string import ascii_lowercase
from random import choice


book_categories = ["Novel", "Science", "Space", "History"]


def random_string(length=12):
    letters = ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str

class BookInfo(Document):
    bookName = fields.StringField()
    author = fields.StringField()
    publisher = fields.StringField()
    volume = fields.IntField()
    mrp = fields.FloatField()
    publishYear = fields.IntField()
    expectedPrice = fields.FloatField()
    ispnID = fields.IntField()
    category = fields.StringField(choices=book_categories)

class Address(EmbeddedDocument):
    streetLine1 = fields.StringField()
    streetLine2 = fields.StringField(blank=True)
    streetLine3 = fields.StringField(blank=True)
    streetLine4 = fields.StringField(blank=True)
    zip = fields.StringField(blank=True)
    city = fields.StringField()
    state = fields.StringField(blank=True)
    county = fields.StringField(blank=True)

class Name(EmbeddedDocument):
    title = fields.StringField(blank=True)
    first = fields.StringField(blank=True)
    middle = fields.StringField(blank=True)
    last = fields.StringField(blank=True)
    suffix = fields.StringField(blank=True)
    nickname = fields.StringField(blank=True)

class User(Document):
    name = fields.EmbeddedDocumentField(Name, blank=True)
    home = fields.EmbeddedDocumentField(Address, blank=True, null=True)
    phoneNumber = fields.StringField(blank=True)
    email = fields.EmailField(blank=False, unique=True)
    password = fields.StringField(blank=False, unique=True)

class Session(Document):
    email = fields.ReferenceField(User)
    access_token = fields.StringField(unique=True, default=random_string())
    created_at = fields.DateTimeField(default=datetime.now())

    meta = {
        'indexes': [
            {
                'fields': ['created_at'],
                'expireAfterSeconds': 30,  # 2 hours
            },
        ]
    }