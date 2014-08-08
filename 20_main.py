#!/usr/bin/python
# -*- coding: utf-8 -*-

def num2dem(num,mag=1):
  """docstring for num2dem"""
  # find magnitude of a number
  a = []
  for i in xrange(10):
    num_mag = num // 10**i 
    a.append(num_mag % 10)
    if (num_mag < 10):
      break
  return a

def summ(a,b):
  """docstring for summ"""
  magn = max(len(a),len(b))
  for i in xrange(magn):
    if (i+1 >= len(a)):
      a.append(b[i])
    else:
      if(i+1 < len(b)):
        a[i] += b[i]
    reff = num2dem(a[i])
    s_ref = len(reff)
#    if (len(a)>i+siz)
    a[i:i+len(reff)+1] = reff[:]
  return a

def problem_20():
  """docstring for problem_20"""
  numb = 136
  dem = num2dem(numb)
  print dem
  print summ(dem,dem)
  return

if __name__ == '__main__':
  problem_20()
