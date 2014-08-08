#!/usr/bin/python
# -*- coding: utf-8 -*-

def problem_10():
  """Solution of 10 problem in Project Euler"""
  a = [2,3,5]
  cur = 5
  summ = sum(a)
  while(cur < 2000000):
    cur += 2
    if(cur % 3 == 0 or cur % 5 == 0):
      continue
    flag = 0
    for k in a[3:]:
      if(cur % k == 0 or cur // k == 0):
        flag += 1
        break
    if (flag == 0):
      a.append(cur)
      summ += cur
  return summ

if __name__ == '__main__':
  print problem_10()
