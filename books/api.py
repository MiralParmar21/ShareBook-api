from rest_framework_mongoengine import viewsets
from books.serializers import BooksSerializer, UsersSerializer, SessionSerializer
from books.models import BookInfo, User, Session
from books.utils import is_logged

class LoginViewSet(viewsets.ModelViewSet):
    pass
    @is_logged
    def list(self, request, *args, **kwargs):
        return super(LoginViewSet, self).list(request, *args, **kwargs)

class BooksViewSet(LoginViewSet):
    serializer_class = BooksSerializer
    queryset = BookInfo.objects.all()

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()
