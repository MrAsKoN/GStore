import datetime
import random
import string
from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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
    # get the user profile
    user_profile = get_object_or_404(CustomUser, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    # if product in request.user.profile.ebooks.all():
    #     messages.info(request, 'You already own this ebook')
    #     return redirect(reverse('products:product-list'))
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    context = {
        'title': "Cart",
        'user_order': user_order,
        'grandtotal': user_order.get_cart_total() + 100
    }
    # show confirmation message and redirect back to the same page
    messages.info(request, product.name + 'has been to your Cart!')
    return render(request, 'cart/cart.html', context)


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    deletedproduct=Product.objects.filter(id=item_id)
    if item_to_delete.exists():
        print(item_to_delete[0])
        item_to_delete[0].delete()
        messages.info(request, deletedproduct.name + " has been removed from the Cart!")
    return render(request, 'cart/cart.html')

@login_required()
def get_user_pending_order(request):
    user_profile = get_object_or_404(CustomUser, user=request.user)
    print(user_profile.user.username)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    print(order)
    if order.exists():
        return order[0]
    return 0

@login_required()
def displaycart(request):
    existingorder = get_user_pending_order(request)
    context = {
        'order': existingorder
    }
    print(existingorder.get_cart_items())
    return render(request, 'cart/cart.html', context)
