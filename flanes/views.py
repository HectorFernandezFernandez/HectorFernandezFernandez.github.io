from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan, Cart, CartItem
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

def index_flans(requests):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(requests, 'index_flan.html', {'flanes':flanes_publicos})

def about_flans(requests):
    return render(requests, 'about_flan.html')

def welcome_flans(requests):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(requests, 'welcome_flan.html', {'flanes':flanes_privados})

def success_flans(requests):
    return render(requests, 'success_flan.html')

def contact_flans(requests):
    if requests.method == 'POST':
        form = ContactFormForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormForm()
    return render(requests, 'contact_flan.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

def flan_detail(requests,flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    return render(requests, 'flan_detail.html', {'flan':flan})

@login_required
def add_to_cart(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, flan=flan)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.cart.user != request.user:
        return redirect('view_cart')
    cart_item.delete()
    
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.flan.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'count': cart_items.count(),
    }
    return render(request, 'cart_flan.html', context)