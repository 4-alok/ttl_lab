# Write a program to find the number range from 1-50 which are prime using user defined function

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def find_primes():
    for number in range(1, 51):
        if is_prime(number):
            print(number)

find_primes()