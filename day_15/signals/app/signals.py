from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created")


# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        print("Profile update")

# post_save.connect(update_profile, sender=User)


# Ways of connecting a receiver to a sender
# 1. post_save.connect(create_profile, sender=User)
# 2. Using decorators --> @receiver(post_save, sender=User)
# 3. Separating signals into signals.py
