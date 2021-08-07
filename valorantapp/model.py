from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title} / {self.author}'


class Weapons(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return f'{self.title} / {self.text}'


class Characters(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return f'{self.title} / {self.text}'

class Skill(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    agent = models.ForeignKey(Characters, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'