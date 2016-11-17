from django.shortcuts import render
from .forms import ingresarBus,ingresarAsiento,ingresarProgramacion,ingresarDestino,ingresarCliente,ingresarReserva
from django.shortcuts import redirect
from .models import Bus,Programacion,Destino,Cliente,Reserva
from django.shortcuts import render, get_object_or_404
# Create your views here.


def inicio(request):
        return render(request, 'blog/principal.html', {})

def IngresarBus(request):
    if request.method == "POST":
        form = ingresarBus(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/ingresar.html', {'form': form})
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
            return render(request, 'blog/ingresarProgramacion.html', {'form': form})
    else:
        form=ingresarProgramacion()
    return render(request, 'blog/ingresarProgramacion.html', {'form': form})

def IngresarDestino(request):
    if request.method == "POST":
        form = ingresarDestino(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/ingresarDestino.html', {'form': form})
    else:
        form=ingresarDestino()
    return render(request, 'blog/ingresarDestino.html', {'form': form})

def IngresarCliente(request):
    if request.method == "POST":
        form = ingresarCliente(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/ingresarCliente.html', {'form': form})
    else:
        form=ingresarCliente()
    return render(request, 'blog/ingresarCliente.html', {'form': form})

def EditarCliente(request, pk):
        post = get_object_or_404(Cliente, pk=pk)
        if request.method == "POST":
            form = ingresarCliente(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author=request.user
                post.save()
                return redirect('blog/views/listaClienteEdit', pk=post.pk)
        else:
            form = ingresarCliente(instance=post)
        return render(request, 'blog/editarCliente.html', {'form': form})


def IngresarReserva(request):
    if request.method == "POST":
        form = ingresarReserva(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/ingresarReserva.html', {'form': form})
    else:
        form=ingresarReserva()
    return render(request, 'blog/ingresarReserva.html', {'form': form})

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

def ListaClienteEditar(request):
    posts=Cliente.objects.order_by('nombre_cliente')
    return render(request, 'blog/listaClienteEdit.html', {'posts': posts})

def ListaReserva(request):
    posts=Reserva.objects.order_by('fecha_reserva')
    return render(request, 'blog/listaReserva.html', {'posts': posts})
