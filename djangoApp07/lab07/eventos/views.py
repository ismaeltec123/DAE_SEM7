from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, RegistroEvento
from .forms import EventoForm, RegistroEventoForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def crear_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
def actualizar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/actualizar_evento.html', {'form': form})

@login_required
def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == "POST":
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})



@login_required
def registrar_usuario(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Verificar si el usuario ya está registrado en el evento
    registro_existente = RegistroEvento.objects.filter(usuario=request.user, evento=evento).exists()
    
    if not registro_existente:
        # Crear el registro del usuario en el evento
        registro = RegistroEvento(usuario=request.user, evento=evento)
        registro.save()
        mensaje = "Te has registrado correctamente en el evento."
    else:
        mensaje = "Ya estás registrado en este evento."
    
    return render(request, 'eventos/registro_exitoso.html', {'evento': evento, 'mensaje': mensaje})
