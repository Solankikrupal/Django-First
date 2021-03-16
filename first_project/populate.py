import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
#this for the pathh because it outside of all app and first_project

import django
django.setup()
#this will set all settings which made upper two line for paths

import random
from first_app.models import Id,Name,Data
from faker import Faker

fake = Faker()

def ids(n):

    id_list = []
    for i in range(n):
        x = '16CP' + str(i)
        id_list.append(x)


    return id_list

def pop(n = 5):

    college_year = ['1st year','2nd year','3rd year','4th year']


    x = ids(n)

    for entry in range(n):


        fake_name = fake.name()
        fake_year = random.choice(college_year)
        fake_date = fake.date()

        idx = Id.objects.get_or_create(id_number = x[entry] )[0]

        namepg = Name.objects.get_or_create(id_stud = idx,name = fake_name,year = fake_year)[0]

        datapg = Data.objects.get_or_create(name = namepg ,birth_date = fake_date)






if __name__ == '__main__':
    print("Populating")
    pop(50)
    print("completed")
