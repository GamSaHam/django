from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def index(request):
    msg = 'My Message'

    class MyClass:
        x = 5
        name = 'foo'

    p1 = MyClass()

    dataList = [1, 2, 3]


    now = datetime.datetime.now()

    return render(request, 'index.html', {'message':msg, 'p1': p1, 'dataList': dataList, 'now': now})





