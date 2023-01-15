from account.models import Account

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@receiver(post_save, sender=Account)
def account_created(sender, instance, created, **kwargs):
    if created:
        user = instance

        subject = "Welcome to icscinterns."
        message = "Thank you for registering in icscinterns7!"
        template = render_to_string(
            "email_app/template_registration.html", {"first_name": user.first_name, "subject": subject, "message": message})
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        email = EmailMessage(
            subject,
            template,
            email_from,
            recipient_list
        )
        email.fail_silently = False
        email.content_subtype = 'html'
        email.attach_file
        email.send()
