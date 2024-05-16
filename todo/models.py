from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    nick = models.CharField(max_length=10, verbose_name='Ник')
    text = models.TextField(max_length=999, verbose_name='Запись')
    mail = models.EmailField(max_length=100, verbose_name='Почта')
    date = models.TimeField(default=True, verbose_name='Дата')

    def str(self):
        return f"Оставил {self.name},время {self.date}"

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
