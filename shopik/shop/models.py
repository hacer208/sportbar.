from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False)
    slug = models.CharField(max_length=20, blank=False,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.CharField(max_length=20, blank=False)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    src = models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Basket(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return str(self.product) +" "+ str(self.count)