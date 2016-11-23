from django.shortcuts import render
from .forms import ingresarBus,ingresarAsiento,ingresarProgramacion,ingresarDestino,ingresarCliente,ingresarReserva,RegistroForm
from django.shortcuts import redirect
from .models import Bus,Programacion,Destino,Cliente,Reserva
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
### Create your views here.
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
###


class RegistroUsuario(CreateView):
    model = User
    template_name = "blog/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('inicio')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/inicio/")
    else:
        # Show an error page
        return redirect('blog.views.login')

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

# inicios

def inicio(request):
    return render(request, 'blog/inicio.html', {})

def BusInicio(request):
    return render(request,'blog/BusInicio.html',{})

def ClienteInicio(request):
    return render(request,'blog/ClienteInicio.html',{})

def ProgramacionInicio(request):
    return render(request,'blog/ProgramacionInicio.html',{})

def DestinoInicio(request):
    return render(request,'blog/DestinosInicio.html',{})

def ReservaInicio(request):
    return render(request,'blog/ReservaInicio.html',{})

#Ingresar

def IngresarBus(request):
    if request.method == "POST":
        form = ingresarBus(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.BusInicio')
            #return render(request, 'blog/listaBus.html', {'form': form})
    else:
        form=ingresarBus()
    return render(request, 'blog/ingresar.html', {'form': form})

def IngresarAsiento(request):
    if request.method == "POST":
        form = ingresarAsiento(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/ingresarAsiento.html', {'form': form})
    else:
        form=ingresarAsiento()
    return render(request, 'blog/ingresarAsiento.html', {'form': form})

def IngresarProgramacion(request):
    if request.method == "POST":
        form = ingresarProgramacion(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.ProgramacionInicio')
    else:
        form=ingresarProgramacion()
    return render(request, 'blog/ingresarProgramacion.html', {'form': form})

def IngresarDestino(request):
    if request.method == "POST":
        form = ingresarDestino(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.DestinoInicio')
    else:
        form=ingresarDestino()
    return render(request, 'blog/ingresarDestino.html', {'form': form})

def IngresarCliente(request):
    if request.method == "POST":
        form = ingresarCliente(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.ClienteInicio')
    else:
        form=ingresarCliente()
    return render(request, 'blog/ingresarCliente.html', {'form': form})

def IngresarReserva(request):
    if request.method == "POST":
        form = ingresarReserva(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.ReservaInicio')
    else:
        form=ingresarReserva()
    return render(request, 'blog/ingresarReserva.html', {'form': form})

#Listas
        #osts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
def ListaBus(request):
    posts=Bus.objects.order_by('placa_bus')
    return render(request, 'blog/listaBus.html', {'posts': posts})

def ListaProgramacion(request):
    posts=Programacion.objects.order_by('hora')
    return render(request, 'blog/listaProgramacion.html', {'posts': posts})

def ListaDestino(request):
    posts=Destino.objects.order_by('lugar_destino')
    return render(request, 'blog/listaDestino.html', {'posts': posts})

def ListaCliente(request):
    posts=Cliente.objects.order_by('nombre_cliente')
    return render(request, 'blog/listaCliente.html', {'posts': posts})

def ListaReserva(request):
    posts=Reserva.objects.order_by('fecha_reserva')
    return render(request, 'blog/listaReserva.html', {'posts': posts})

# Lista Editar

def ListaBusEditar(request):
    posts=Bus.objects.order_by('placa_bus')
    return render(request, 'blog/listaBusEdit.html', {'posts': posts})

def ListaClienteEditar(request):
    posts=Cliente.objects.order_by('nombre_cliente')
    return render(request, 'blog/listaClienteEdit.html', {'posts': posts})

def ListaProgramacionEditar(request):
    posts=Programacion.objects.order_by('hora')
    return render(request, 'blog/listaProgramacionEdit.html', {'posts': posts})

def ListaDestinoEditar(request):
    posts=Destino.objects.order_by('lugar_destino')
    return render(request, 'blog/listaDestinoEdit.html', {'posts': posts})

def ListaReservaEditar(request):
    posts=Reserva.objects.order_by('fecha_reserva')
    return render(request, 'blog/listaReservaEdit.html', {'posts': posts})

# Lista EliminarBus

def ListaBusEliminar(request):
    posts=Bus.objects.order_by('placa_bus')
    return render(request, 'blog/listaBusEliminar.html', {'posts': posts})

def ListaClienteEliminar(request):
    posts=Cliente.objects.order_by('nombre_cliente')
    return render(request, 'blog/listaClienteEliminar.html', {'posts': posts})

def ListaDestinoEliminar(request):
    posts=Destino.objects.order_by('lugar_destino')
    return render(request, 'blog/listaDestinoEliminar.html', {'posts': posts})

def ListaProgramacionEliminar(request):
    posts=Programacion.objects.order_by('hora')
    return render(request, 'blog/listaProgramacionEliminar.html', {'posts': posts})

def ListaReservaEliminar(request):
    posts=Reserva.objects.order_by('fecha_reserva')
    return render(request, 'blog/listaReservaEliminar.html', {'posts': posts})

# editar

def EditarCliente(request, pk):
    posts=Cliente.objects.order_by('nombre_cliente')
    post = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ingresarCliente(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.ListaClienteEditar')
    else:
        form = ingresarCliente(instance=post)
    return render(request, 'blog/editarCliente.html', {'form': form})

def EditarBus(request, pk):
    posts=Bus.objects.order_by('placa_bus')
    post = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        form = ingresarBus(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.ListaBusEditar')
    else:
        form = ingresarBus(instance=post)
    return render(request, 'blog/editarBus.html', {'form': form})

def EditarProgramacion(request, pk):
    posts=Programacion.objects.order_by('hora')
    post = get_object_or_404(Programacion, pk=pk)
    if request.method == "POST":
        form = ingresarProgramacion(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.ListaProgramacionEditar')
    else:
        form = ingresarProgramacion(instance=post)
    return render(request, 'blog/editarProgramacion.html', {'form': form})

def EditarDestino(request, pk):
    posts=Destino.objects.order_by('lugar_destino')
    post = get_object_or_404(Destino, pk=pk)
    if request.method == "POST":
        form = ingresarDestino(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.ListaDestinoEditar')
    else:
        form = ingresarDestino(instance=post)
    return render(request, 'blog/editarDestino.html', {'form': form})

def EditarReserva(request, pk):
    posts=Reserva.objects.order_by('fecha_reserva')
    post = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ingresarReserva(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.ListaReservaEditar')
    else:
        form = ingresarReserva(instance=post)
    return render(request, 'blog/editarReserva.html', {'form': form})

# Eliminar

def EliminarBus(request, pk):
    post = get_object_or_404(Bus, pk=pk)
    post.delete()
    return redirect('blog.views.ListaBusEliminar')
    #return render (request, 'blog/listaBusEliminar.html',{'form':post})

def EliminarCliente(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    post.delete()
    return redirect('blog.views.ListaClienteEliminar')

def EliminarDestino(request, pk):
    post = get_object_or_404(Destino, pk=pk)
    post.delete()
    return redirect('blog.views.ListaDestinoEliminar')

def EliminarProgramacion(request, pk):
    post = get_object_or_404(Programacion, pk=pk)
    post.delete()
    return redirect('blog.views.ListaProgramacionEliminar')

def EliminarReserva(request, pk):
    post = get_object_or_404(Reserva, pk=pk)
    post.delete()
    return redirect('blog.views.ListaReservaEliminar')
