import graphene
from .typees import AccountType
from .models import Account
from graphql_jwt.decorators import login_required


# account mutations
class AccountCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        confirm_password = graphene.String(required=True)

    account = graphene.Field(AccountType)
    message = graphene.String()

    def mutate(self, info, first_name, last_name, email, password, confirm_password):
        email_check = Account.objects.filter(email=email).exists()
        if email_check == True:
            raise Exception('Email already exits.')

        if password != confirm_password:
            raise Exception("Password and confirm password didn't match.")

        account = Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=confirm_password
        )

        return AccountCreateMutation(account=account, message=f"{account.first_name}, you are registered now with icscinterns7.")


class AccountUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        confirm_password = graphene.String()

    account = graphene.Field(AccountType)
    success_message = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        account = Account.objects.get(pk=kwargs.get('id'))
        if kwargs.get("first_name") is not None:
            account.first_name = kwargs.get("first_name")
        if kwargs.get("last_name") is not None:
            account.last_name = kwargs.get("last_name")

        if kwargs.get("email") is not None:
            email_check = Account.objects.filter(
                email=kwargs.get("email")).exists()
            if email_check == True:
                raise Exception('Email already exits.')
            account.email = kwargs.get("email")
        if kwargs.get("password") and kwargs.get("confirm_password"):
            if kwargs.get("password") != kwargs.get("confirm_password"):
                raise Exception("Password and confirm password didn't match.")
            account.password = kwargs.get("confirm_password")
        account.save()
        success_message = f"{user.first_name}, your account details are updated."
        return AccountUpdateMutation(account=account, message=success_message)
