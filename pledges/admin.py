from django.contrib import admin

from .models import Action, Answer, Pledge, Question, Select


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'action',
        'question_number',
        'question_text',
        'question_type',
    )


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Select)
class SelectAdmin(admin.ModelAdmin):
    list_display = ('question', 'response', 'value')


@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'action')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'pledge', 'question', 'response_select', 'response_number')
