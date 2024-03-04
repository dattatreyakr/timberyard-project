from django.db import models


# Create your models here.
class woods(models.Model):
    itemAdded = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(upload_to="woodImage/", blank=False)
    name = models.TextField(blank=False, max_length=10000)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.name)


class benifits(models.Model):
    fkey = models.ForeignKey(woods, on_delete=models.CASCADE)
    benift = models.TextField(max_length=5000)

    def __str__(self):
        return str(self.fkey)


class OrderConfirm(models.Model):
    email = models.EmailField(blank=False)
    address = models.TextField(max_length=3000, blank=False)
    city = models.TextField(max_length=3000, blank=False)
    pin = models.IntegerField(max_length=3000, blank=False)
    phone = models.IntegerField(max_length=3000, blank=False)
    totalc = models.IntegerField(max_length=3000, blank=False)
    mode = models.TextField(max_length=3000, blank=False)
    date = models.DateTimeField(auto_now=True, blank=True)
    product=models.TextField(blank=False,max_length=200)
    product_id=models.TextField(blank=False,max_length=200)
    total_amount=models.IntegerField(blank=False)
    quantiy=models.IntegerField(blank=False)

    def __str__(self):
        return str(self.email)

