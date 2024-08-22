from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=300)
    city = models.CharField(max_length=10)
    image = models.ImageField(upload_to='img')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Contact(models.Model):
    number = models.IntegerField(verbose_name='номер')
    adres = models.CharField('адрес',max_length=50)

    def __str__(self):
        return self.adres
