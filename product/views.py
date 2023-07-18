from django.shortcuts import render,redirect
from.models import Product,Billing,Footwear,Rating,Shoe,Shirt,Croptop,Tshirt,Aline,Bodycon
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
lis=[]
def home(req):
    global lis
    lis=[]
    user=req.user
    print(lis)
    return render (req,'product/base.html',{'user':user})
    # return render(req,'product/base.html')
def base(req):
    return render(req,'product/base.html')

def croptop(req):
    return render(req,'product/croptop.html')
def tshirt(req):
    return render(req,'product/tshirt.html')
def shirt(req):
    return render(req,'product/shirt.html')
def bodycon(req):
    return render(req,'product/bodycon.html')
def aline(req):
    return render(req,'product/aline.html')



def signuppage(req):
    if req.method=='POST':
        uname=req.POST.get('username')
        email=req.POST.get('email')
        pass1=req.POST.get('password1')
        pass2=req.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect("login")
    return render(req,'product/signup.html')

def logInpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        pass1=req.POST.get('pass')
        
        user=authenticate(req,username=username,password=pass1)
        if user is not None:
            login(req,user)
            return redirect('base')
        else:
            return HttpResponse('your password is incorrect please enter your correct password')
           
    return render(req,'product/login.html')

def LogOutpage(req):
    logout(req)
    return redirect('login')


def allitems(req):
    cat="allitems"
    data=Product.objects.all()
    return render(req,'product/allitems.html',{'data':data,'cat':cat})


def shoe(req):
    cat="Shoe"
    data=Shoe.objects.all()
    return render(req,'product/allitems.html',{'data':data,'cat':cat})

def shirt(req):
    cat="shirt"
    data=Shirt.objects.all()
    return render(req,'product/allitems.html',{'data':data,'cat':cat})

def croptop(req):
    cat="croptop"
    data=Croptop.objects.all()
    return render(req,'product/allitems.html',{'data':data,'cat':cat})



def footwear(req):
    data=Footwear.objects.all()
    cat="footwear"
    return render (req,'product/allitems.html',{'data':data,'cat':cat})

def tshirt(req):
    data=Tshirt.objects.all()
    cat="tshirt"
    return render (req,'product/allitems.html',{'data':data,'cat':cat})

def aline(req):
    data=Aline.objects.all()
    cat="aline"
    return render (req,'product/allitems.html',{'data':data,'cat':cat})

def bodycon(req):
    data=Bodycon.objects.all()
    cat="bodycon"
    return render (req,'product/allitems.html',{'data':data,'cat':cat})

def buy(req,id,price,av,cat):
    global lis
    lis=lis
    print(lis)  #addcard

    if req.method == "POST":
        
        if cat=="footwear":
            data=Footwear.objects.get(pk=id)
        elif cat=="Shoe":
            data=Shoe.objects.get(pk=id)
        elif cat=="shirt":
            data=Shirt.objects.get(pk=id)
        elif cat=="croptop":
            data=Croptop.objects.get(pk=id)
        elif cat=="tshirt":
            data=Tshirt.objects.get(pk=id)
        elif cat=="allitems":
            data=Product.objects.get(pk=id)
        elif cat=="aline":
            data=Aline.objects.get(pk=id)
        elif cat=="bodycon":
            data=Bodycon.objects.get(pk=id)
               
        else:
            data=Product.objects.get(pk=id)

        q = int(req.POST.get('quan'))
        av=int(av)-q
        price=float(price)
        total=q*price
        lis.append({cat:[id,q,total]})
        p1=Product.objects.filter(pk=id).update(available=av)
        return render (req,'product/final.html',{'i':data,'q':q,'total':total,'available':av})
    
def bill(req):
    return render(req,'product/billing.html')  

def bills(req):
    if req.method=="POST":
        cusn=req.POST.get('fname')
        cusa=req.POST.get('address')
        cusp=req.POST.get('pincode')
        cusc=req.POST.get('city')
        cusm=req.POST.get('mobile')
        bills=Billing(fname=cusn,address=cusa,pincode=cusp,city=cusc,mobile=cusm)
        bills.save()

        return render(req,'product/billing.html')  
    
    
def search(req):
    if req.method=="POST":
        searchitem=req.POST.get('searchitem')
        d1=Product.objects.filter(name=searchitem)
        d2=Footwear.objects.filter(name=searchitem)
        d3=Shirt.objects.filter(name=searchitem)
        d4=Tshirt.objects.filter(name=searchitem)
        d5=Croptop.objects.filter(name=searchitem)
        d6=Aline.objects.filter(name=searchitem)
        d7=Bodycon.objects.filter(name=searchitem)

        if d1 or d2 or d3 or d4 or d5 or d6 or d7 :
            return render(req,'product/search.html',{'i1':d1,'j1':d2,"k1":d3,'l1':d4,'m1':d5,'n1':d6,'o1':d7})
        
        else:
            return render(req,'product/search.html',{'msg':'no data available'})

def rating(req):
    data=User.objects.all()
    return render (req,'product/rating.html',{'data':data})

def submitreview(req):
    if req.method=="POST":
        un=req.POST.get('ch')
        cr=req.POST.get('cr')
        crev=req.POST.get('crev')
        cp=req.POST.get('cp')
        id1=User.objects.values().filter(username=un)[0].get('id')
        user=User.objects.get(pk=id1)
        rating_user=Rating(appuser=user,rating=cr,fav=cp,feedback=crev)
        rating_user.save()
        data=User.objects.all()
       # return HttpResponse('Thanks You')
        return render (req,'product/rating.html',{'data':data})

def mycart(req):
    global lis
    lis=lis
    print(lis)
   # [{'footwear':[2,22,1055340.0]}] [{'shoe':[2,22,1055340.0]}]
    lis_complex=[]
    lis_total=[]
    lis_q=[]
    for i in lis:
        for j,k in i.items():
            if j=="footwear":
                data=Footwear.objects.get(pk=k[0])
            elif j=="Shoe":
                data=Shoe.objects.get(pk=k[0])
            elif j=="shirt":
                data=Shirt.objects.get(pk=k[0])
            elif j=="allitems":
                data=Product.objects.get(pk=k[0])
            elif j=="croptop":
                data=Croptop.objects.get(pk=k[0])
            elif j=="tshirt":
                data=Tshirt.objects.get(pk=k[0])
            elif j=="bodycon":
                data=Bodycon.objects.get(pk=k[0])
            elif j=="aline":
                data=Aline.objects.get(pk=k[0])
            
            lis_complex.append(data)

            lis_total.append(k[2])
            lis_q.append(k[1])
    total=sum(lis_total)
    final_lis=[]
    print(lis_complex)
    print(lis_total)
    print(lis_q)
    for i in range(len(lis_q)):
        li=[lis_complex[i],lis_total[i],lis_q[i]]
        final_lis.append(li)
    return render(req,"product/mycart.html",{'data':final_lis,'total':total})