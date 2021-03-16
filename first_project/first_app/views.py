from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Id,Name,Data

# Create your views here.
def index(request):
    my_dict={
    'insert_me':'Now THIS FROM the View.pY fiLE!!!'
    }
    return render(request,'index.html',context = my_dict)

def access(request):
    webpages_id = Id.objects.order_by('id_number')
    webpages_name = Name.objects.order_by('id_stud')
    webpages_data = Data.objects.order_by('name')

    my_dict = {
    'ids':webpages_id,
    'names':webpages_name,
    'data':webpages_data
    }

    return render(request,'database.html',context = my_dict)
