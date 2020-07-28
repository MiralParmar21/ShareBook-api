from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from books import api
from books.views import login

router = DefaultRouter()
router.register(r'books', api.BooksViewSet, basename='BookInfo')
router.register(r'users', api.UsersViewSet, basename='User')
router.register(r'session', api.SessionViewSet, basename='Session')
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^login/', login)
]