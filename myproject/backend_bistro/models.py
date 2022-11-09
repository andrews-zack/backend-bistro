from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=40, null=False, unique=True)
    desc = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    cuisine_id = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - $" + str(self.price)


class Cuisine(models.Model):
    name = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    label = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.label
