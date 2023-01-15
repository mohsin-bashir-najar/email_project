# from . models import Account
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=Account)
# def account_created(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         user.username = user.email.split('@')[0].lower()
#         user.save()
