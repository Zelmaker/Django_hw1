from django.db import models


# Create your models here.
class Ads(models.Model):
    name = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=False)
    description = models.TextField(max_length=2000, blank=True)
    address = models.TextField(max_length=1000)
    is_published = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Cat(models.Model):
    name = models.TextField(max_length=2000)

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
