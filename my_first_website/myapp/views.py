from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Book
import json

def index(request):
    return HttpResponse("this is the default response!")


def book_by_id(request, book_id):
    book = Book.objects.get(id=book_id)

    # return HttpResponse(f"Book : {book.title}, published on date : {book.pub_date}")
    return render(request, 'book_details.html', {'book' : book})


def show_all_books(request):
    querySet = Book.objects.all()
    serialized_data = serialize('json', querySet)
    serialized_data = json.loads(serialized_data)
    # print(querySet)
    
    # for i in querySet:
    #     print(HttpResponse(i.title))

    context = {
        'all_books' : querySet
    }
    template_name = 'all_books.html'

    
    # return render(request, template_name, context)
    # return HttpResponse(json.dumps(querySet))
    return JsonResponse(serialized_data, safe = False)




# To return JsonResponse, in your views you can do as
# JsonResponse(serialized_data, safe=False, status=200)