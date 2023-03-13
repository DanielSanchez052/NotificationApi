import random
import string


def generate_random_string(length: int):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length))
