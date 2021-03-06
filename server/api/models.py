from django.db import models

# Create your models here.

class Status(models.TextChoices):
    ACTIVE = 'Active'
    BLOCKED = 'Blocked'
    DELETED = 'Deleted'

class Role(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'role'

class Customer(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'customer'

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='profile_of')

    class Meta:
        db_table = 'profile'
class Receptor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    customer = models.ForeignKey(Customer,related_name='receptor_of', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'receptor'

class Size(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

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
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'ingredient'

class IngredientHistory(models.Model):
    price = models.FloatField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='price_of')
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None)

    class Meta:
        db_table = 'ingredient_history'

class Ordersheet(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = 'Created'
        PAYED = 'Payed'
        DELIVERED = 'Delivered'
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_of')
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE, related_name='order_to', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.CREATED)

    class Meta:
        db_table: 'ordersheet'

class Pizza(models.Model):
    size = models.ForeignKey(SizeHistory, on_delete=models.CASCADE, related_name='pizza_size_of')
    ordersheet = models.ForeignKey(Ordersheet, on_delete=models.CASCADE, related_name='pizza_order_of')
    ingredients = models.ManyToManyField(IngredientHistory, through='Ration')
    class Meta:
        db_table = 'pizza'

class Ration(models.Model):
    quantity = models.IntegerField()
    ingredient_price = models.ForeignKey(IngredientHistory, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    class Meta:
        db_table: 'ration'