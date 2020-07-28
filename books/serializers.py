from rest_framework_mongoengine import serializers
from books.models import BookInfo, User, Session

class BooksSerializer(serializers.DocumentSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"

class UsersSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SessionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Session
        fields = ['email']