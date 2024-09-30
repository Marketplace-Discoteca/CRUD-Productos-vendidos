from django import forms
from .models import TicketCabecera, TicketDetalle

# Formulario para TicketCabecera
class TcForm(forms.ModelForm):
    class Meta:
        model = TicketCabecera
        fields = '__all__'  # O puedes especificar los campos que deseas mostrar

# Formulario para TicketDetalle
class TdForm(forms.ModelForm):
    class Meta:
        model = TicketDetalle
        fields = '__all__'  # O especifica los campos necesarios
