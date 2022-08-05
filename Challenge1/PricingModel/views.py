from django.shortcuts import render
from PricingModel.models import Retail
import io
import csv
from io import *

# Create your views here.
def homeView(request):

    if request.method=="GET":
       return render(request,'MyApp/Index.html')

    csv_files=request.FILES['file']
    if not csv_files.name.endswith('.csv'):
        #context={"Error":"File is not csv"}
        return render(request,'MyApp/Index.html')

    data_set=csv_files.read().decode('utf-8')
    io_string=io.StringIO(data_set)
    for column in csv.reader(io_string,delimiter=',',quotechar="|"):
        created=Retail.objects.update_or_create(
        Store_ID=column[0],
        SKU=column[1],
        Product_name=column[2],
        Price=column[3],
        Date=column[4]
        )
    return render(request,'MyApp/Index.html')
