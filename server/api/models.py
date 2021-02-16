from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_lenght=50)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        db_table = 'role'

class Customer(models.Model):
    email = models.CharField(max_lenght=100)
    password = models.CharField(max_lenght=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        db_table = 'customer'

class Profile(models.Model):
    first_name = models.CharField(max_lenght=100)
    last_name = models.CharField(max_lenght=100)
    document = models.CharField(max_lenght=50)
    phone = models.CharField(max_lenght=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='profile_of')

    class Meta:
        db_table = 'profile'
class Receptor(models.Model):
    first_name = models.CharField(max_lenght=100)
    last_name = models.CharField(max_lenght=100)
    document = models.CharField(max_lenght=50)
    phone = models.CharField(max_lenght=50)
    address = models.CharField(max_lenght=250)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    customer = models.ForeignKey(Customer,related_name='receptor_of', on_delete=models.CASCADE)

    class Meta:
        db_table = 'receptor'

class Size(models.Model):
    name = models.CharField(max_lenght=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        db_table = 'size'

class Ingredient(models.Model):
    name = models.CharField(max_lenght=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        db_table = 'ingredient'