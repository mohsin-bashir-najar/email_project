from .models import Account


# account resolvers

def resolve_all_accounts(self, info, **kwargs):
    return Account.objects.all()


def resolve_account(self, info, **kwargs):
    id = kwargs.get('id')
    first_name = kwargs.get('first_name')
    if id is not None:
        return Account.objects.get(pk=id)
    if first_name is not None:
        return Account.objects.get(first_name=first_name)
    return None


def resolve_delete_account(self, info, **kwargs):
    user = info.context.user
    message = f"{user.first_name}, your account is deleted successfully."
    user.delete()
    return message


# message resolvers

def resolve_inbox(self, info, **kwargs):
    user = info.context.user
    return user.messages.all()


def resolve_received_messages(self, info, **kwargs):
    user = info.context.user
    return user.messages.all()


def resolve_sent_messages(self, info, **kwargs):
    user = info.context.user
    return user.message_set.all()


def resolve_view_message(self, info, **kwargs):
    user = info.context.user
    return user.messages.get(pk=kwargs.get("id"))


def resolve_sent_message_delete(self, info, **kwargs):
    user = info.context.user
    deleting_message = user.message_set.get(pk=kwargs.get("id"))
    deleting_message.delete()
    return None


def resolve_received_message_delete(self, info, **kwargs):
    user = info.context.user
    deleting_message = user.messages.get(pk=kwargs.get("id"))
    deleting_message.delete()
    return None


def resolve_welcome(self, info, **kwargs):
    if info.context.user.is_authenticated:
        return "Welcome to graphql world."
    return None
