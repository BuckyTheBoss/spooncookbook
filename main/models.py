from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    spoon_id = models.PositiveIntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    title = models.CharField(max_length=200)
    ready_minutes = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    image = models.URLField()
    summary = models.TextField()
    instructions = models.TextField()