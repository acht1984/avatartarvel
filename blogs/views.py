from django.shortcuts import render


def index(request):
    """docstring for index"""
    return render(request, 'blogs/index.html')
