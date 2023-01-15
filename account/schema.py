import graphene
from .typees import AccountType

from .resolvers import resolve_all_accounts, resolve_account, resolve_delete_account, resolve_welcome

from .mutations import AccountCreateMutation, AccountUpdateMutation

from graphql_jwt.decorators import login_required, superuser_required


import graphql_jwt


class Query(graphene.ObjectType):

    # account query
    welcome = graphene.String()
    all_accounts = graphene.List(AccountType)
    account = graphene.Field(
        AccountType,
        id=graphene.Int(required=True),
        first_name=graphene.String()
    )

    delete_account = graphene.String()

    # account resolvers

    @login_required
    def resolve_all_accounts(self, info, **kwargs):
        return resolve_all_accounts(self, info, **kwargs)

    @login_required
    def resolve_account(self, info, **kwargs):
        return resolve_account(self, info, **kwargs)

    @login_required
    def resolve_delete_account(self, info, **kwargs):
        return resolve_delete_account(self, info, **kwargs)

    def resolve_welcome(self, info, **kwargs):
        return resolve_welcome(self, info, **kwargs)


class Mutation:
    login = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()

    register = AccountCreateMutation.Field()
    update_account = AccountUpdateMutation.Field()
