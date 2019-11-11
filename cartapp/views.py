from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from productapp.models import Stock, Product, Cart
from django.contrib.auth.models import User



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
	x = request.GET["pid"]
	qt= request.GET["qt"]
	print('getting pid ')
	user= User.objects.get(id=request.session.get("_auth_user_id"))
	un= str(user.username)
	pr=Product.objects.get(pid=int(x))
	print('hope for the best')
	a= int(str(x))
	b= int(str(qt))
	c= un
	d= float(pr.pcost)
	e= int(str(qt)) * float(pr.pcost)
	ct= Cart(username=c, pid=a, units=b, unitprice=d, tuprice=e)
	ct.save()
	print('insert cart sucessfull2')
	return render(request, 'cartapp/insertcart.html')


def viewcart(request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    y=Cart.objects.filter(username=un)
    return render(request,'cartapp/viewcart.html',{'x': y})

def delete(request):
	# return HttpResponse('delete item')
    cs=Cart.objects.filter(id=int(request.GET["id"]))
    cs.delete()
    return render(request,'cartapp/viewcart.html',{'x': display(request)})

def display (request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    ct = Cart.objects.filter(username=un)
    # tp = 0.0
    # ctid=0
    # for p in ct:
    #     tp = tp + float(p.tuprice)
    #     ctid=p.id
    # dic= {"k": ct, "tp":tp, 'ctid':ctid}
    return ct

def modifycart(request):
    x= int(request.GET['pid'])
    qt= Stock.objects.filter(prodid=x)
    qtt = 0
    for p in qt:
        qtt = p
    qt = [q for q in range(1, qtt.tot_qty + 1)]
    oldqt = request.GET['oqt']
    cid = request.GET['id']
    return render(request,'cartapp/modifyqty.html',{"cartid":cid,"pid":x,"qtt":qt,"oq":oldqt})

def modifiedcart(request):
    cid= int(request.GET["cid"])
    nqt= int(request.GET["nqt"])
    oldqty=int(request.GET["oldqty"])
    obj= Cart.objects.get(id=cid)
    # stc = Stock.objects.get(prodid=int(cid))
    # stc.tot_qty= int(stc.tot_qty)+int(oldqty)
    # stc.tot_qty=int(stc.tot_qty) - int(nqt)
    # stc.save()
    obj.units = nqt
    obj.save()
    up = obj.unitprice
    obj.tuprice=up * nqt
    obj.save()
    return render(request,'cartapp/viewcart.html',{'x': display(request)})