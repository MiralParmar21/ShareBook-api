from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from books.models import User, Session

@csrf_exempt
def login(request):
    user_data = request.POST
    mail = user_data['mail']
    pwd = user_data['pwd']

    user = User.objects.get(email=mail, password=pwd)
    if user:
        session = Session.objects.create(email=mail)
        return JsonResponse({'mail':mail, 'access_token':session.access_token})

    return JsonResponse({'msg':"Invalid User"})

