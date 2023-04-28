from django.shortcuts import redirect, render
from django.views import View
from .models import Customer,Product,Order,OrderItem,CustomerInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

class Store(View):
	def get(self,request):
		products = Product.objects.all()
		return render(request, 'store.html', {'produits':products})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('store')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


class Cart(View):
	def get(self,request):
		if request.user.is_authenticated:
			customer = request.user.customer 
			order, created = Order.objects.get_or_create(customer=customer, closed=False)
			items = order.orderitem_set.all()
		else:
			items=[]
			order={'get_cart_total:0','get_cart_items:0'}
		return render(request, 'cart.html', {'items':items , 'order':order})

class Checkout(View):
	def get(self,request):
		if request.user.is_authenticated:
			customer = request.user.customer 
			order, created = Order.objects.get_or_create(customer=customer, closed=False)
			items = order.orderitem_set.all()
		else:
			items=[]
			order={'get_cart_total:0','get_cart_items:0'}
		return render(request, 'checkout.html', {'items':items , 'order':order})
