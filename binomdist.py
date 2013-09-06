#!/usr/bin/python

import sys
import itertools
from scipy.stats import binom

def main():
  total_link_speed = 1000000
  individual_link_speed = 100000
  transmit_percent = 10
  user_count = 35
  user_limit = 10
  print(' n   P(x=n)   P(x<=n)    P(x>n)')
  m = user_count
  p = transmit_percent / 100
  for index, valtriple in enumerate([(binom_dist_eq  (m,k,p),
                                      binom_dist_lteq(m,k,p),
                                      binom_dist_gt  (m,k,p)) for k in range(0, user_limit+1)]):
    print('%02d' % index, '%09.6f %09.6f %09.6f' % valtriple)

def binom_dist_eq(successes, trials, probability):
  return binom.pmf(trials, successes, probability)

def binom_dist_lteq(successes, trials, probability):
  return binom.cdf(trials, successes, probability)

def binom_dist_gt(successes, trials, probability):
  return 1.0-binom_dist_lteq(successes, trials, probability)

if __name__ == '__main__':
  main()
