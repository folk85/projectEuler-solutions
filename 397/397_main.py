#!/usr/bin/python

# -*- coding: utf-8 -*-

import numpy as np
def val(k,coord):
  """docstring for val"""
  cord = np.empty([3],dtype=int)
#  tan_v = np.empty([3],dtype=int)
  val_num = np.empty([3],dtype=int)
  val_den = np.empty([3],dtype=int)
  cord[:] = coord[:]
  tan_v = [cord[i]+cord[(i+2) % 3] for i in xrange(3)]
  for i in xrange(3):
    j = (i + 1) % 3
    val_num[i] = tan_v[i] - tan_v[j]
    val_den[i] = k * k + tan_v[i]*tan_v[j]
  cond = np.where(k*val_num-val_den == 0)[0]
  if(len(cond)>0) :
#    print cord[:], k*val_num-val_den
    return 1
  else:
    return 0

def solution_397(k,bound):
  """docstring for solution_397"""
  summ = 0
  for ke in xrange(1,k+1):
    for a in xrange(-bound,0):
      for c in xrange(a+2,bound+1):
        for b in xrange(a+1,min(1,c)):
          addit = val(ke,[a,b,c])
          summ += addit + addit
  #        if(a == -c and b == 0):
          if(b == 0):
            summ -= addit
  return summ

if (__name__=="__main__"):
  k = 1000000
  b = 1000000000
  sol = solution_397(k,b)
  print sol
