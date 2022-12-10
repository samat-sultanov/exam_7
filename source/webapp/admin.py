from django.contrib import admin

from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_display_links = ['id', 'question']
    search_fields = ['question']
    exclude = []
    readonly_fields = ["created_at"]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'option', 'poll']
    list_display_links = ['id', 'option']
    search_fields = ['option']
    exclude = []


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'option']
    list_display_links = ['id', 'poll', 'option']
    exclude = []


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
