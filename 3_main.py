#!/usr/bin/python
# -*- coding: utf-8 -*-

def problem_3():
  """Solution of 3 problem in Project Euler"""
  a = [2,3]
  cur = 3
  lprime = 1
  val = 600851475143
  val12 = val // 2 + 1
  while(cur < val12):
    cur += 2
    flag = 0
    for k in a:
      if(cur % k == 0 or cur // k == 0):
        flag += 1
        break
    if (flag == 0):
      a.append(cur)
      if (val % cur == 0):
        lprime = cur
        print lprime
        val /= cur
        val12 = val #//2 + 1
  return lprime

if __name__ == '__main__':
  print problem_3()
