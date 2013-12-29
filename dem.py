#!/usr/bin/python

def num2dem(num):
    """docstring for num2dem"""
    mag = get_magn(num)
    a = [0] * (mag + 1)
    for i in xrange(mag+1):
        a[i] = num // 10**i % 10
    return a

def get_magn(num,magn=0):
    """docstring for get_magn"""
    a = num // 10
    if (a > 0):
        if (a > 9):
            magn = get_magn(a) + 1
        else:
            magn = 1
    return magn

def dem_norm(a):
    """docstring for dem_norm"""
    for i in xrange(len(a)):
        b = num2dem(a[i])
        for j in xrange(1,len(b)):
            if (i+j == len(a)):
                a.append(b[j])
            else:
                a[i+j] += b[j]
        a[i] = b[0]
    return a

def mult_dem1num(a,b):
    """docstring for mult_dem1num"""
    for i in xrange(len(a)):
        a[i] *= b
    dem_norm(a)
    return a

def add_dem1dem(a,b):
    """docstring for add_dem1dem"""
    magn_b = len(b)
    magn_a = len(a)
    for i in xrange(magn_a):
        if (i < magn_b):
            a[i] += b[i]
    for i in xrange(magn_b-magn_a):
        a.append(b[magn_a+i])
    dem_norm(a)
    return a
