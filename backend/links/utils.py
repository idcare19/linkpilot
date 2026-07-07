import random
import string
from .models import Link

def generate_short_code():
    length = 6
    short_code = ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    )
    if not Link.objects.filter(short_code=short_code).exists():
        return short_code
    else:
        return generate_short_code()
    
