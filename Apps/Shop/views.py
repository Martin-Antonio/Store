from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.







class home(ListView):
	model= Shop_Men
	template_name='index.html'
	paginate_by = 3
	
		
	


class body(ListView):
	model= Shop_body
	template_name='articulo.html'
	paginate_by =3


		