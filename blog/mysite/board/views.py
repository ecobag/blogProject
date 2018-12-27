from django.shortcuts import render, get_object_or_404
from .models import boardDB
# Create your views here.

def index(request):
    board_list = boardDB.objects.all()
    data = {'board_list': board_list}
    return render(request,'board/index.html', data)

def detail(request):
    board_list = boardDB.objects.all()
    data = {'board_list': board_list}
    return render(request, 'board/detail.html', data)