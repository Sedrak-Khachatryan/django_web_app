from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    img = models.FileField(upload_to='images', blank=True, null=True)
    description = models.TextField()
    date = models.DateField()


class Kitchen(models.Model):
    title = models.CharField(max_length=50)
    img = models.FileField(upload_to='images', blank=True)
    description = models.CharField(max_length=100)


class ContactForm(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=100)


class CraftBeer(models.Model):

    class BavarianWeizen(models.Model):
        pass

    class FarmhouseAle(models.Model):
        pass

    class APA(models.Model):
        pass

    class IPA(models.Model):
        pass

    class DIPA(models.Model):
        pass

    class CherryAle(models.Model):
        pass

    class AppleCider(models.Model):
        pass

    class DarkLager(models.Model):
        pass

