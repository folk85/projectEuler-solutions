#!/usr/bin/python
# -*- coding: utf-8 -*-

# make array of factorial from 0 to 9
def factor(n):
    ni = int(n)
    if ( ni == 0):
      return 1
    else:
      summ = 1
      for i in xrange(1,ni+1):
        summ *= i
      return summ

sl = []
for i in xrange(10):
  sl.append(factor(i))

def sep_nmb(nmb):
  st = str(nmb)
  ne = len(st)
  a = nmb; cl = []
  for i in xrange(ne):
    cl.append(a % 10) 
    a /= 10
  return cl


ar = []
for a in xrange(3,10000000):
  cl = sep_nmb(a)
  summ = 0
  for i in cl:
    summ += sl[i]
  if a == summ :
    print a
    ar.append(a)
  del(cl)
print "Result %d" %sum(ar)

