from django.http import HttpResponse, JsonResponse
from .models import Book, Game
from .serializers import BookSerializer, GameSerializer
from rest_framework.parsers import JSONParser

def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def book_single(request, title):
    try:
        book = Book.objects.get(title=title)
    except:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        book.delete()
        return HttpResponse(status=204)