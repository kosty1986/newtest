from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return f'Category: {self.name}'

class Product(models.Model):
    name = models.CharField(max_length=128, null=False)
    categories = models.ManyToManyField(Category, through= 'ProductCategory')
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Product: {self.name}'


class ProductCategory(models.Model):
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories_pivot')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_pivot')
    extra_column = models.IntegerField(null=True, default=None)

