import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from ads.models import Cat, Ads


# from .models import Ads, Cat

# Create your views here.
def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@csrf_exempt
def getads(request):
    if request.method == "GET":
        categories = Ads.objects.all()
        response = []
        for x in categories:
            response.append({"id": x.id,
                             'name': x.name,
                             'author': x.author,
                             'price': x.price,
                             'description': x.description,
                             'address': x.address,
                             'is_published': x.is_published})
        return JsonResponse(response, safe=False)
    if request.method == 'POST':
        ads_data = json.loads(request.body)
        ads1 = Ads.objects.create(
            name = ads_data['name'],
            author = ads_data['author'],
            price = ads_data['price'],
            description = ads_data['description'],
            address = ads_data['address'],
            is_published = ads_data['is_published'],
        )

        return JsonResponse({
            "id": ads1.id,
            "name": ads1.name,
            "author": ads1.author,
            "price": ads1.price,
            "description": ads1.description,
            "address": ads1.address,
            "is_published": ads1.is_published
        })


@csrf_exempt
def getcat(request):
    if request.method == "GET":
        categories = Cat.objects.all()
        response = []
        for x in categories:
            response.append({"id": x.id,
                             'name': x.name,
                             })
        return JsonResponse(response, safe=False)

    elif request.method == 'POST':
        cat_data = json.loads(request.body)
        cat = Cat.objects.create(
            name=cat_data['name'],
        )

        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        })


@csrf_exempt
def getads_id(request,number):
    if request.method == "GET":
        number = request.get()
        categories = Ads.get.object()
        response = []
        for x in categories:
            response.append({"id": x.id,
                             'name': x.name,
                             'author': x.author,
                             'price': x.price,
                             'description': x.description,
                             'address': x.address,
                             'is_published': x.is_published})
        return JsonResponse(response, safe=False)
# Реализуйте для /cat метод GET.
# Реализуйте для /ad метод GET.
# Реализуйте для /cat/:id метод GET.
# Реализуйте для /ad/:id метод GET.
# Реализуйте для /cat метод POST.
# Реализуйте для /ad метод POST.
