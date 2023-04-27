from decimal import Decimal
from django.conf import settings
from .models import Iha
from django.core import serializers

class Cart(object):
    """docstring for Cart"""


    def __init__(self, request):
        """initalize the cart"""


        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')


    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': int(product.price),'brand':product.brand.name,'model':product.model.name,'category':product.category.name} #ürünü id'ye göre kart'a ekleme

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart #session güncelledik
        self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Iha.objects.filter(id__in=product_ids)



        for item in self.cart.values():
            item['price'] = item['price']
            item['total_price'] = item['price'] * item['quantity'] #fiyat hesaplama işlemleri
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values()) #toplam sepet tutarı


    def clear(self):
        del self.session[settings.CART_SESSION_ID] #session silme
        self.session.modified = True
