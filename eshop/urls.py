from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls import url



from eshop import views

app_name = "eshop_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('secciones/', views.secciones, name="secciones"),
    path('producto/<int:id>/', views.producto, name="producto"),
    path('logout', LogoutView.as_view(), {"next_page": '/promociones/'}, name="logout"),
    path('signup/', views.signup.as_view(), name="signup"),
    path('update/<int:id>/<int:id2>/', views.update, name="update"),
    path('delete/<int:id>/<int:id2>/', views.delete, name="delete"),
    path('create/<int:id>/', views.create, name="create"),
    path('carrito/<int:id>/', views.carrito, name="carrito"),
    path('agregarcarrito/<int:id>/', views.agregarCarrito, name="agregarcarrito"),
    path('quitarcarrito/<int:id>/', views.quitarcarrito, name="quitarcarrito"),
    path('comprar/', views.comprar, name="comprar"),
    path('createCreditCard/', views.createCreditCard, name="createCreditCard"),
    path('deleteCC/<int:id>', views.deleteCC, name="deleteCC"),
    path('agregarproducto/', views.agregarproducto, name="agregarproducto"),
    path('agregarseccion/', views.agregarseccion, name="agregarseccion"),
    path('productoscomprados/', views.productoscomprados, name="productoscomprados"),
    path('success/', views.success, name="success"),
    path('CompraExitosa/', views.CompraExitosa, name="CompraExitosa"),
    url(r'^results/$', views.search, name='search'),
    
   # url(r'^create/(?P<param>\d+)/$', RedirectSomewhere.as_view(), name="create"),

    
]
