import graphene
from account.models import Account
from .typees import MessageType
from .models import Message
# from graphql_jwt.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


class ComposeMessageMutation(graphene.Mutation):
    class Arguments:
        recipient = graphene.String(required=True)
        subject = graphene.String(required=True)
        body = graphene.String(required=True)

    compose = graphene.Field(MessageType)
    success_message = graphene.String()

    # @login_required
    def mutate(self, info, **kwargs):
        try:
            recipient = Account.objects.get(email=kwargs.get("recipient"))
        except:
            raise Exception("Respective email does not exist in the database.")

        sender = info.context.user
        template = render_to_string(
            "email_app/template_message.html", {"first_name": recipient.first_name, "subject": kwargs.get("subject"), "message": kwargs.get("body")})
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient.email]
        if recipient.email == sender.email:
            raise Exception("Sender and recipient must not be same.")
        email = EmailMessage(
            kwargs.get("subject"),
            template,
            email_from,
            recipient_list
        )
        email.fail_silently = False
        email.content_subtype = 'html'
        try:
            email.send()
        except Exception as e:
            raise Exception(e)

        compose = Message.objects.create(
            sender=sender,
            recipient=recipient,
            subject=kwargs.get("subject"),
            body=kwargs.get("body")
        )
        success_message = f"{sender.first_name} message sent to {recipient.first_name} successfully."

        return ComposeMessageMutation(compose=compose, success_message=success_message)
