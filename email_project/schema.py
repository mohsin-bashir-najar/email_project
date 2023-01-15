import graphene
import account.schema
import email_app.schema


class Query(account.schema.Query, email_app.schema.Query, graphene.ObjectType):
    pass


class Mutation(account.schema.Mutation, email_app.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
