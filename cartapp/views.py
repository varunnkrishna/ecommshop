from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from productapp.models import Stock


# Create your views here.
# @login_required
def cartapp(request):
	x=request.GET["pid"]
	qt=Stock.objects.filter(prodid=x)
	qtt=0
	for p in qt:
		qtt=p
#global qtt
	qt=[q for q in range(1,qtt.tot_qty+1)]
	return render(request,'cartapp/cart.html',{"pid":x,"qtt":qt})

def insertcart(request):
	x = request.GET("pid")
	qt= request.GET("qt")
	user= User.objects.GET(id=request.session.get("_auth_user_id"))
	un= str(user.username)
	pr=Product.objects.get(pid=int(x))
	a= int(str(x))
	b= int(str(qt))
	c= un
	d= float(pr.pcost)
	e= int(str(qt)) * float(pr.pcost)
	ct= Cart(username=c, pid=a, units=b, unitprice=d, tuprice=e)
	ct.save()
	return render(request, 'insertcart.html')