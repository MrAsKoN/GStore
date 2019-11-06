import datetime
import random
import string
from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from cart.models import OrderItem, Order
from home.models import Product
from users.models import CustomUser


# Create your views here.

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(CustomUser, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    order_item, status = OrderItem.objects.get_or_create(product=product)
    order_item.quantity = 1
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    if product.stock <= 0:
        messages.info(request, product.name + 'is out of stock!')
    else:

        user_order.items.add(order_item)
        if status:
            # generate a reference code
            user_order.ref_code = generate_order_id()
            user_order.save()
        shippingcost = 100
        if user_order.get_cart_items().count() == 0:
            shippingcost = 0
        context = {
            'title': "Cart",
            'order': user_order,
            'shippingcost': shippingcost,
            'grandtotal': user_order.get_cart_total() + shippingcost
        }
        # show confirmation message and redirect back to the same page
        messages.info(request, product.name + 'has been to your Cart!')
    shippingcost = 100
    if user_order.get_cart_items().count() == 0:
        shippingcost = 0
    context = {
        'title': "Cart",
        'order': user_order,
        'shippingcost': shippingcost,
        'grandtotal': user_order.get_cart_total() + shippingcost
    }
    return render(request, 'cart/cart.html', context)


@login_required()
def delete_from_cart(request, item_id):
    print('111')
    deletedproduct = Product.objects.filter(id=item_id)
    print('Deleted : ', deletedproduct)
    oldorder = get_user_pending_order(request)
    item_to_delete = OrderItem.objects.get(product=deletedproduct[0])
    print(item_to_delete)
    # print(item_id)
    print(item_to_delete)
    if item_to_delete:
        print(item_to_delete)
        item_to_delete.delete()
        # messages.info(request, deletedproduct.name + " has been removed from the Cart!")
    existingorder = get_user_pending_order(request)
    shippingcost = 100
    print(existingorder.get_cart_items())
    if existingorder.get_cart_items().count() == 0:
        shippingcost = 0
    print(
        shippingcost
    )
    context = {
        'order': existingorder,
        'shippingcost': shippingcost,
        'grandtotal': existingorder.get_cart_total() + shippingcost
    }
    return render(request, 'cart/cart.html', context)


@login_required()
def get_user_pending_order(request):
    user_profile = get_object_or_404(CustomUser, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def displaycart(request):
    user_profile = get_object_or_404(CustomUser, user=request.user)
    existingorder = get_user_pending_order(request)
    print(existingorder)
    if existingorder == 0:
        existingorder = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    shippingcost = 100
    if existingorder.get_cart_items().count() == 0:
        shippingcost = 0

    context = {
        'order': existingorder,
        'shippingcost': shippingcost,
        'grandtotal': existingorder.get_cart_total() + shippingcost
    }
    print(existingorder.get_cart_items())
    return render(request, 'cart/cart.html', context)


@login_required()
def increasequantity(request, item_id):
    existingorder = get_user_pending_order(request)
    deletedproduct = Product.objects.filter(id=item_id)
    item_to_delete = OrderItem.objects.get(product=deletedproduct[0])
    item_to_delete.quantity += 1
    if item_to_delete.quantity > deletedproduct[0].stock:
        messages.info(request, deletedproduct[0].name + " Cannot increase quantity !")
    else:
        item_to_delete.save()
    shippingcost = 100
    if existingorder.get_cart_items().count() == 0:
        shippingcost = 0
    context = {
        'order': existingorder,
        'shippingcost': shippingcost,
        'grandtotal': existingorder.get_cart_total() + shippingcost
    }
    return render(request, 'cart/cart.html', context)


@login_required()
def decreasequantity(request, item_id):
    existingorder = get_user_pending_order(request)
    deletedproduct = Product.objects.filter(id=item_id)
    item_to_delete = OrderItem.objects.get(product=deletedproduct[0])
    item_to_delete.quantity -= 1
    if item_to_delete.quantity <= 0:
        messages.info(request, "Quantity cannot be zero or negative")
    else:
        item_to_delete.save()
    shippingcost = 100
    if existingorder.get_cart_items().count() == 0:
        shippingcost = 0
    context = {
        'order': existingorder,
        'shippingcost': shippingcost,
        'grandtotal': existingorder.get_cart_total() + shippingcost
    }
    return render(request, 'cart/cart.html', context)


@login_required()
def checkout(request):
    existingorder = get_user_pending_order(request)
    shippingcost = 100
    if existingorder.get_cart_items().count() == 0:
        shippingcost = 0
        return redirect('displaycart')

    context = {
        'order': existingorder,
        'shippingcost': shippingcost,
        'grandtotal': existingorder.get_cart_total() + shippingcost
    }
    return render(request, 'cart/checkout.html', context)


@login_required()
def success(request):
    existingorder = get_user_pending_order(request)
    if existingorder:
        newstock = {}
        for item in existingorder.get_cart_items():
            updatedstock = item.product.stock - item.quantity
            newstock[item] = updatedstock
            if updatedstock < 0:
                return HttpResponse("<h1>Out of Stock!</h1>")
        for item in existingorder.get_cart_items():
            Product.objects.filter(id=item.product.id).update(stock=newstock[item])
        existingorder.is_ordered = True
        existingorder.date_ordered = datetime.datetime.now()
        existingorder.ref_code = generate_order_id()
        print(existingorder.ref_code)
        existingorder.save()
        Order.objects.filter(owner=get_object_or_404(CustomUser, user=request.user), is_ordered=False).update(
            is_ordered=True, date_ordered=datetime.datetime.now())
        Order.objects.get_or_create(owner=get_object_or_404(CustomUser, user=request.user), is_ordered=False)
        return render(request, 'cart/success.html')
    return HttpResponse("<h1>404 Error Not Found!</h1>")


@login_required()
def orders(request):
    curruser = get_object_or_404(CustomUser, user=request.user)
    allorders = Order.objects.filter(owner=curruser, is_ordered=True)
    context = {
        'allorders': allorders
    }
    print(allorders)
    return render(request, 'cart/previousorders.html', context)


@login_required()
def adminhome(request):
    return render(request, 'users/adminhome.html')
