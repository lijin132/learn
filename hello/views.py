from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader
# Create your views here.

def hello(request):
    t = loader.get_template("index.html")
    c = Context({})
    return HttpResponse(t.render(c))

def dong(request):
    t = loader.get_template("dongtai.html")
    user={"name":"tom","age":23,"haha":"hehe"}
    c = Context({"title":"django","user":user})
    return HttpResponse(t.render(c))