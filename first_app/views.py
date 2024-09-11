from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    users = {'numbers': [1, 2, 3, 4, 5], 'names': ['John Doe', 'Jane Doe', 'Alice', 'Bob', 'Charlie']}
    return render(request,'first_app/index.html',context=users)
def about(request):
    return HttpResponse("<h1>This is about page.</h1> <a href='/contact/'>Contact</a> <a href='/services/'>Services</a>")
def contact(request):
    return HttpResponse(" <h1>This is contact page.</h1> <a href='/services/'>Services</a> <a href='/help/'>Help</a>")
def services(request):
    return HttpResponse("This is services page.")
def help(request):
    return HttpResponse("This is help page.")