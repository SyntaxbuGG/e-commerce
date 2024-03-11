from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404

from .cart import Cart
from product.models import Product
from django.http import JsonResponse, HttpResponse
import json


def cart_index(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()

    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')

        product = get_object_or_404(Product, id=product_id)
        cart.add(product, product_qty)
        data = {'qty': len(cart_products), 'quantities': quantities}

        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        return render(request, 'cart.html', {'cart_products': cart_products, 'quantities': quantities})


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product)

        # get quantity
        cart_quantity = cart.__len__()

        # return response
        # response = JsonResponse({'Product Name': product.title})
        response = JsonResponse({'qty': cart_quantity})
        return response
