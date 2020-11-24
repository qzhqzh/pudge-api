from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_migrate
from django.dispatch import receiver

@receiver(post_migrate, sender=None)
def create_super_user(**kwargs):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(username='admin', email='admin@admin.com',
                                      password='admin123')
