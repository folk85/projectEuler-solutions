#!/usr/bin/python

# -*- coding: utf-8 -*-

def solution_2(maximum):
  """Solution Problem 2 in Project Euler"""
  val = [1,1,0]
  summ = 0
  while (val[2] < maximum):
    print val[:]
    val[2] = val[1] + val[0]
    if(val[2] % 2 == 0):
      summ += val[2]
    val[0] = val[1]
    val[1] = val[2]
  return summ

if (__name__ == '__main__'):
  num = 4000000
  summ = solution_2(num)
  print summ
