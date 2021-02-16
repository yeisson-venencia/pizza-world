from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_lenght=50)

    class Meta:
        db_table = 'role'