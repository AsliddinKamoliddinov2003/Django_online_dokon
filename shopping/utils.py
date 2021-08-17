from .models import Cart,CartItem


def get_cart(request):
    session_id = request.session.session_key
    if not session_id:
        session_id = request.session.create()

    cart = Cart.objects.filter(session_id=session_id)
    if cart.exists():
        cart = cart.first()
    else:
        cart = Cart(session_id=session_id).save()

    return cart


def get_cartitems_count(request):
    cart = get_cart(request)
    
    amount=0
    if cart:
        cartitems = CartItem.objects.filter(cart=cart)
        for cartitem in cartitems:
            amount += cartitem.quantity

    return  amount



