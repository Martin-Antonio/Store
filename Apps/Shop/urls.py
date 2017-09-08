
from django.conf.urls import url
from Apps.Shop import views

  


urlpatterns = [
   

   url(r'^', views.home.as_view(), name='body'),




   ]
