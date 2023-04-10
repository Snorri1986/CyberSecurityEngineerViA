import random


def gen_random_key(n):
    """Generates a random key of bits (with 0s or 1s) of length n"""
    key = [0] * (round(n / 2)) + [1] * (round(n / 2))
    random.shuffle(key)
    return key


def xoroperationencrypt(source, key):
    """XOR source file and key file"""
    result = bytearray(len(source))
    for i in range(len(source)):
        result[i] = source[i] ^ key[i]

    return result
