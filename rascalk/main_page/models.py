from django.db import models
from django.urls import reverse
# Create your models here.


class Review(models.Model):
    user = models.CharField(max_length=100, verbose_name="Пользователь")  # Поле теперь простое текстовое
    rating = models.PositiveSmallIntegerField("Оценка", choices=((i, i) for i in range(1, 6)))  # Выбор оценки от 1 до 5
    text = models.TextField("Текст отзыва")
    admin_response = models.TextField("Ответ модерации", blank=True, null=True)
    def __str__(self):
        return self.user


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"





class Vote(models.Model):
    option = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.option} by {self.ip_address}"
