from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hellow World!このページは投稿のインデックスです。")
    return render(request, 'posts/index.html')

# Create your views here.
