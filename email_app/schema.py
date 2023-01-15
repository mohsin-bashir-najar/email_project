import graphene
from .typees import MessageType

from .resolvers import resolve_inbox, resolve_view_message, resolve_received_messages, resolve_sent_messages, resolve_sent_message_delete, resolve_received_message_delete, resolve_welcome_message

from .mutations import ComposeMessageMutation

from graphql_jwt.decorators import login_required, superuser_required


# import graphql_jwt


class Query(graphene.ObjectType):

    # account query
    welcome_message = graphene.String()

    # message query
    inbox = graphene.List(MessageType)
    view_message = graphene.Field(
        MessageType,
        id=graphene.Int(required=True)
    )
    received_messages = graphene.List(MessageType)
    sent_messages = graphene.List(MessageType)
    sent_message_delete = graphene.Field(
        MessageType, id=graphene.Int(required=True))
    received_message_delete = graphene.Field(
        MessageType, id=graphene.Int(required=True))

    # message resolvers

    @login_required
    def resolve_inbox(self, info, **kwargs):
        return resolve_inbox(self, info, **kwargs)

    @login_required
    def resolve_view_message(self, info, **kwargs):
        return resolve_view_message(self, info, **kwargs)

    @login_required
    def resolve_received_messages(self, info, **kwargs):
        return resolve_received_messages(self, info, **kwargs)

    @login_required
    def resolve_sent_messages(self, info, **kwargs):
        return resolve_sent_messages(self, info, **kwargs)

    @login_required
    def resolve_sent_message_delete(self, info, **kwargs):
        return resolve_sent_message_delete(self, info, **kwargs)

    @login_required
    def resolve_received_message_delete(self, info, **kwargs):
        return resolve_received_message_delete(self, info, **kwargs)

    def resolve_welcome_message(self, info, **kwargs):
        return resolve_welcome_message(self, info, **kwargs)


class Mutation:
    compose_message = ComposeMessageMutation.Field()
