from django.db import models

class User(models.Model):
    sname = models.CharField(max_length=200)
    sid = models.IntegerField(max_length=9)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=10)
    #admin.site.register(User)