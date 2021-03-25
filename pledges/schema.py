import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from .models import Action, Answer, Pledge, Question, Select

User = get_user_model()


class ActionType(DjangoObjectType):
    class Meta:
        model = Action


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class SelectType(DjangoObjectType):
    class Meta:
        model = Select


class PledgeType(DjangoObjectType):
    class Meta:
        model = Pledge


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer


class Query(graphene.ObjectType):
    actions = graphene.List(ActionType)
    selects = graphene.List(SelectType)
    questions = graphene.List(QuestionType)
    pledges = graphene.List(PledgeType)
    answers = graphene.List(AnswerType)

    def resolve_actions(self, info, **kwargs):
        return Action.objects.all()

    def resolve_questions(self, info, action_id):
        return Question.objects.filter(question=action_id)

    def resolve_selects(self, info, question_id):
        return Select.objects.filter(question_id)

    def resolve_pledges(self, info, action_id):
        return Pledge.objects.filter(pledge=action_id)

    def resolve_answers(self, info, question_id):
        return Answer.objects.filter(question=question_id)


""" Mutations """


class CreateAction(graphene.Mutation):
    action = graphene.Field(ActionType)

    class Arguments:
        title = graphene.String()
        version = graphene.Float()

    def mutate(self, info, title, version):
        action = Action(title=title, version=version)
        action.save()
        return CreateAction(action=action)


class UpdateAction(graphene.Mutation):
    action = graphene.Field(ActionType)

    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        version = graphene.Float()

    def mutate(self, info, id, title, version):
        action = Action.objects.get(id=id)
        action.title = title if title is not None else action.title
        action.version = version if version is not None else action.version
        action.save()
        return UpdateAction(action=action)


class DeleteAction(graphene.Mutation):
    action = graphene.Field(ActionType)

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        action = Action.objects.get(id=id)
        action.delete()
        return DeleteAction(action=action)


class Mutation(graphene.ObjectType):
    create_action = CreateAction.Field()
    update_action = UpdateAction.Field()
    delete_action = DeleteAction.Field()
