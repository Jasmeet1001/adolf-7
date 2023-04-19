from django.db import models
from register.models import User
from PIL import Image

# Create your models here.
class CommonInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    photo = models.FileField(default='default.jpg', upload_to='profile_pics')
    
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
    def __str__(self):
        return f"Adolf7 Admin: {self.user.first_name} {self.user.last_name}, {self.user.phone_number}"

class Distributer(CommonInfo):
    adolfAdmin = models.ForeignKey(AdolfAdmin, on_delete=models.PROTECT, related_name='distributers')
    location_dist = models.CharField(max_length=255, blank=True)
    company_name_dist = models.CharField(max_length=255, blank=True)
    company_address_dist = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, {self.user.phone_number}, {self.company_name_dist}, {self.company_address_dist}"

class Retailer(CommonInfo):
    distributer = models.ForeignKey(Distributer, on_delete=models.PROTECT, related_name='retailers')
    location_ret = models.CharField(max_length=255, blank=True)
    company_name_ret = models.CharField(max_length=255, blank=True)
    company_address_ret = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, {self.user.phone_number}, {self.company_name_ret}, {self.company_address_ret}"

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

class OrderDist(models.Model):
    distributer = models.ForeignKey(Distributer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.distributer.user.first_name} {self.distributer.user.last_name} {self.product.vehical_type} {self.product.color} {self.product.product_name} {self.quantity}"

class OrderRet(models.Model):
    order_dist = models.ForeignKey(OrderDist, on_delete=models.CASCADE, related_name='retailer_orders')
    retailer = models.ForeignKey(Retailer, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.retailer.user.first_name} {self.retailer.user.last_name} {self.order_dist.product.vehical_type} {self.order_dist.product.color} {self.order_dist.product.product_name} {self.quantity}"

class Cart(models.Model):
    product = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()