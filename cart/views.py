from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from shop.models import Product  # Replace 'myapp' with the name of your app

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_item = CartItem.objects.get(cart__user=request.user, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1  # Decrease quantity if quantity > 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove item from cart if quantity is 1
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Process the checkout, e.g., payment, order creation, etc.
        cart.delete()  # Clear the cart after checkout
        return redirect('home')

    return render(request, 'cart/checkout.html', {'cart': cart})