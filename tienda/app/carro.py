from decimal import Decimal
from django.conf import settings
from .models import Producto

class Carro(object): # class to manage shopping cart

    def __init__(self, request):
        """ Initialize the cart with request object """
        self.session = request.session # to make it accessible to the other methods of the Cart class.
        # add products to cart by product id
        carro = self.session.get(settings.CART_SESSION_ID)
        if not carro:
            # save an empty cart in the session
            carro = self.session[settings.CART_SESSION_ID] = {}
        self.carro = carro

    # product to add/update in cart, default cantidad=1
    def add(self, producto, cantidad=1, actualizar_cantidad=False):
        """ Add a product to the cart or update its quantity. """
        producto_id = str(producto.id) # as key in cart contents's dictionary, in str coz django uses json to serialize session data
        if producto_id not in self.carro:
            self.carro[producto_id] = {'cantidad': 0, 'precio': str(producto.precio)} # price in str to serialize it
        if actualizar_cantidad:
            self.carro[producto_id]['cantidad'] = cantidad
        else:
            self.carro[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        # mark the session as 'modified' to make sure it gets saved
        self.session.modified = True

    def remove(self, producto):
        """ Remove a product from the cart """
        producto_id = str(producto.id) # json format takes string only
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()

    # method iterate through the items contained in the cart and access the related Product instances.
    def __iter__(self):
        """ Iterate	over the items in the cart and get the products from the database. """
        producto_ids = self.carro.keys()
        # get the product objects and add them to the cart
        productos = Producto.objects.filter(id__in=producto_ids)

        carro = self.carro.copy()
        for producto in productos:
            carro[str(producto.id)]['producto'] = producto

        for item in carro.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad'] # total price attribute
            yield item

    def __len__(self):
        """ Count all items in the cart """
        return sum(item['cantidad'] for item in self.carro.values())

    def get_total_precio(self):
        """ Total price of items in the cart """
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
