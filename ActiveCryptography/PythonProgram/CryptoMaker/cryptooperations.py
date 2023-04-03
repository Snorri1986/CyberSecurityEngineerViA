def gen_random_key(n):
    """Generates a random key of bits (with 0s or 1s) of length n"""
    A = 1
    B = 0
    size = n
    key = []
    for x in size :
       if(x%2 == 0) : key.append(A)
       else : key.append(B)
    #TODO: loop does not work
