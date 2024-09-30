from django.db import models

class TicketCabecera(models.Model):
    id_ticketCabecera = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha")
    nombreCliente = models.CharField(verbose_name="Cliente", max_length=100)
    celular = models.CharField(verbose_name="Celular", max_length=11)
    distrito = models.CharField(verbose_name="Distrito", max_length=100)
    total = models.DecimalField(verbose_name="Total", max_digits=10, decimal_places=2)

    def __str__(self):
        # Convertir 'fecha' a cadena antes de concatenar
        return f"Fecha: {self.fecha.strftime('%Y-%m-%d')} - Cliente: {self.nombreCliente} - Celular: {self.celular} - Distrito: {self.distrito} - Total: {self.total}"

class TicketDetalle(models.Model):
    id_ticketDetalle = models.AutoField(primary_key=True)
    id_ticketCabecera = models.ForeignKey(TicketCabecera, on_delete=models.CASCADE)
    nombreProducto = models.CharField(verbose_name="Producto", max_length=100)
    precioUnidad = models.DecimalField(verbose_name="Precio Unidad", max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        fila = "nombreProducto" + self.nombreProducto + "-" + "precioUnidad" + self.precioUnidad + "-" + "cantidad" + self.cantidad 
        return fila
        return self.nombreProducto
