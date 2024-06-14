from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='products_category')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand=models.TextField(default = '')
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=True, blank=True)
    condition=models.CharField(max_length=50, default = 'New')
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class TV(Product):
    screen_size = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    # Add other TV-specific fields

class AudioSystem(Product):
    type=models.CharField(max_length=50)
    


class Laptop(Product):
    kind=models.CharField(max_length=50)

class Computer(Product):
    kind=models.CharField(max_length=50)

class Gadjet(Product):
    kind=models.CharField(max_length=50)

class Refrigerator(Product):
    kind=models.CharField(max_length=50)

class Washing_machine(Product):
    kind=models.CharField(max_length=50) 

class Blender(Product):
    kind=models.CharField(max_length=50) 

class Airfryer(Product):
    kind=models.CharField(max_length=50) 

class Coffee_maker(Product):
    kind=models.CharField(max_length=50)     


