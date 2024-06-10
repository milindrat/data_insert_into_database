from django.urls import path
from . import views

urlpatterns = [
    path('ba/',views.batchEx_upload_file,name='batchform'),
    path('itm/',views.item_upload_file,name='item'),
    path('log/', views.login_view, name='login'),
    path('ord/',views.ordertoreceive_upload_file,name='orders'),
    path('sale',views.saleshistory_upload_file,name='sales'),
    path('',views.Home_view),
  #  path('dwn/',views.downloads_page,name='down'),

]
