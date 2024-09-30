from django.contrib import admin
from django.urls import path
from django.urls import include
from productosVendidos.views import inicio, nosotros, productos, crear, ccliente, mostrar_ticket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('productos/', productos, name='productos'),
    path('productos/ccliente', ccliente, name='ccliente'),
    path('productos/crear', crear, name='crear'),
    path('mostrar_ticket/<int:id>/', mostrar_ticket, name='mostrar_ticket'),
]
