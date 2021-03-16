from django.db import models

# Create your models here.
class Id(models.Model):
    id_number = models.CharField(max_length = 264)

    def __str__(self):
        return self.id_number

class Name(models.Model):
    id_stud = models.ForeignKey(Id,on_delete = models.CASCADE)
    name = models.CharField(max_length = 264)
    year = models.CharField(max_length = 264)

    def __str__(self):
        return self.name

class Data(models.Model):
    name = models.ForeignKey(Name , on_delete = models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return str(self.birth_date)
