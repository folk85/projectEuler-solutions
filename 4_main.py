#!/usr/bin/python
# -*- coding: utf-8 -*-
def problem_4():
  """Solution for problem 4 in Project Euler"""
  maxx = 1
  for a in xrange(999,900,-1):
    for b in xrange(999,900,-1):
        c = a * b
        if((c // 100000) % 10 == c % 10 and  (c // 10000) % 10 == (c // 10) %10 and (c // 1000) % 10 == (c // 100) % 10):
          if (c > maxx): maxx = c
  return maxx

if __name__ == '__main__':
  print problem_4()
