from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=200)
    product_count = models.IntegerField()

    def __str__(self):
        return self.product_id


class Order(models.Model):
    order_id = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id


class Customer(models.Model):
    customer_id = models.CharField(max_lenght=200)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_id
