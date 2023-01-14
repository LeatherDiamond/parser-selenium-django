from django.db import models

# Create your models here.


class ResultView(models.Model):
    product_name = models.CharField(
        max_length=150,
        verbose_name="Product name"
    )
    publisher = models.CharField(
        max_length=150,
        verbose_name="Publisher"
    )
    release_date = models.IntegerField(
        verbose_name="Release date"
    )
    contact_info = models.CharField(
        max_length=150,
        verbose_name="Contact info"
    )

    def __str__(self):
        return self.product_name
