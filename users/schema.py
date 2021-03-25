import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class UpdateUsername(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID()
        username = graphene.String(required=True)

    def mutate(self, info, id, username):
        user = User.objects.get(id=id)
        user.username = username
        user.save()
        return UpdateUsername(user=user)


class UpdateEmail(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID()
        email = graphene.String(required=True)

    def mutate(self, info, id, email):
        user = User.objects.get(id=id)
        user.email = email
        user.save()
        return UpdateEmail(user=user)


class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        user = User.objects.get(id=id)
        user.delete()
        return DeleteUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_username = UpdateUsername.Field()
    update_email = UpdateEmail.Field()
    delete_user = DeleteUser.Field()
