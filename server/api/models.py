from django.db import models

# Create your models here.

class Status(models.TextChoices):
    ACTIVE = 'Active'
    BLOCKED = 'Blocked'
    DELETED = 'Deleted'

class Role(models.Model):
    name = models.CharField(max_lenght=50)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.CharField(max_lenght=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'role'

class Customer(models.Model):
    email = models.CharField(max_lenght=100, unique=True)
    password = models.CharField(max_lenght=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.CharField(max_lenght=10, choices=Status.choices, default=Status.ACTIVE)

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
    status = models.CharField(max_lenght=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'receptor'

class Size(models.Model):
    name = models.CharField(max_lenght=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.CharField(max_lenght=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'size'

class SizeHistory(models.Model):
    price = models.FloatField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='price_of')
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None)

    class Meta:
        db_table = 'size_history'


class Ingredient(models.Model):
    name = models.CharField(max_lenght=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.CharField(max_lenght=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'ingredient'

class IngredientHistory(models.Model):
    price = models.FloatField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='price_of')
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None)

    class Meta:
        db_table = 'ingredient_history'

class Order(models.Model):
    class OrderStatus():
        CREATED = 'Created'
        PAYED = 'Payed'
        DELIVERED = 'Delivered'
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_of')
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE, related_name='order_to', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_lenght=10, choices=OrderStatus.choices, default=OrderStatus.CREATED)

    class Meta:
        db_table: 'order'