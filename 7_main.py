#!/usr/bin/python
# -*- coding: utf-8 -*-

def problem_7():
  """Solution of 7 problem in Project Euler"""
  a = [2,3]
  cur = 3
  while(len(a)<10001):
    cur += 2
    flag = 0
    for k in a:
      if(cur % k == 0 or cur // k == 0):
        flag += 1
        break
    if (flag == 0):
      a.append(cur)
  return a[-1]

if __name__ == '__main__':
  print problem_7()
