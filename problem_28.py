''' taken from the web'''


"""Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| < 1000
Find the product of the coefficients, a and b, 
for the quadratic expression that produces 
the maximum number of primes for 
consecutive values of n, 
starting with n = 0."""

from timeit import default_timer as timer
import math
start = timer()

def longestPrimeQuadratic(alim, blim):

    def isPrime(k): # checks if a number is prime
        if k < 2: return False
        elif k == 2: return True
        elif k % 2 == 0: return False
        else: 
            for x in range(3, int(math.sqrt(k)+1), 2):
                if k % x == 0: return False

        return True 

    longest = [0, 0, 0] # length, a, b
    for a in range((alim * -1) + 1, alim):
        for b in range(2, blim):
            if isPrime(b):
                count = 0
                n = 0
                while isPrime((n**2) + (a*n) + b):
                    count += 1
                    n += 1

                if count > longest[0]:
                    longest = [count, a, b]

    return longest

ans = longestPrimeQuadratic(1000, 1000)

elapsed_time = (timer() - start) * 100 # s --> ms

print("Found %d and %d in %r ms." % (ans[1], ans[2], elapsed_time))
        
        


