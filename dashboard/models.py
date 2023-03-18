from django.db import models
from register.models import User
from PIL import Image

# Create your models here.
class CommonInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    photo = models.FileField(default='media/default.jpg', upload_to='profile_pics')
    # user_type = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            resize = (300, 300)
            img.thumbnail(resize)
            img.save(self.photo.path)

    class Meta:
        abstract = True

class AdolfAdmin(CommonInfo):
    company_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Adolf7 Admin: {self.user.first_name} {self.user.last_name}, {self.user.phone_number}"

class Distributer(CommonInfo):
    adolfAdmin = models.ForeignKey(AdolfAdmin, on_delete=models.PROTECT, related_name='distributers')
    location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, {self.user.phone_number}, {self.company_name}, {self.company_address}"

class Retailer(CommonInfo):
    distributer = models.ForeignKey(Distributer, on_delete=models.PROTECT, related_name='retailers')
    location = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    shop_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, {self.user.phone_number}, {self.shop_name}, {self.shop_address}"

class PriceList(models.Model):
    vehical_type = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=100, null=True)
    product_name = models.CharField(max_length=255, null=True)
    product_image = models.ImageField(upload_to='product_images', default='default_product_image.png')
    item_desc = models.CharField(max_length=100, null=True)
    uom = models.CharField(max_length=50, null=True)
    price_bef_gst = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    tax_rate = models.CharField(max_length=20, null=True)
    price_bef_gst_pu = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    price_aft_gst_pu = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    unit_per_nos = models.PositiveIntegerField(null=True)
    price_pernos_incl_gst = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    mrp_incl_gst_pu = models.DecimalField(max_digits=10, decimal_places=4, null=True)

    def __str__(self):
        return f"{self.vehical_type} {self.color} {self.product_name} - {self.mrp_incl_gst_pu}"

# class Restock(models.Model):
#     pass

# class Order(models.Model):
#     distributer = models.ForeignKey(Distributer, on_delete=models.DO_NOTHING)
#     retailer = models.ForeignKey(Retailer, on_delete=models.DO_NOTHING)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.id) #type:ignore

# class OrderItem(models.Model):
#     pass
