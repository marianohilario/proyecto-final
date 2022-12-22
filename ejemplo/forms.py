from django import forms
from ejemplo.models import Familiar, Mascota, Vehiculos

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'nacimiento', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'raza', 'nacimiento']

class VehiculoForm(forms.ModelForm):
  class Meta:
    model = Vehiculos
    fields = ['marca', 'modelo']