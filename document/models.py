from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to='media/')

    def __str__(self) -> str:
        return self.name