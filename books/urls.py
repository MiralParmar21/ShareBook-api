from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from books import api


router = DefaultRouter()
router.register(r'books', api.BooksViewSet, basename='BookInfo')
router.register(r'users', api.UsersViewSet, basename='User')
urlpatterns = [
    url(r'^api/', include(router.urls)),
]