import datetime
import carrinho.models as model

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = model.Cart.objects.get(id=cart_id, checked_out=False)
            except model.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = model.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, quantity=1, valor=0.0):
        try:
            item = model.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except model.Item.DoesNotExist:
            item = model.Item()
            item.cart = self.cart
            item.product = product
            item.unit_price = unit_price
            item.valor   =  valor
            item.quantity = int(quantity)
            item.save()
        else:  # ItemAlreadyExists
            item.unit_price = unit_price
            valor.valor = float(valor)
            item.quantity += int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = model.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except model.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product, quantity, unit_price=None, valor=0.0):
        try:
            item = model.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except model.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:  # ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                valor = valor
                item.quantity = int(quantity)
                item.save()

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1 * item.quantity
        return result

    def summary(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.total_price
        return result

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()
