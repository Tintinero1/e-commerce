from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import  Producto, Counter, Comment, CreditCard, seccion, historialcompras, PromEst
from django.views.generic.base import RedirectView
from django.db.models import Sum, Q, Avg
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage
import random
#from example.config import pagination


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import FormComment, LoginForm, SignupForm,  FormCreditCard, FormSeccion, FormProductoCarrito, FormProductoPurchased, FormProducto

queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
lol = queryCONTADORCARRITO.count()

# Create your views here.
def index(request):
	#promestrellas = Comment.objects.filter(producto=producto)

	stars = PromEst.objects.all()
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	message = "Not Logged yet"
	querysetIndex = Producto.objects.all()
	form = LoginForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			#data = form.cleaned_data
			#print(data)
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username, password=password)
			#print(username)
			#print(password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "User Logged"
				else:
					message = "User Not Active"
			else:
				message = "Username or password is not Correct"
		context = {
			"message": message,
			"form": form,
			"username": username,
			"objects": querysetIndex,
			"lol":lol,
			"stars":stars,
		}
	context = {
		"form": form,
		"lol":lol,
		"message": message,
		"objects": querysetIndex,
		"stars":stars,
	}
	return render(request, "eshop/index.html", context)

def secciones(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()

	prd = seccion.objects.all()
	
	context = {
		"lol":lol,
		"stars":prd,
		
	}
	return render(request, "eshop/secciones.html", context)






#	context = {
#		"lol":lol,
#		"prom":prom,
#		
#	}
#	return render(request, "eshop/index.html", context)

def producto(request, id):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	clave = id
	querysetComments = Comment.objects.filter(producto=id)
	queryset = Producto.objects.filter(id=id)
	validator = Producto.objects.get(id=id)

	var_title = queryset[0]
	counter = Counter
	form = FormComment()
	form2 = FormProductoCarrito()
	us = request.user
	sec = Producto.objects.all()
	flag = False
	if validator.carritochecker:
		flag = True

	context = {
	"objects": queryset,
	"lol":lol,
	"counter": counter,
	"title": var_title,
	"querysetComments": querysetComments,
	"create_form": FormComment(),
	"create_url": reverse_lazy("eshop_app:create",kwargs={'id': id},current_app='eshop'),
	"clave": clave,
	"carrito_form": form2,
	"carrito_url": reverse_lazy("eshop_app:agregarcarrito",kwargs={'id': id},current_app='eshop'),
	"sec":sec,
	"us":us,
	"flag":flag,
	"validator":validator

	}
	return render(request, "eshop/producto.html", context)

def carrito(request, id):
	message = "No hay productos en el carrito."
	flag = False
	queryTitle = Producto.objects.filter(id=id)
	queryPRODUCTOS = Producto.objects.filter(carritochecker=True)
	lol = queryPRODUCTOS.count()
	if lol > 1:
		message = " Productos en el carrito"
		Flag = True
	elif lol == 1:
		message = " Producto en el carrito"
		Flag = True
	else:
		message = message
		Flag = False
	#var_title = queryTitle[0]
	form = FormProductoCarrito()
	
	#form.fields["producto"].initial = Producto.objects.get(id=id)
	if form.is_valid():
		#Comment = form.save(commit=False)
		#form.fields.cleaned_data['producto'] = 2
		instance = form.save(commit=False)
		instance.carritochecker = True
		instance.save()
	context = {
		"productoID":id,
		"queryPRODUCTOS": queryPRODUCTOS,
		#"title": var_title,
		"message":message,
		"Flag":Flag,
		"lol":lol
	}
	return render(request, "eshop/carrito.html", context)

def comprar(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	queryPRODUCTOS = Producto.objects.filter(carritochecker=True)
	total = 0
	flag = False
	form = FormCreditCard()
	queryCARD = CreditCard.objects.filter(user=request.user)
	if queryCARD.count() > 0:
		flag = True
	else:
		flag = False
	prpchased = FormProductoPurchased()
	#for x in var_title:
	#	lol += var_title.precio
	total = Producto.objects.filter(carritochecker=True).aggregate(Sum('precio'))['precio__sum']
	context = {
		#"productoID":id,
		"queryPRODUCTOS": queryPRODUCTOS,
		"lol":lol,
		"form":form,
		"create_url": reverse_lazy("eshop_app:createCreditCard",current_app='eshop'),
		"CreditCard_form": form,
		"queryCARD":queryCARD,
		"flag":flag,
		"total":total,
		"purchased_form": prpchased,
		"carrito_url":reverse_lazy("eshop_app:success",current_app='eshop'),
	}
	return render(request, "eshop/comprar.html", context)
#Signup View
class signup(generic.CreateView):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	template_name = "eshop/signup.html"
	model = User
	form_class = SignupForm
	success_url = reverse_lazy("eshop_app:index")

def delete(request, id, id2):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	queryComment = Comment.objects.get(id=id)
	if request.method=="POST":
		queryComment.delete()

		#avg en productos
		prds = Producto.objects.all()
		res = 0
		for obj in prds:
			p = Producto.objects.get(id=obj.id)
			open = Comment.objects.filter(producto=obj.id)
			if open.count() == 0:
				res = 1
				d = PromEst.objects.filter(producto=p)
				if d.count() > 0:
					d.delete()
				avg = PromEst.objects.create(producto=p, calificacion=res)
				avg.save()
			else:
				res = Comment.objects.filter(producto=obj.id).aggregate(Avg('estrellas'))['estrellas__avg']
				d = PromEst.objects.filter(producto=p)
				if d.count() > 0:
					d.delete()
				avg = PromEst.objects.create(producto=p, calificacion=res)
				avg.save()

		return redirect("eshop_app:producto",id2)
	context = {
		#"form": form,
		"tweet": queryComment,
		"lol":lol,
		"id2":id2

	}
	return render(request, "eshop/delete.html", context)

def deleteCC(request, id):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	queryCC = CreditCard.objects.get(id=id)
	if request.method=="POST":
		queryCC.delete()
		return redirect("eshop_app:comprar")
	context = {
		#"form": form,
		"queryCC": queryCC,
		"lol":lol

	}
	return render(request, "eshop/deleteCC.html", context)

def update(request, id, id2):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	redir = id2
	object_tweet = Comment.objects.get(id=id)
	if request.method == "GET":
		form = FormComment(instance=object_tweet)
	else:
		form = FormComment(request.POST, instance=object_tweet)
		if form.is_valid():

			#avg en productos
			prds = Producto.objects.all()
			res = 0
			for obj in prds:
				p = Producto.objects.get(id=obj.id)
				open = Comment.objects.filter(producto=obj.id)
				if open.count() == 0:
					res = 1
					d = PromEst.objects.filter(producto=p)
					if d.count() > 0:
						d.delete()
					avg = PromEst.objects.create(producto=p, calificacion=res)
					avg.save()
				else:
					res = Comment.objects.filter(producto=obj.id).aggregate(Avg('estrellas'))['estrellas__avg']
					d = PromEst.objects.filter(producto=p)
					if d.count() > 0:
						d.delete()
					avg = PromEst.objects.create(producto=p, calificacion=res)
					avg.save()

			form.save()
		return redirect("eshop_app:producto",redir)
	context = {
		"form": form,
		"lol":lol
	}
	return render(request, "eshop/update.html", context)

def create(request, id):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()



	form = FormComment(request.POST or None)
	#form.fields["producto"].initial = Producto.objects.get(id=id)
	if form.is_valid():
		#Comment = form.save(commit=False)
		#form.fields.cleaned_data['producto'] = 2
		instance = form.save(commit=False)
		instance.user = request.user
		instance.producto = id
		instance.save()

		#avg en productos
		prds = Producto.objects.all()
		res = 0
		for obj in prds:
			p = Producto.objects.get(id=obj.id)
			open = Comment.objects.filter(producto=obj.id)
			if open.count() == 0:
				res = 1
				d = PromEst.objects.filter(producto=p)
				if d.count() > 0:
					d.delete()
				avg = PromEst.objects.create(producto=p, calificacion=res)
				avg.save()
			else:
				res = Comment.objects.filter(producto=obj.id).aggregate(Avg('estrellas'))['estrellas__avg']
				d = PromEst.objects.filter(producto=p)
				if d.count() > 0:
					d.delete()
				avg = PromEst.objects.create(producto=p, calificacion=res)
				avg.save()

		return redirect('eshop_app:producto',id)
		#return reverse_lazy('eshop_app:producto',kwargs={'id': 2},current_app='eshop')
	else:
		form = FormComment()
		context = {
			"form": form,
			"lol":lol
		}
		return render(request, "eshop/create.html", context)

#def agregarCarrito(request, id):
#	obj = Producto.objects.get(id=id)
#	carrito
#		return render(request, "eshop/agregarcarrito.html", context)

def agregarCarrito(request, id):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	open = Producto.objects.get(id=id)
	open.carritochecker = True
	open.save()
	return redirect("eshop_app:carrito",id)
	context = {
		#"form": form
		"lol":lol
		}
	return render(request, "eshop/agregarcarrito.html", context)

#class RedirectSomewhere(RedirectView):
#	param = 2
 #   def get_redirect_url(self, param):
#        return reverse_lazy("eshop_app:index",
 #                           kwargs={'param': param},
  #                          current_app='myapp')

def quitarcarrito(request, id):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	open = Producto.objects.get(id=id)
	open.carritochecker = False
	open.save()
	return redirect("eshop_app:carrito",id)
	context = {
		"lol":lol


	}
	return render(request, "eshop/delete.html", context)

def createCreditCard(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	form = FormCreditCard(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('eshop_app:comprar')
	else:
		form = FormCreditCard()
		context = {
			"form": form,
			"lol":lol
		}
		return render(request, "eshop/createCreditCard.html", context)

def agregarproducto(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	form = FormProducto(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		#avg en productos
		prds = Producto.objects.all()
		res = 0
		for obj in prds:
			p = Producto.objects.get(id=obj.id)
			open = Comment.objects.filter(producto=obj.id)
			if open.count() == 0:
				res = 1
				d = PromEst.objects.filter(producto=p)
				if d.count() > 0:
					d.delete()
				avg = PromEst.objects.create(producto=p, calificacion=res)
				avg.save()
			else:
				res = Comment.objects.filter(producto=obj.id).aggregate(Avg('estrellas'))['estrellas__avg']
				d = PromEst.objects.filter(producto=p)
				if d.count() > 0:
					d.delete()
				avg = PromEst.objects.create(producto=p, calificacion=res)
				avg.save()

			
		#instance = form.save(commit=False)
		#instance.save()
		return redirect('eshop_app:index')
	else:
		form = FormProducto()
		context = {
			"form": form,
			"lol":lol
		}
		return render(request, "eshop/agregarproducto.html", context)

def agregarseccion(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()

	form = FormSeccion(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('eshop_app:index')
	else:
		form = FormSeccion()
		context = {
			"form": form,
			"lol":lol
		}
		return render(request, "eshop/agregarseccion.html", context)

def search(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	template = 'eshop/index.html'


	query = request.GET.get('q')

	if query:
		results = PromEst.objects.filter(Q(producto__name__icontains=query) | Q(producto__content__icontains=query) 
			| Q(producto__precio__icontains=query)| 
			Q(producto__seccion__seccion__icontains=query))
	else:
		results = PromEst.objects.all()
	

	#pages = pagination(request, results, num=1)
	context = {
		"stars": results,
		"lol": lol,
		#"items": pages[0],
		#"page_range":pages[1],
		}
	return render(request, template, context)

def productoscomprados(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	purchas = 0
	message = " "
	Flag = False
	queryCONTADORpurchased = Producto.objects.filter(purchased=True)
	if request.user.is_authenticated:

		prodcomp = historialcompras.objects.filter(user=request.user)
		message = "El historial esta vacio"
		purchas = queryCONTADORpurchased.count()

		queryPP = Producto.objects.filter(purchased=True)
		if purchas > 1:
			message = ""
			Flag = True
		elif purchas == 1:
			message = ""
			Flag = True
		else:
			message = message
			Flag = False
	else:
		message = "Favor de iniciar sesion para ver su historial."
		prodcomp = 0
		Flag = False
		queryPP = 0
		
#	for obj in prodcomp:
#		print (obj.producto)
#		#idp = prodcomp.producto.id
#		#Producto.objects.filter(id=idp)

	

	context = {
		"queryPP":queryPP,
		"message":message,
		"Flag":Flag,
		"purchas":purchas,
		"lol":lol,
		"prodcomp":prodcomp
	}
	return render(request, "eshop/productoscomprados.html", context)

def CompraExitosa(request):
	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	prod = Producto.objects.filter(carritochecker = True)

	total = Producto.objects.filter(carritochecker=True).aggregate(Sum('precio'))['precio__sum']
	leademail = []

	for pro in prod:
		time = pro.timestamp
		res = pro.name
		leademail.append(res)

	leademail = '\n\n'.join(leademail)
	
	if prod.count() <= 0:
		total = 0
		time = 0

	email = EmailMessage('Recibo EShop', str(request.user) + ', Muchas gracias por tu compra, espero te veamos pronto! \n\n' + 
		'Tus productos seran procesados y enviados enseguida!:\n\n'

	+	str(leademail) + '\n\nTotal de la compra: ' + str(total) + 'Dlls' + '\nFecha de recibo: ' + str(time), to=[request.user.email])
	
	if prod.count() >0:
		email.send()
		
	allproductsPurchased = Producto.objects.filter(carritochecker = True)
	for obj in allproductsPurchased:
		obj.carritochecker = False
		obj.save()
	context = {
		"lol":lol,
		"allproductsPurchased":allproductsPurchased,
		}
	return render(request, "eshop/CompraExitosa.html", context)

def success(request):

	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()

	
	open = Producto.objects.filter(carritochecker=True)
	for obj in open:
		obj.purchased = True
		obj.save()
		if obj.purchased:
			producto = Producto.objects.get(id=obj.id)
			histc = historialcompras.objects.create(user = request.user, producto=producto)
			histc.save()

	
	jan = Producto.objects.filter(purchased=True)
	#return redirect("eshop_app:success")
	return redirect("eshop_app:CompraExitosa")
	context = {
		"queryPRODUCTOS": jan,
		"lol":lol
		}
	return render(request, "eshop/success.html", context)

def sec(request):

	lol = 0
	queryCONTADORCARRITO = Producto.objects.filter(carritochecker=True)
	lol = queryCONTADORCARRITO.count()
	template = "eshop:secciones"

	results = seccion.objects.all()
	context = {
		"results": results,
		"lol":lol
		}
	return render(request, template, context)

