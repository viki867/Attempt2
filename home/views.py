from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
username = ''
email =''
data='hi'

def home(request):
    return render(request,'home.html',{})
def ad(request):
    return render(request,'admin.html',{})
def user(request):
    if request.method=="POST":
        global username
        global email
        email=request.POST['mail']
        z=request.POST['pwd'] 
        return render(request,'use/user.html',{})
    else:
        return render(request,'use/user.html',{})

def userreg(request):

    if request.method=='POST':
        return render(request,'use/userreg.html',{"status":"fail"})
    else:
        return render(request,'use/userreg.html',{})



def withdraw(request):
    if request.method=='POST':
        a=request.POST['accno']
        b=int(request.POST['amt'])   

        return render(request,'use/oguser.html',{'msg':'succesc vc s'})
    else:
        return render(request,'withdraw.html',{})


def deposit(request):
    if request.method=='POST':
        a=request.POST['accno']
        b=int(request.POST['amt'])   
        return render(request,'use/oguser.html',{'msg':'success'})
    else:
        return render(request,'deposit.html',{})
    
def transfer(request):
    return render(request,'use/oguser.html',{})

def detail(request):
    if request.method == "GET":

        return render(request,'udetail.html',{'result':data})

    else:
        return render(request,'udetail.html',{})


def admin(request):

    if request.method=="POST":
        global username
        username=request.POST['un']
        z=request.POST['pwd'] 
        return render(request,'adlogin.html',{"result":"fail"})
    else:
        return render(request,'adlogin.html',{})
def adreg(request):
    if request.method=='POST':
        a=request.POST['adun']
        b=request.POST['admail']
        c=request.POST['pwd']
        d=request.POST['cpwd'] 
        return render(request,"adreg.html",{'status':"success"})
    else:
        print("k")
        return render(request,"adreg.html",{})

def bankdetail(request):
   
    if request.method == "GET":
        return render(request,'bd.html',{'result':'HI'})

    else:
        return render(request,'bd.html',{})

def remove(request):
    if request.method == "POST":
        return render(request,"admin.html",{})
    else:
        return render(request,"remove.html",{})
    

    
def contact(request):
    return render(request,'contact.html',{})
def logout(request):
    return render(request,'home.html',{})


def transfer(request):
    if request.method=="POST":
 
        return render(request,'transfer.html',{'result':404})

    else:
        return render(request,'transfer.html',{})
    

def viewTransaction(request):
    if request.method=="GET":
       
       
        return render(request,'ViewTransactions.html',{'result':'hi'})
        
    else:
        return render(request,'ViewTransactions.html',{})
    

def download(request):
    content="Transaction ID ,From Account NO, To Account NO, Transfer Amount, Date\n"
    response = HttpResponse(content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transaction.csv"'

    return response


