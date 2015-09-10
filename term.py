#!/usr/bin/python3

from random import Random
from collections import Counter

def main():
  r = {'G': 3, 'O': 2, 'A': 5, 'L': 5, 'I': 5}
  w = [
    '01.09-06.09',
    '07.09-13.09',
    '14.09-20.09',
    '21.09-27.09',
    '28.09-04.10',
    '05.10-11.10',
    '12.10-18.10',
    '19.10-25.10',
    '26.10-01.11',
    '02.11-08.10',
    '09.11-15.10',
    '16.11-22.10',
    '23.11-29.10',
    '30.11-06.12',
    '07.12-13.12',
    '14.12-20.12',
    '21.12-27.12',
    #'28.12-27.12',
    '30.12-03.12',
    '04.01-10.01',
    '11.01-17.01',
    '18.01-24.01',
  ]
  rnd = Random('Antananarivo')
  iters = 0
  while True:
    iters += 1
    assign = [rnd.choice(sorted(list(r.keys()))) for i in range(sum(r.values()))]
    if Counter(assign) == r:
      if assign[0] == 'O':
        # print(iters, assign)
        if all(map(lambda x: x[0]!=x[1], zip(assign, assign[1:]))): 
          print(iters, assign)
          break

if __name__ == "__main__":
  main()
