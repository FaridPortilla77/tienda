from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto  

@receiver(post_save, sender=Producto)
def producto_creado(sender, instance, created, **kwargs):
    if created:
        print(f"Nuevo producto añadido: {instance.nombre}")
    else:
        print(f"Producto actualizado: {instance.nombre}")
