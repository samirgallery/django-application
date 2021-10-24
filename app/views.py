from django.shortcuts import render

from.models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    #data come from htlml to view 
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    #creating Object of models Class 
    #inserting data into table
    newuser=student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)


    #after insert render show .html
    return render(request,"app/show.html")

    

    
    
