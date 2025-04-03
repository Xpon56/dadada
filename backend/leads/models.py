from django.db import models

class Lead(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    service = models.CharField('Услуга', max_length=100)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.service}'