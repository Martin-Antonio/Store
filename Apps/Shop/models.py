from django.db import models


# Create your models here.

class Shop_Men(models.Model):
	Nombre = models.CharField(max_length=100)
	cantidad =models.IntegerField()
	Precio = models.IntegerField()
	imagen1 = models.ImageField(upload_to="media/Image")
	imagen2 = models.ImageField(upload_to="media/Image")
	imagen3 = models.ImageField(upload_to="media/Image")
	imagen4= models.ImageField(upload_to="media/Image")
	descripcion = models.CharField(max_length=50)
	Telefono=models.ManyToManyField('Contacto')

	def __str__(self):
		num=str(self.cantidad)
		vista=self.Nombre +":  " +'Cantidad en existencia'+' :'+ num
		return vista


class Shop_body(models.Model):
	Nombre = models.CharField(max_length=100)
	cantidad =models.IntegerField()
	Precio = models.IntegerField()
	imagen1 = models.ImageField(upload_to="media/Image")
	imagen2 = models.ImageField(upload_to="media/Image")
	imagen3 = models.ImageField(upload_to="media/Image")
	imagen4= models.ImageField(upload_to="media/Image")
	descripcion = models.CharField(max_length=50)
	Telefono=models.ManyToManyField('Contacto')

	def __str__(self):
		num=str(self.cantidad)
		vista=self.Nombre +":  " +'Cantidad en existencia'+' :'+ num
		return vista


class Contacto(models.Model):
	Telefono=models.CharField(max_length=11,primary_key=True)
	
	
	
	def __str__(self):

		return self.Telefono
