#!/usr/bin/python
# -*- coding: utf-8 -*-

sl = [2]
for i in xrange(3,100000):
  key = 0
  for j in sl:
    if( i % j == 0):
      key = 1
      break
  if key == 0 :
    sl.append(i)


def check(nmb,sl,ne):
    n = 0
    nmb1 = nmb
    for i in sl:
        if nmb1 < i :
            break
        if nmb1 % i == 0:
            nmb1 /= i
            n += 1
            if n == ne:
                break
    if (n == ne):
        return 1
    return 0

elem = 0

for i in xrange(100,10000000):
  rt = check(i,sl,4)
  if (rt == 1):
    if (elem > 2):
      break
    elem += 1
  else:
    elem = 0
print (i - elem) 
