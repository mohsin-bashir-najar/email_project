from graphene_django.types import DjangoObjectType
from .models import Message


class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = '__all__'
