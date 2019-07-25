from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2, default=10.99)

    def __str__(self):
        return self.title
    


