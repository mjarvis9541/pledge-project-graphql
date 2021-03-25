from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


class Action(models.Model):
    """ Model to store actions such as Veg Out, Clean Bills, etc. """

    title = models.CharField(max_length=225)
    version = models.FloatField()  # version number of action for formulas
    # question_text = models.CharField(max_length=225)
    # CO2 formula
    # Water formula
    # Waste formula

    def __str__(self):
        return self.title


class Question(models.Model):
    """ Questions related to the specific action. """

    class QuestionType(models.IntegerChoices):
        NUMBER = 1, _('Numeric Response')
        SELECT = 2, _('Multiple Choice Response')

    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='questions')
    question_number = models.CharField(max_length=10)
    question_type = models.IntegerField(choices=QuestionType.choices)
    question_text = models.CharField(max_length=225)

    def __str__(self):
        return f'Type: {self.get_question_type_display()}, Q: {self.question_text}'


class Select(models.Model):
    """ Responses for multiple choice-type questions. """

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='select_answers')
    response = models.CharField(max_length=225)
    value = models.FloatField()

    def __str__(self):
        return f'{self.response}'


class Pledge(models.Model):
    """
    Model to save the user's pledge, start date, end date, and the
    metrics such as co2, water and waste savings during the pledge.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pledges')
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='pledges')
    date = models.DateTimeField(default=timezone.now)
    # CO2 savings
    # Water savings
    # Waste savings

    def __str__(self):
        return f'{self.user}, {self.action}'


class Answer(models.Model):
    """ Model to store user answers to their pledge-action questions. """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    response_select = models.ForeignKey(Select, on_delete=models.CASCADE, null=True, blank=True)
    response_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.response_select} or {self.response_number}'
