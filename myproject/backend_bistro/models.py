from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MenuItem(models.Model):
    title = models.CharField(max_length=40, null=False, unique=True)
    desc = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    spicy = models.PositiveIntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(5)])
    cuisine_id = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - $" + str(self.price)


class Cuisine(models.Model):
    title = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.title
