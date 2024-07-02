from django.urls import path
from . import views

urlpatterns = [
    path('ba/',views.batchEx_upload_file,name='batchform'),
    path('itm/',views.item_upload_file,name='item'),
    path('log/', views.login_view, name='login'),
    path('ord/',views.ordertoreceive_upload_file,name='orders'),
    path('sale',views.saleshistory_upload_file,name='sales'),
    path('',views.Home_view),
    path('download-batch-ex/', views.download_batchEx_excel, name='download_batchEx_excel'),
    path('download-item/', views.download_item_excel, name='download_item_excel'),
    path('download-order-to-receive/',views.download_orderstoreceive_excel, name='download_orderstoreceive_excel'),
    path('download-sales-history/', views.download_saleshistory_excel, name='download_saleshistory_excel'),
  

]
