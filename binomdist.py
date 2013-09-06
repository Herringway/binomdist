#!/usr/bin/python

import sys
from scipy.stats import binom

def main():
  totallinkspeed = 1000000
  individuallinkspeed = 100000
  transmitpercent = 10
  usercount = 35
  userlimit = 10
  print(' n   P(x=n)   P(x<=n)    P(x>n)')
  for users in range(0,userlimit+1):
    print('%02d %09.6f %09.6f %09.6f' % (users, binomDistEq(transmitpercent / 100, users, usercount), binomDistLtEq(transmitpercent / 100, users, usercount), binomDistGt(transmitpercent / 100, users, usercount)))

def binomDistEq(probability, trials, arg3):
  return binom.pmf(trials, arg3, probability)

def binomDistLtEq(probability, trials, arg3):
  return binom.cdf(trials, arg3, probability)

def binomDistGt(probability, trials, arg3):
  return 1.0-binomDistLtEq(probability, trials, arg3)

if __name__ == '__main__':
  main()
