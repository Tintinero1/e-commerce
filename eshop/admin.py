from django.contrib import admin
from .models import  Comment, CreditCard, seccion, Producto, historialcompras, PromEst
# Register your models here.

admin.site.register(Comment)
admin.site.register(CreditCard)
admin.site.register(seccion)
admin.site.register(Producto)
admin.site.register(historialcompras)
admin.site.register(PromEst)