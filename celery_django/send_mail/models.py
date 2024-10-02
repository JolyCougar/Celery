from django.db import models


class Contact(models.Model):
    """Модель контакта"""
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
