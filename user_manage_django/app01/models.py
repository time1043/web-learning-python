from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()


class Department(models.Model):
    title = models.CharField(max_length=16)

# class Role(models.Model):
#     caption = models.CharField(max_length=16)
