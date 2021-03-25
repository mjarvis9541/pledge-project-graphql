import graphene
import pledges.schema
import users.schema


class Query(
    pledges.schema.Query,
    users.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    pledges.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
