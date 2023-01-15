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


def resolve_welcome_message(self, info, **kwargs):
    if info.context.user.is_authenticated:
        return "Welcome to graphql world."
    return None
