from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default='')
    added = models.DateField()
    updated = models.DateField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-added']

    def __str__(self):
        return "{}".format(self.name)

