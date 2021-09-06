from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
