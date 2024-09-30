from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TicketCabecera, TicketDetalle
from .forms import TcForm, TdForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html', {'key1': 'valor1', 'key2': 'valor2'})
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def productos(request):
    tc = TicketCabecera.objects.all()
    td = TicketDetalle.objects.all()    
    return render(request, 'productos/index.html', {'productos': tc})


def crear(request):
    # Instanciar el formulario
    formulario1 = TdForm(request.POST or None)

    if request.method == 'POST':
        if formulario1.is_valid():
            formulario1.save()  # Guardar los datos en la base de datos
            return redirect('productos')  # Redirigir a la página de productos u otra página tras guardar

    return render(request, 'productos/crear.html', {
        'formulario1': formulario1
    })

def ccliente(request):
    # Instanciar el formulario
    formulario = TcForm(request.POST or None)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()  # Guardar los datos en la base de datos
            return redirect('productos')  # Redirigir a la página de productos u otra página tras guardar

    return render(request, 'productos/ccliente.html', {
        'formulario': formulario
    })

def mostrar_ticket(request, id):
    ticket_cabecera = TicketCabecera.objects.get(id_ticketCabecera=id)
    ticket_detalles = TicketDetalle.objects.filter(id_ticketCabecera=ticket_cabecera)
    return render(request, 'productos/mostrar_ticket.html', {
        'ticket_cabecera': ticket_cabecera,
        'ticket_detalles': ticket_detalles
    })

