import random
def gen_random_key(n):
    """Generates a random key of bits (with 0s or 1s) of length n"""
    key = [0] * (round(n/2)) + [1] * (round(n/2))
    random.shuffle(key)
    return key
