
from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Mascota, Vehiculos
from ejemplo.forms import Buscar, FamiliarForm, MascotaForm, VehiculoForm
from django.views import View

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_mascotas(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})

def mostrar_vehiculos(request):
    lista_vehiculos = Vehiculos.objects.all()
    return render(request, "ejemplo/vehiculos.html", {"lista_vehiculos": lista_vehiculos})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "nacimiento":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Familiar {form.cleaned_data.get('nombre')} cargado con éxito!"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"nombre":"", "raza":"", "nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Mascota {form.cleaned_data.get('nombre')} cargado con éxito!"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaVehiculo(View):

    form_class = VehiculoForm
    template_name = 'ejemplo/alta_vehiculo.html'
    initial = {"marca":"", "modelo":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Vehiculo {form.cleaned_data.get('modelo')} cargado con éxito!"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "nacimiento":"", "numero_pasaporte":""}
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"nombre":"", "raza":"", "nacimiento":""}
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarVehiculo(View):
  form_class = VehiculoForm
  template_name = 'ejemplo/actualizar_vehiculo.html'
  initial = {"marca":"", "modelo":""}
  
  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculos, pk=pk)
      form = self.form_class(instance=vehiculo)
      return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})

  def post(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculos, pk=pk)
      form = self.form_class(request.POST ,instance=vehiculo)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito el vehiculo {form.cleaned_data.get('modelo')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'vehiculo': vehiculo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})
      
      return render(request, self.template_name, {})

class BorrarMascota(View):
  template_name = 'ejemplo/mascotas.html'
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      mascota.delete()
      mascotas = Mascota.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascotas})
      
      return render(request, self.template_name, {})

class BorrarVehiculo(View):
  template_name = 'ejemplo/vehiculos.html'
  
  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculos, pk=pk)
      vehiculo.delete()
      vehiculos = Vehiculos.objects.all()
      return render(request, self.template_name, {'lista_vehiculos': vehiculos})
      
      return render(request, self.template_name, {})

