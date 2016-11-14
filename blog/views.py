from django.shortcuts import render
from .forms import ingresarBus,ingresarAsiento,ingresarProgramacion,ingresarDestino,ingresarCliente,ingresarReserva
from django.shortcuts import redirect

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

    
