from graphene_django.types import DjangoObjectType
from .models import Account


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = '__all__'
