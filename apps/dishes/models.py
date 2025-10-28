from django.db import models


class Dish(models.Model):
    id: models.AutoField
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
