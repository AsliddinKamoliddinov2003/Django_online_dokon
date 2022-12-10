
def generate_order_number(cart):
    from datetime import datetime
    from random import randint
    now = datetime.now()
    return "".join(list(map(str, [now.year, now.month, now.day, cart.id ])) + list(map(str, [randint(0, 9) for _ in range(4)])))


def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip