#!/usr/bin/python

import sys
from scipy.stats import binom

def main():
  totallinkspeed = 1000000
  individuallinkspeed = 100000
  transmitpercent = 10
  userlimit = 10
  print(' n   P(x=n)   P(x<=n)    P(x>n)')
  for users in range(0,userlimit+1):
    print('%02d %09.6f %09.6f %09.6f' % (users, binomDistEq(transmitpercent / 100, users, userlimit), binomDistLtEq(transmitpercent / 100, users, userlimit), binomDistGt(transmitpercent / 100, users, userlimit)))

def binomDistEq(probability, trials, arg3):
  return trials

def binomDistLtEq(probability, trials, arg3):
  return trials

def binomDistGt(probability, trials, arg3):
  return trials

if __name__ == '__main__':
  main()
