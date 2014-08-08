#!/usr/bin/python

# -*- coding: utf-8 -*-

summ = 0
def solution_1(val):
  """Solution Problem 1 in Project Euler"""
  summ = 0
  for i in xrange(1,val):
    if(i % 3 == 0 or i % 5 == 0):
      summ += i
  return summ

if (__name__ == '__main__'):
  num = 1000
  summ = solution_1(num)
  print summ
