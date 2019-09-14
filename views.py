from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views import generic
from AppTrans.models import Motorista, RegistroLlegada, UnidadTransporte, PuntoControl, ResponsablePunto
from AppTrans.forms import UsuarioForm, RegistroForm, MotoristaForm, ResponsableForm, UnidadForm, FormularioPuntos, CambioMotoristaForm

# Create your views here.

def home(request):
	return render(request, 'home.html');

#Esta es una vista basada en clases
class registrarUsuario(CreateView): #Hereda de la clase CreateView
	model = User
	template_name = "registrarUsuario.html"
	form_class = UsuarioForm
	success_url = reverse_lazy('home')

#Todas las demás son vistas basadas en funciones
def consultarMotoristas(request):
	#Devuelve los Motoristas ordenados por id (ascendente)
	motoristas=Motorista.objects.all().order_by('id')
	return render(request, 'consultarMotoristas.html', {'motoristas': motoristas})

def consultarPuntos(request):
	puntos=PuntoControl.objects.all().order_by('id')
	return render(request, 'consultarPuntos.html', {'puntos':puntos})

def consultarUnidades(request):
	unidades=UnidadTransporte.objects.all().order_by('id')
	return render(request, 'consultarUnidades.html', {'unidades':unidades})

def consultarRegistros(request):
	registros = RegistroLlegada.objects.all().order_by('id')
	return render(request, 'consultarRegistros.html', {'registros':registros})

#class consultarRegistros(generic.ListView):
#	queryset = RegistroLlegada.objects.all().order_by('id')
#	template_name = "consultarRegistros.html"
#	paginate_by =5

def consultarResponsables(request):
	responsables=ResponsablePunto.objects.all().order_by('id')
	return render(request, 'consultarResponsables.html', {'responsables':responsables})

def verDetalleRegistro(request, id_registro):
	registro = RegistroLlegada.objects.get(id=id_registro)
	return render(request, 'verDetalleRegistro.html', {'registro':registro})

def verDetalleResponsable(request, id_responsable):
	responsable = ResponsablePunto.objects.get(id=id_responsable)
	return render(request, 'verDetalleResponsable.html', {'responsable':responsable})

def verDetalleMotorista(request, id_motorista):
	motorista = Motorista.objects.get(id=id_motorista)
	return render(request, 'verDetalleMotorista.html', {'motorista':motorista})

def verDetalleUnidad(request, id_unidad):
	unidad = UnidadTransporte.objects.get(id=id_unidad)
	return render(request, 'verDetalleUnidad.html', {'unidad':unidad})

def crearRegistro(request):
	if request.method == 'POST':
		formulario = RegistroForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, 'Se guardó el registro')
		return redirect('home')
	else:
		formulario = RegistroForm()

	return render(request, 'crearRegistro.html', {'formulario':formulario})

def crearMotorista(request):
	if request.method == 'POST':
		formulario = MotoristaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario = MotoristaForm()

	return render(request, 'crearMotorista.html', {'formulario':formulario})

def crearResponsable(request):
	if request.method == 'POST':
		formulario = ResponsableForm(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario = ResponsableForm()

	return render(request, 'crearResponsable.html', {'formulario':formulario})

def crearUnidad(request):
	if request.method == 'POST':
		formulario = UnidadForm(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario = UnidadForm()

	return render(request, 'crearUnidad.html', {'formulario':formulario})

def crearPuntos(request):
	if request.method == 'POST':
		formulario = FormularioPuntos(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario = FormularioPuntos()

	return render(request, 'crearPuntos.html', {'formulario':formulario})

def editarPunto(request, id_punto):
	punto = PuntoControl.objects.get(id=id_punto)
	if request.method == 'GET':
		formulario = FormularioPuntos(instance=punto)
	else:
		formulario = FormularioPuntos(request.POST, instance=punto)
		if formulario.is_valid():
			formulario.save()
		return redirect('consultarPuntos')
	return render(request, 'crearPuntos.html', {'formulario':formulario})


def cambiarMotorista(request, id_unidad):
	unidad = UnidadTransporte.objects.get(id=id_unidad)
	if request.method == 'GET':
		formulario = CambioMotoristaForm(instance=unidad)
	else:
		formulario = CambioMotoristaForm(request.POST, instance=unidad)
		if formulario.is_valid():
			formulario.save()
		return redirect('consultarUnidades')
	return render(request, 'cambiarMotorista.html', {'formulario':formulario})

#def cambiarResponsable(request, id_punto):
#	punto = ResponsablePunto.objects.get(id=id_punto)
#	if request.method == 'GET':
#		formulario = PuntoControlForm(instance=punto)
#	else:
#		formulario = PuntoControlForm(request.POST, instance=punto)
#		if formulario.is_valid():
#			formulario.save()
#		return redirect('consultarPuntos')
#	return render(request, 'crearPunto.html', {'formulario':formulario})

def eliminarUnidad(request, id_unidad):
	unidad = UnidadTransporte.objects.get(id=id_unidad)
	if request.method == 'POST':
		unidad.delete()
		return redirect('consultarUnidades')
	return render(request, 'eliminarUnidad.html', {'unidad':unidad})

def eliminarMotorista(request, id_motorista):
	motorista = Motorista.objects.get(id=id_motorista)
	if request.method == 'POST':
		motorista.delete()
		return redirect('consultarMotoristas')
	return render(request, 'eliminarMotorista.html', {'motorista':motorista})

def eliminarResponsable(request, id_responsable):
	responsable = ResponsablePunto.objects.get(id=id_responsable)
	if request.method == 'POST':
		responsable.delete()
		return redirect('consultarResponsables')
	return render(request, 'eliminarResponsable.html', {'responsable':responsable})