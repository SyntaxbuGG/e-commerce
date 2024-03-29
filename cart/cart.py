from product.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        # If the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product,quantity=1):
        product_id = str(product.id)
        product_qty = int(quantity)

        # logic

        if product_id in self.cart:
            self.cart[product_id] = {'quantities':int(product_qty)}
        else:
            self.cart[product_id] = {'quantities':int(product_qty)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # User ids to lookyp products in database model
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities
