from pyexpat.errors import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import woods, benifits, OrderConfirm
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt


RAZOR_KEY_ID = "rzp_test_HPR933L2nTKRBP"
RAZOR_KEY_SECRET = "9Qf2Gau5DKgdmjZ6k7GJyAlj"
rezerpay_clint = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


# Create your views here.
def index(request):
    wood = woods.objects.all()
    ben = benifits.objects.all()
    return render(request, "app1/index1.html", context={
        "wood": wood,
        "ben": ben,
    })


def orderRequest(request):
    if request.method == "POST":
        if request.POST["quantity"] is None:
            return HttpResponse("please select quantity")
        idofproduct = request.POST["idofproduct"]
        quantity = request.POST["quantity"]
        price = request.POST["price"]
        names = request.POST["names"]
        total = (int(price) * int(quantity))
        clien_s=rezerpay_clint.order.create({"amount":((int(price)*100)*int(quantity)), "currency":"INR","payment_capture":1})
        c_id=clien_s["id"]
    
        return render(request, "app1/index2.html", context={
            "cod": idofproduct,
            "quantity": quantity,
            "price": price,
            "name": names,
            "total": total,
            "client_id":c_id,
            "api_key":RAZOR_KEY_ID,
            "amount":((int(price)*100)*int(quantity)),
        })
    return render(request, "app1/index2.html")


def confirmOrder(request):
    if request.method == "POST":
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        pin = request.POST["pin"]
        phone = request.POST["phone"]
        totalc = request.POST["totalc"]
        mode = request.POST["mode"]
        product = request.POST["product"]
        product_id = request.POST["product_id"]
        total_amount = request.POST["total"]
        quantiy = request.POST["quantity"]
        savedata = OrderConfirm.objects.create(email=email,
                                               address=address,
                                               city=city,
                                               pin=pin,
                                               phone=phone,
                                               totalc=totalc,
                                               mode=mode,
                                               product=product,
                                               product_id=product_id,
                                               total_amount=total_amount,
                                               quantiy=quantiy
                                               )                                       
        savedata.save()
        if mode == "Online":
            clien_s=rezerpay_clint.order.create({"amount":(int(total_amount)*100), "currency":"INR","payment_capture":1})
            c_id=clien_s["id"]
            return render(request,"app1/online.html",context={
            "price": totalc,
            "total": totalc,
            "client_id":c_id,
            "api_key":RAZOR_KEY_ID,
            "amount":(int(total_amount)*100),
            })
        else:
            return render(request,"app1/payDone.html")
    return redirect("index")


def loginPage(request):
    if request.method == "POST":
        user=authenticate(username=request.POST["email"],password=request.POST["password"])
        if user is not None:
            login(request,user=user)
            return redirect("index")
    return render(request,"app1/loginpage.html")




def signupPage(request):
    if request.method == "POST":
        # usern=request.Post["firstname"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        if password == confirm_password:
            user=User.objects.create_user(username=email,email=email,password=password)
            user.save()
            return redirect("log")
        else:
            return HttpResponse("password Not match")
    return render(request,"app1/signuppage.html")


def profile(request):
    order=OrderConfirm.objects.all().filter(email=request.user.email)
    if request.method == "POST":
        if "LOgout" in request.POST:
            logout(request)
            return redirect("index")
        if "cancels" in request.POST:
            idofProduct=request.POST["idofproduct"]
            OrderConfirm.objects.get(id=idofProduct).delete()
            return redirect("profile")
        if "return_home" in request.POST:
            return redirect("index")

    return render(request,"app1/profile.html",context={
        "order":order,
    })


@csrf_exempt
def payment_complete(request):
    if request.method == "POST":
        if request.POST.get("razorpay_payment_id") is not None:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = rezerpay_clint.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                return render(request,"app1/payDone.html")
            else:
                print("failed")
    return HttpResponse("It's a payment page")

def payd(request):
    if request.method == "POST":
         if "conti" in request.POST:
            return redirect("index")
    return render(request,"app1/payDone.html")