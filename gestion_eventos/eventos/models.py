from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class RegistroEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.nombre} registrado en {self.evento.titulo}'
