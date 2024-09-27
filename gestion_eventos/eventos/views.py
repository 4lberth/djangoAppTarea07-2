from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Usuario, RegistroEvento
from .forms import EventoForm, UsuarioForm, RegistroEventoForm
from django.http import HttpResponse

# Vista para listar eventos
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

# Vista para detalle de eventos
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})

# Vista para registrar usuario en evento
def registrar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    usuario = Usuario.objects.first()  # Simplificación, selecciona el primer usuario
    RegistroEvento.objects.create(evento=evento, usuario=usuario)
    return HttpResponse(f'{usuario.nombre} registrado en {evento.titulo}')

# Vista para actualizar un evento
def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', evento_id=evento.id)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/actualizar_evento.html', {'form': form, 'evento': evento})

# Vista para actualizar un registro de evento
def actualizar_registro(request, registro_id):
    registro = get_object_or_404(RegistroEvento, pk=registro_id)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', evento_id=registro.evento.id)
    else:
        form = RegistroEventoForm(instance=registro)
    return render(request, 'eventos/actualizar_registro.html', {'form': form, 'registro': registro})



# Vista para agregar un nuevo evento
def agregar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/agregar_evento.html', {'form': form})

# Vista para agregar un nuevo usuario
def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = UsuarioForm()
    return render(request, 'eventos/agregar_usuario.html', {'form': form})

# Vista para registrar un usuario en un evento
def registrar_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = RegistroEventoForm()
    return render(request, 'eventos/registrar_evento.html', {'form': form})

# Vista para eliminar un evento
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

# Vista para eliminar un registro de evento
def eliminar_registro(request, registro_id):
    registro = get_object_or_404(RegistroEvento, pk=registro_id)
    if request.method == 'POST':
        registro.delete()
        return redirect('detalle_evento', evento_id=registro.evento.id)
    return render(request, 'eventos/eliminar_registro.html', {'registro': registro})
