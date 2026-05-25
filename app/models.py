from django.db import models

class Employee(models.Model):

    fullname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    image = models.URLField()

    def __str__(self):

        return self.fullname