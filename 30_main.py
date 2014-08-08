#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def main_30(npow):
  sm = 9 ** npow
  for i in xrange(1,15):
    nmax = i - 1
    if ((10**i / i - sm) > 0) :
      print("max number of digits is %d" %nmax)
      break
  sm *= npow
  san = sm // 10 ** nmax
  print("sm = %d" %sm)
  sa = 9
  while sa != san:
    sm = sm - sa**npow + sa**npow
    sa = san
    san = sm // 10 ** nmax
    print("sm = %d" %sm)
    print("sa, san = %d, %d" %(sa,san))

  print("the highest first digit is %d"%san)

  res = np.zeros(0,dtype=np.int)
  a = np.zeros(nmax,dtype=np.int)
  for inum in xrange(2,(sa+1)*10**nmax):
#  for inum in xrange(2,sm+1):
    inums = inum
    for i in xrange(1,nmax+1):
      a[i-1] = (inums % 10 ** i) // 10 ** (i-1)
    keys = 0
    keys = calc_summ_pow(inums, sorted(a),npow,keys)
#    print("%d has key %d" %(inum,keys))
    if (keys > 1): 
      print("%d has key %d" %(inum,keys))
      res = np.append(res,np.int(inum))
  print("Result of sum = %d" %(sum(res)))

def calc_summ_pow(anum,ar,npow,key):
  """docstring for calc_summ_pow"""
#  print("calc %d: number %d" %(np.size(ar),anum))
  s = ar[-1] ** npow
  arsize = np.size(ar)
  ssum = anum - s * arsize
  if (ssum > 0):
    key = 1
    return key
  elif (ssum == 0 and arsize == 1):
    print("we have solution")
    key = 2
    return key
  if (arsize > 1):
    anum -= s
    key = calc_summ_pow(anum,ar[:-1],npow,key)
  elif (arsize == 1):
    if( key ==0) :
      key = 1
  return key

if __name__ == '__main__':
  n = 5
  main_30(n)
