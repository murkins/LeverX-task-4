from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Persona


@receiver(post_save, sender=User)
def create_persona(sender, instance, created, **kwargs):
    if created:
        Persona.objects.create(user=instance)
