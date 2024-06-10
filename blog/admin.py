from django.contrib import admin
from .models import Batch_expiration,Item

# Register your models here.


class Batch_expirationAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'batch_code', 'expiration_date', 'on_hand', 'customer', 'dc_name', 'updated_on', 'item_name']


class ItemAdmin(admin.ModelAdmin):
    list_display= ['Item_Category_1','Item_Category_2','Item_Category_3','Item_Category_4','Item_Code','Description','Dc_Name','Supplier_Code','Supplier_Name','Last_On_Hand','Of_Periods_For_Safety_Stock','Lead_Time','Ordering_Days','Rounding','Shelf_Life_Days','Customer','Updated_On','Min_Safety_Stock']


admin.site.register(Batch_expiration, Batch_expirationAdmin)
admin.site.register(Item,ItemAdmin)