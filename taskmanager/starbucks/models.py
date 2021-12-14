from django.db import models


class Registration(models.Model):
    username = models.CharField('username', max_length=50)
    product = models.CharField('Coffee', max_length=50)

    def __str__(self):
        return self.username
