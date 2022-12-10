from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        abstract = True


class Poll(BaseModel):
    question = models.TextField(max_length=400, verbose_name="Вопрос")

    def __str__(self):
        return f"{self.id}: {self.question}"

    class Meta:
        db_table = "Polls"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(models.Model):
    option = models.TextField(max_length=100, verbose_name="Вариант")
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, verbose_name="Опрос", related_name="choices")

    def __str__(self):
        return f"{self.id}: {self.option}"

    class Meta:
        db_table = "Choices"
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"