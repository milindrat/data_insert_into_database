from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.conf import settings
from django.http import FileResponse,Http404,HttpResponse
import os

from .forms import *
from .models import *
import pandas as pd

import logging
from tempfile import NamedTemporaryFile
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm




# Create your views here.
@login_required
def Home_view(request):
    template_name = 'blog/base.html'
    form=BatchExpirationUploadFileForm()
    context = {'form':form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == 'POST':
        #form = AuthenticationForm(request, data=request.POST)

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:8000/base/")  # Redirect to a success page.
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})
#@login_required
def batchEx_handle_uploaded_file(f):
    try:
        df = pd.read_excel(f, engine='openpyxl')
    except FileNotFoundError:
        logging.error("File not found")
        raise
   
    for index, row in df.iterrows():
        try:
            Batch_expiration.objects.create(
                item_code=row['item_code'],
                batch_code=row['batch_code'],
                expiration_date=row['expiration_date'],
                on_hand=row['on_hand'],
                customer=row['customer'],
                dc_name=row['dc_name'],
                updated_on=row['updated_on'],
                item_name=row['item_name'],
            )
        except Exception as e:
            logging.error(f"Error inserting row {index}: {e}")
            raise

def batchEx_upload_file(request):
    if request.method == 'POST':
        fm = BatchExpirationUploadFileForm(request.POST, request.FILES)
        if fm.is_valid():
            try:
                batchEx_handle_uploaded_file(request.FILES['file'])
                messages.success(request, 'File successfully uploaded and data inserted into the database.')
            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
        else:
            messages.error(request, "Invalid form submission")
    else:
        fm = BatchExpirationUploadFileForm()
    return render(request, 'blog/batch_form.html', {'form': fm})

def download_batchEx_excel(request):
    file_path = r'D:\OneDrive - Radhakrishna Foodland Pvt Ltd\Python_Project\File To Upload Tool\BatchExpiration.xlsx'
    return serve_file(request, file_path, 'BatchExpiration.xlsx')
    

def add_item(row):
    try:
        Item.objects.create(
            Item_Category_1=row['Item_Category_1'],
            Item_Category_2=row['Item_Category_2'],
            Item_Category_3=row['Item_Category_3'],
            Item_Category_4=row['Item_Category_4'],
            Item_Code=row['Item_Code'],
            Description=row['Description'],
            Dc_Name=row['Dc_Name'],
            Supplier_Code=row['Supplier_Code'],
            Supplier_Name=row['Supplier_Name'],
            Last_On_Hand=row['Last_On_Hand'],
            Of_Periods_For_Safety_Stock=row['Of_Periods_For_Safety_Stock'],
            Lead_Time=row['Lead_Time'],
            Ordering_Days=row['Ordering_Days'],
            Rounding=row['Rounding'],
            Shelf_Life_Days=row['Shelf_Life_Days'],
            Customer=row['Customer'],
            Updated_On=row['Updated_On'],
            Min_Safety_Stock=row['Min_Safety_Stock']
        )
    except IntegrityError:
        logging.info(f"Duplicate entry found for Item_Code: {row['Item_Code']}. Skipping the entry.")
    except Exception as e:
        logging.error(f"Error inserting row: {e}")
        raise

def item_handle_uploaded_file(f):
    try:
        df = pd.read_excel(f, engine='openpyxl')
    except FileNotFoundError:
        logging.error("File not found")
        raise
    
    for index, row in df.iterrows():
        try:
            add_item(row)
        except Exception as e:
            logging.error(f"Error processing row {index}: {e}")
            raise

def item_upload_file(request):
    if request.method == 'POST':
        fm = ItemUploadFileForm(request.POST, request.FILES)
        if fm.is_valid():
            try:
                item_handle_uploaded_file(request.FILES['file'])
                messages.success(request, 'File successfully uploaded and data inserted into the database.')
            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
        else:
            messages.error(request, "Invalid form submission")
    else:
        fm = ItemUploadFileForm()
    return render(request, 'blog/item_form.html', {'form': fm})

