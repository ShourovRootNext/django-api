from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

def index(request):
    musician_list = Musician.objects.order_by('first_name','last_name','instrument')
    album_list = Album.objects.order_by('artist', 'name','release_date','num_stars')
    users = {'text_1':'This is a list of Musicians',  'musician': musician_list, 'album':album_list, 'numbers': [1, 2, 3, 4, 5], 'names': ['John Doe', 'Jane Doe', 'Alice', 'Bob', 'Charlie']}
    return render(request,'first_app/index.html',context=users)
def form(request):
    new_form = forms.user_form()
    diction = {'heading_1':'This is a form create by Django Library.', 'test_form':new_form}
    return render(request,'first_app/form.html', context=diction)
def about(request):
    return HttpResponse("<h1>This is about page.</h1> <a href='/contact/'>Contact</a> <a href='/services/'>Services</a>")
def contact(request):
    return HttpResponse(" <h1>This is contact page.</h1> <a href='/services/'>Services</a> <a href='/help/'>Help</a>")
def services(request):
    return HttpResponse("This is services page.")
def help(request):
    return HttpResponse("This is help page.")