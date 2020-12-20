from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=128)
    phone = models.CharField(verbose_name='Номер телефона', max_length=16)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=128)
    position = models.CharField(verbose_name='Должность', max_length=128)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Request(models.Model):

    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    text = models.TextField(verbose_name='Текст запроса')
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Заявка №{self.pk}'
