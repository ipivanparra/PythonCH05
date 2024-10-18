def is_prime():
    import random
    n = random.randint(0,90)

    if n > 1:
        if n % 2 == 0:
            print("False")
        else: 
            print("True")
    else: 
        print("Iuput a value greater than 1")


def print_primes():
    import random
    test = random.randint(0,80)

    for n in range(test): 
        if n > 1:
            if  n % 2 == 0:
                continue
            else: 
                print(n, end=" ")


def get_primes(): 
    import random
    test = random.randint(0,80)

    for n in range(test): 
        if n > 1:
            if  n % 2 == 0:
                continue
            else: 
                return test
   