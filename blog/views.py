from django.shortcuts import render
from .forms import ingresarBus,ingresarAsiento
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