def download_item_excel(request):
    file_path = r'D:\OneDrive - Radhakrishna Foodland Pvt Ltd\Python_Project\File To Upload Tool\Item.xlsx'
    return serve_file(request, file_path, 'Item.xlsx')
    

def ordertoreceive_handle_uploaded_file(f):
    try:
        df = pd.read_excel(f, engine='openpyxl')
    except FileNotFoundError:
        logging.error("File not found")
        raise
   

    for index, row in df.iterrows():
        try:
            OrdersToReceive.objects.create(
                item_code=row['item_code'],
                supplier=row['supplier'],
                sendout_date=row['sendout_date'],
                delivery_date=row['delivery_date'],
                qty_to_receive=row['qty_to_receive'],
                order_number=row['order_number'],
                customer=row['customer'],
                dc_name=row['dc_name'],
                updated_on=row['updated_on'],
                vendor_name=row['vendor_name'],
            )
        except Exception as e:
            logging.error(f"Error inserting row {index}: {e}")
            raise

def ordertoreceive_upload_file(request):
    if request.method == 'POST':
        fm = OrdersToReceiveUploadFileForm(request.POST, request.FILES)
        if fm.is_valid():
            try:
                ordertoreceive_handle_uploaded_file(request.FILES['file'])
                messages.success(request, 'File successfully uploaded and data inserted into the database.')
            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
        else:
            messages.error(request, "Invalid form submission")
    else:
        fm = OrdersToReceiveUploadFileForm()
    return render(request, 'blog/orderstoreceive_form.html', {'form': fm})


def download_orderstoreceive_excel(request):
    file_path = r'D:\OneDrive - Radhakrishna Foodland Pvt Ltd\Python_Project\File To Upload Tool\OrderToReceive.xlsx'
    return serve_file(request, file_path, 'OrderToReceive.xlsx')

def saleshistory_handle_uploaded_file(f):
    try:
        df = pd.read_excel(f, engine='openpyxl')
    except FileNotFoundError:
        logging.error("File not found")
        raise

    for index, row in df.iterrows():
        try:
            SalesHistory.objects.create(
                total=row['total'],
                category=row['category'],
                Class=row['Class'],
                variable_name=row['variable_name'],
                description=row['description'],
                starting_year=row['starting_year'],
                starting_period=row['starting_period'],
                periods_per_year=row['periods_per_year'],
                periods_per_cycle=row['periods_per_cycle'],
                attribute=row['attribute'],
                value=row['value'],
                customer=row['customer'],
                dc_name=row['dc_name'],
                updated_on=row['updated_on'],
            )
        except Exception as e:
            logging.error(f"Error inserting row {index}: {e}")
            raise


def saleshistory_upload_file(request):
    if request.method == 'POST':
        fm = SalesHistoryUploadFileForm(request.POST, request.FILES)
        if fm.is_valid():
            try:
                saleshistory_handle_uploaded_file(request.FILES['file'])
                messages.success(request, 'File successfully uploaded and data inserted into the database.')
            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
        else:
            messages.error(request, "Invalid form submission")
    else:
        fm = SalesHistoryUploadFileForm()
    return render(request, 'blog/saleshistory_form.html', {'form': fm})


def download_saleshistory_excel(request):
    file_path = r'D:\OneDrive - Radhakrishna Foodland Pvt Ltd\Python_Project\File To Upload Tool\SalesHistory.xlsx'
    return serve_file(request, file_path, 'SalesHistory.xlsx')
    

# Each download_file function will call serve_file with the appropriate file path and filename.
def serve_file(request, file_path, filename):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        return HttpResponse(status=404)


'''
def downloads_page(request):
    return render(request, 'blog/download.html')



filename= 'BatchExpiration.xlsx'

# def download_file(request, filename):
#    file_path = os.path.join(settings.MEDIA_ROOT, 'media/BatchExpiration.xlsx', filename)
#    print(file_path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'inline; filename="{filename}"'+ os.path.basename(file_path)
        return response
    else:
        # Handle the case where the file does not exist
        raise Http404("File not found")
   # return response(request,'blog/download.html')


def download_BtchExfile(request):
    return download_file(request, 'BatchExpiration.xlsx')
'''
















