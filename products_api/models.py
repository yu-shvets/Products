from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default='')
    added = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-added']

    def __str__(self):
        return "{}".format(self.name)

