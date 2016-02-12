#!/usr/bin/python

from random import Random
from collections import Counter

from math import pi, exp

def metric(assign):
  kv = list(set(assign))
  hv = [[1 if j == k else 0 for j in assign] for k in kv]
  def gauss(v, r = 1.0):
    n = len(v)
    return [sum((v[i] * exp(-(i-j)**2 / (2 * r * r)) for i in range(n))) / (2 * pi * r * r) for j in range(n)]

  gv = [gauss(p) for p in hv]
  def dist(a, b):
    return sum((p * q for p, q in zip(a, b)))
  return sum((dist(p, q) for p in gv for q in gv if p != q))

def main():
  r = {'G': 4, 'A': 2, 'L': 8, 'I': 8}
  w = [
        '#1: 14.02',
        '#2: 21.02',
        '#3: 28.02',
        '#4: 06.03',
        '#5: 13.03',
        '#6: 20.03',
        '#7: 27.03',
        '#8: 03.04',
        '#9: 10.04',
        '#10: 17.04',
        '#11: 24.04',
        '#12: 01.05',
        '#13: 08.05',
        '#14: 15.05',
        '#15: 22.05',
        '#16: 29.05',
        '#17: 05.06',
        '#18: 12.06',
        '#19: 19.06',
        '#20: 26.06',
        '#21: 03.07',
        '#22: 10.07',
  ]
  rnd = Random('FortBoyard')
  iters = 0

  mv, last_it = None, 0
  assign = [k for k, v in r.items() for i in range(v)]

  while True:
    iters += 1
    rnd.shuffle(assign)
    if 'G' not in assign[-4:] and 'A' not in assign[-4:]:
      cv = metric(assign)
      if mv is None or mv < cv:
        if last_it and iters >= 1e6:
          print(iters, cv, assign)
          break
        mv, last_it = cv, iters

if __name__ == "__main__":
  main()
