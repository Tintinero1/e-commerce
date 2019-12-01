from django import forms
from .models import Producto, Comment, CreditCard, seccion#, SeccionProducto

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


STAR = (('1',1),('2',2),('3',3),('4',4),('5',5))

class FormComment(forms.ModelForm):
	Comentar = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
	estrellas = forms.ChoiceField(choices=STAR)
	class Meta:
		model = Comment
		fields = [
			"Comentar",
			"estrellas"
		]

class FormProducto(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	content = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	precio = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	seccion = forms.ModelChoiceField(widget=forms.Select, queryset = seccion.objects.all())
	photo = forms.ImageField()
	class Meta:
		model = Producto
		fields = [
			"name",
			"content",
			"precio",
			"seccion",
			"photo",

		]

class FormSeccion(forms.ModelForm):
	seccion = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = seccion
		fields = [
			"seccion",


		]

#class FormSeccionProducto(forms.ModelForm):
#	product = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset = Producto.objects.all())
#	seccion = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset = seccion.objects.all())
#	
#	class Meta:
#		model = SeccionProducto
#		fields = [
#			"product",
#			"seccion"
#
#
#		]


class FormProductoCarrito(forms.ModelForm):
	carritochecker = forms.BooleanField()
	class Meta:
		model = Producto
		fields = [
			"carritochecker",

		]

class FormProductoPurchased(forms.ModelForm):
	purchased = forms.BooleanField()
	class Meta:
		model = Producto
		fields = [
			"purchased",

		]

class FormCreditCard(forms.ModelForm):
	Numero_De_Tarjeta = 0
	Mes = 0
	Año = 0
	CVV = 0
	class Meta:
		model = CreditCard
		fields = [
			"CardNumber",
			"Month",
			"Year",
			"cvv"
		]
	


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'size':30}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':30}))

class SignupForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))

	class Meta:
		model = User
		fields = [
			"first_name",
			"last_name",
			"email",
			"username",
			"password1",
			"password2"
		]