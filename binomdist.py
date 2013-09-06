#!/usr/bin/python

import sys
import itertools
from scipy.stats import binom

def main():
  totallinkspeed = 1000000
  individuallinkspeed = 100000
  transmitpercent = 10
  usercount = 35
  userlimit = 10
  print(' n   P(x=n)   P(x<=n)    P(x>n)')
  m = usercount
  p = transmitpercent / 100
  for k,valtriple in enumerate([(binom_dist_eq  (m,k,p),
                                 binom_dist_lteq(m,k,p),
                                 binom_dist_gt  (m,k,p)) for k in range(0, userlimit+1)]):
    print('%02d' % k, '%09.6f %09.6f %09.6f' % valtriple)

def binom_dist_eq(successes, trials, probability):
  return binom.pmf(trials, successes, probability)

def binom_dist_lteq(successes, trials, probability):
  return binom.cdf(trials, successes, probability)

def binom_dist_gt(successes, trials, probability):
  return 1.0-binom_dist_lteq(successes, trials, probability)

if __name__ == '__main__':
  main()
