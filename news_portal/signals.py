from django.db.models.signals import m2m_changed,post_init, pre_init, pre_save, post_save, post_delete
import django.db.models.signals as signals
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.conf import settings
from .models import Post, PostCategory

@receiver(signal=m2m_changed, sender=PostCategory)
def notify_pre_create (sender, instance,**kwargs):
      if kwargs['action'] == 'post_add':
            print(f'PostCategory changed')
