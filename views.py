from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def count(request):
    if request.method=='POST':
        input = request.POST['input']
        word_count = len(input.split())
        return render(request, 'count.html', {'word_count':word_count})


