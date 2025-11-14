from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import Profile
from django.db.models.signals import post_migrate


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    if not User.objects.filter(username='nhotun').exists():
        User.objects.create_superuser('nhotun', 'nhotun@example.com', '123456')
        print("✅ Đã tạo user mặc định: nhotun / 123456")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
