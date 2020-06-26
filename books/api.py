from rest_framework_mongoengine import viewsets
from books.serializers import BooksSerializer, UsersSerializer
from books.models import BookInfo, User

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = BookInfo.objects.all()

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()