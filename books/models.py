from mongoengine import Document, fields, EmbeddedDocument
# Create your models here.
book_categories = ["Novel", "Science", "Space", "History"]

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
    email = fields.EmailField(blank=False)

