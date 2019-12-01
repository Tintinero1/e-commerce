from django.db import models
from django.conf import settings
from django.utils import timezone


User = settings.AUTH_USER_MODEL


# Create your models here.


class historialcompras(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.producto

class seccion(models.Model):
	seccion = models.CharField(max_length=256)

	def __str__(self):
		return self.seccion


class Producto(models.Model):
	name = models.CharField('Nombre' ,max_length=256)
	content = models.CharField(max_length=1024)
	precio = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(upload_to="gallery")
	carritochecker = models.BooleanField(default=False)
	purchased = models.BooleanField(default=False)  
	seccion = models.ForeignKey(seccion, on_delete=models.CASCADE,)


	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name


#class SeccionProducto(models.Model):
#	product = models.ForeignKey(Producto, on_delete=models.CASCADE)
#	seccionn = models.ForeignKey(seccion, on_delete=models.CASCADE)
#
#	def __unicode__(self):
#		return "%s esta en la seccion %s" % (self.product, self.seccion)

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''

# Create your models here.

STAR = (('1',1),('2',2),('3',3),('4',4),('5',5))
class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	Comentar = models.CharField(max_length=256)
	timestamp = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now_add=True)
	producto = models.IntegerField()
	estrellas = models.CharField(max_length=256, choices = STAR)

	class Meta:
		ordering = ["-timestamp"]

	def __str__(self):
		return self.Comentar

class PromEst(models.Model):
	producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
#	comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
	calificacion = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		ordering = ["-producto"]
	def __str__(self):
		return self.calificacion

class CreditCard(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	CardNumber = models.BigIntegerField()
	Month = models.PositiveSmallIntegerField()
	Year = models.PositiveSmallIntegerField()
	cvv = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.user)
'''
class Ruleta(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	CardNumber = models.BigIntegerField()
	Month = models.PositiveSmallIntegerField()
	Year = models.PositiveSmallIntegerField()
	cvv = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.user)
'''

#class Carrito(models.Model):
#	user = models.ForeignKey(User, null=True, blank=True)
#	producto = models.ManyToManyField(Producto, blank=True)
#	timestamp = models.DateTimeField(auto_now_add=True)
#	updated = models.DateTimeField(auto_now=True)
#	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

#	def __str__(self):
#		return str(self.id)



			