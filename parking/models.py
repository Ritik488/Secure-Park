from django.db import models
from datetime import date

GENDER_CHOICE ={
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),

}

QUES_CHOICE = {
    ('book','What is your favourite book?'),
    ('food', 'What is your favourite Food?'),
    ('city', 'What city you were born in?'),
    ('place','Which is your favourite place to vacation'),

}

VEHICLE_CHOICE = {
    ('two','Two Wheeler'),
    ('three','Three Wheeler'),
    ('four','Four Wheeler'),
}

class Registration(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    rpassword = models.CharField(max_length=30)
    addressp = models.CharField(max_length=100)
    contactno = models.CharField(max_length=10)
    dob = models.DateField(default=date.today)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='male')
    ques = models.CharField(max_length=50, choices=QUES_CHOICE, default='book')
    answer = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.fname + '-' + self.lname

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contactno =models.CharField(max_length=20)
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20, default=True)
    lname = models.CharField(max_length=20)
    contactno = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    complaint_type = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.fname + '-' + self.lname

class VehicleEntry(models.Model):
    vehicleno=models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_CHOICE, default='two')
    contactno=models.CharField(max_length=10)
    date = models.DateField(default=date.today)
    intime = models.TimeField(null= True, blank= True)
    spacealloted = models.CharField(max_length=10)
    flooralloted = models.CharField(max_length=10)
    tagno = models.CharField(max_length=20)

    def __str__(self):
        return self.vehicleno


class VehicleExit(models.Model):
    vehicleno = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_CHOICE, default='two')
    tagno = models.CharField(max_length=20)
    outtime = models.TimeField(null=True, blank=True)
    fare = models.CharField(max_length=10)

    def __str__(self):
        return self.vehicleno+self.vehicle_type


