# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:10:32 2015

@author: bacro
"""

def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

tmp = primes_sieve1(2000000)


