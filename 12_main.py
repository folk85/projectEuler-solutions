#!/usr/bin/python
# -*- coding: utf-8 -*-
def problem_12():
  """Solution of 12 problem in Project Euler"""
  cur = 1
  val = 1
  maxx = 2
  while (maxx < 500 ):
    cur += 1
    val += cur
    maxx = 4
    max1 = 2
    max2 = 2
    for i in xrange(3,(cur+1)//2+1):
      if (cur % i == 0):
        max1 += 1
        continue
      if ((cur+1) % i == 0):
        max2 += 1
    if (cur % 4 != 0 and (cur+1) % 4 != 0):
      if (cur % 2 == 0):
        max1 -= 1
      else :
        max2 -= 1
    maxx = max1 * max2
    print cur, cur*(cur+1)/2, val, maxx
  val = cur * (cur + 1) / 2
  return val

if __name__ == '__main__':
  print problem_12()
