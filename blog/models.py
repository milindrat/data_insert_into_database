from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Batch_expiration(models.Model):
    id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=54, null=True)
    batch_code = models.CharField(max_length=108, null=True)
    expiration_date = models.DateTimeField(null=True)
    on_hand = models.IntegerField(null=True)
    customer = models.CharField(max_length=108, null=True)
    dc_name = models.CharField(max_length=256, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    item_name = models.CharField(max_length=256, null=True)

    
    class Meta:
        db_table = 'Batch_expiration'



class Item(models.Model):
    id = models.AutoField(primary_key=True)
    Item_Category_1 = models.CharField(max_length=72, null=True, blank=True)
    Item_Category_2 = models.CharField(max_length=72, null=True, blank=True)
    Item_Category_3 = models.CharField(max_length=72, null=True, blank=True)
    Item_Category_4 = models.CharField(max_length=72, null=True, blank=True)
    Item_Code = models.CharField(max_length=54, null=True, blank=True)
    Description = models.CharField(max_length=512, null=True, blank=True)
    Dc_Name = models.CharField(max_length=72,null=True, blank=True)
    Supplier_Code = models.CharField(max_length=72, null=True, blank=True)
    Supplier_Name = models.CharField(max_length=512, null=True, blank=True)
    Last_On_Hand = models.IntegerField(null=True, blank=True)
    Of_Periods_For_Safety_Stock = models.IntegerField(null=True, blank=True)
    Lead_Time = models.IntegerField(null=True, blank=True)
    Ordering_Days = models.CharField(max_length=24, null=True, blank=True)
    Rounding = models.IntegerField(null=True, blank=True)
    Shelf_Life_Days = models.IntegerField(null=True, blank=True)
    Customer = models.CharField(max_length=108, null=True, blank=True)
    Updated_On = models.DateTimeField(null=True, blank=True)
    Min_Safety_Stock = models.IntegerField(null=True, blank=True)
        

    class Meta:
        db_table = 'item'
        unique_together = ('Item_Category_4','Description','Item_Code','Dc_Name','Supplier_Code')
        
    def save(self, *args, **kwargs):
        if Item.objects.filter(Item_Category_4=self.Item_Category_4, Item_Code=self.Item_Code, Description=self.Description, Dc_Name=self.Dc_Name, Supplier_Code=self.Supplier_Code).exists():
            raise IntegrityError('Duplicate entry detected.')
        super(Item, self).save(*args, **kwargs)

 


class OrdersToReceive(models.Model):
    item_code = models.CharField(max_length=54, null=True, blank=True)
    supplier = models.CharField(max_length=108, null=True, blank=True)
    sendout_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    qty_to_receive = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_number = models.CharField(max_length=54, null=True, blank=True)
    customer = models.CharField(max_length=108, null=True, blank=True)
    dc_name = models.CharField(max_length=256, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    vendor_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'Orders_to_receive'



class SalesHistory(models.Model):
    total = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=64, null=True, blank=True)
    Class = models.CharField(max_length=64, null=True, blank=True)
    variable_name = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    starting_year = models.IntegerField(null=True, blank=True)
    starting_period = models.IntegerField(null=True, blank=True)
    periods_per_year = models.IntegerField(null=True, blank=True)
    periods_per_cycle = models.IntegerField(null=True, blank=True)
    attribute = models.DateTimeField(null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    customer = models.CharField(max_length=64, null=True, blank=True)
    dc_name = models.CharField(max_length=256, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Sales_History_table'

