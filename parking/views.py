from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Registration, Contact, Complaint
from .models import VehicleEntry, VehicleExit
import math, random
from datetime import datetime,date,time
from datetime import *
from django.http import HttpResponse

f=0

def park1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Registration()
        if username == 'admin' and password == 'admin123':
            return render(request, 'adminpage.html')

        if Registration.objects.filter(username=username, password=password).all():
            user = Registration.objects.filter(username=username, password=password).all()
            n=on()
            context= {
                'f':n,
            }
            return render(request, 'entryexit.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/park1/')
    else:
        return render(request, 'park1.html')


def on():
    global f
    f = 1
    return f

def check():
    global f
    return f



def entryexit(request):
    return render(request, 'entryexit.html')


def signup(request):
    if request.method == 'POST':
        print(request)
        fname=request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        rpassword = request.POST.get('rpassword', '')
        addressp = request.POST.get('addressp', '')
        contactno = request.POST.get('contactno', '')
        dob = request.POST.get('dob', '')
        gender =request.POST.get('gender', 'male')
        ques = request.POST.get('ques', '')
        answer = request.POST.get('answer', '')
        if password == rpassword:
            signup = Registration(fname=fname, lname=lname, email=email, username=username, password=password,
                                  rpassword=rpassword, addressp=addressp, contactno=contactno, dob=dob, gender=gender,
                                  ques=ques, answer=answer)
            signup.save()
            messages.success(request, 'User is Registered Successfully')
        else:
            messages.success(request, 'Password doesnt matches')
            return redirect('/signup/')
    return render(request, 'signup.html')


def forgot(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        ques = request.POST.get('ques', '')
        answer = request.POST.get('answer', '')
        user= Registration()
        if Registration.objects.filter(username=username, ques=ques, answer=answer).all():
            user = Registration.objects.filter(username=username, ques=ques, answer=answer).all()
            return render(request, 'entryexit.html')
        else:
            messages.info(request, 'Invalid Username')
            return redirect('/')
    else:
        return render(request, 'forgot.html')


stringspace = "123456"
stringfloor = "123"
stringtag = "29876543"

lentspace = len(stringspace)
spaceallot1 = " "
spaceallot2 = " "
for i in range(1):
   spaceallot1 +=stringspace[math.floor(random.random()*lentspace)]
for i in range(2):
   spaceallot2 +=stringspace[math.floor(random.random()*lentspace)]
space= spaceallot1 + spaceallot2

lentfloor = len(stringfloor)
floorallot = " "
for i in range(1):
   floorallot +=stringfloor[math.floor(random.random()*lentfloor)]

lenttag = len(stringtag)
tagallot = " "
for i in range(2):
   tagallot +=stringtag[math.floor(random.random()*lenttag)]
tag = space + floorallot + tagallot

todaydate = date.today()
dt = datetime.now()
t1 = dt.strftime("%H:%M:%S")

def entry(request):
    n = 0
    z = check()
    if z == 1:
        n = 1
    context = {
        'n': n,
    }
    if request.method == 'POST':
        vehicleno = request.POST.get('vehicleno', '')
        vehicle_type = request.POST.get('vehicle_type', '')
        contactno = request.POST.get('contactno', '')
        date = todaydate
        intime =t1
        spacealloted = space
        flooralloted = floorallot
        tagno = 'f' + tag
        entry= VehicleEntry(vehicleno=vehicleno, vehicle_type=vehicle_type,contactno=contactno,
                            date=date, intime=intime,spacealloted=spacealloted,flooralloted=flooralloted,
                            tagno=tagno)
        entry.save()
    return render(request, 'entry.html',context)


def aboutus(request):
    return render(request, 'aboutus.html')

def complaint(request):
    if request.method == 'POST':
        print(request)
        fname=request.POST.get('fname', '')
        mname = request.POST.get('mname', '')
        lname = request.POST.get('lname', '')
        contactno = request.POST.get('contactno', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        complaint_type= request.POST.get('complaint_type', '')
        message = request.POST.get('message', '')
        complaint = Complaint(fname=fname, mname=mname, lname=lname, contactno=contactno, email=email,
                              address=address, complaint_type=complaint_type, message=message)
        complaint.save()
    return render(request, 'complaint.html')


def fare(request):
    return render(request, 'fare.html')

def maps(request):
    return render(request, 'maps.html')

t2=dt.strftime('%H:%M:%S')

def exit(request):
    n = 0
    z = check()
    if z == 1:
        n = 1
    context = {
        'n': n,
    }
    if request.method == 'POST':
        vehicleno = request.POST.get('vehicleno', '')
        vehicle_type = request.POST.get('vehicle_type', '')
        tagno = request.POST.get('tagno','')
        outtime = t2
        fare= 0
        FMT = '%H:%M:%S'
        tdiff = datetime.strptime(t2, FMT)-datetime.strptime(t1, FMT)
        user = VehicleEntry()
        tc1 = timedelta(hours=6, minutes=00)
        tc2 = timedelta(hours=12, minutes=00)
        user = VehicleEntry.objects.filter(vehicleno=vehicleno, vehicle_type=vehicle_type, tagno=tagno).all()
        if len(user)>0:
            if vehicle_type == 'two':
                if tdiff <= tc1:
                    fare = 15
                elif tdiff <= tc2:
                    fare = 25
                elif tdiff > tc2:
                    fare = 30
            elif vehicle_type == 'three':
                if tdiff <= tc1:
                    fare = 20
                elif tdiff <= tc2:
                    fare = 35
                elif tdiff > tc2:
                    fare = 40
            elif vehicle_type == 'four':
                if tdiff <= tc1:
                    fare = 30
                elif tdiff <= tc2:
                    fare = 50
                elif tdiff > tc2:
                    fare = 60
            else:
                fare = 0
            exit = VehicleExit(vehicleno=vehicleno, vehicle_type=vehicle_type, outtime=outtime, fare=fare, tagno=tagno)
            exit.save()
            return HttpResponse('<h2>Vehicle found in the parking lot.</h2><br><span style="font-size:25px" class="psw"> Print <a href="/exitdetails/" style="color:blue" style="font-size:30px">Recipt</a></span>')
        else:
            return HttpResponse('<h2>Vehicle not found in parking lot</h2>')
    else:
        return render(request, 'exit.html',context)

def contactus(request):
    if request.method == 'POST':
        print(request)
        name=request.POST.get('name', '')
        email = request.POST.get('email', '')
        contactno = request.POST.get('contactno', '')
        question = request.POST.get('question', '')
        contactus = Contact(name=name, email=email, contactno=contactno, question=question)
        contactus.save()
    return render(request, 'contactus.html')

def details(request):
    obj = VehicleEntry.objects.filter().last()
    return render(request, 'details.html', {'obj':obj})


def exitdetails(request):
    obj = VehicleExit.objects.filter().last()
    return render(request, 'exitdetails.html', {'obj': obj})

def homepage(request):
    return render(request, 'homepage.html')

def adminpage(request):
    params = {'name': 'parking', 'place': 'mars'}
    return render(request,'adminpage.html', params)

def printcontact(request):
    obj = Contact.objects.filter().all()
    return render(request, 'printcontact.html', {'obj':obj})

def printcomplaint(request):
    # obj = Registration.objects.last()
    obj = Complaint.objects.filter().all()
    return render(request, 'printcomplaint.html', {'obj':obj})

def printvehicles(request):
    obj = VehicleEntry.objects.filter().all()
    return render(request, 'printvehicles.html', {'obj': obj})