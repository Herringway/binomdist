#!/usr/bin/python

import sys
import math

def main():
  total_link_speed = 1000000
  individual_link_speed = 100000
  transmit_percent = 10
  user_count = 35
  user_limit = 10
  print(' n   P(x=n)    P(x≤n)    P(x>n)')
  m = user_count
  p = transmit_percent / 100
  for index, valtriple in enumerate([(binom_dist_eq  (m,k,p),
                                      binom_dist_lteq(m,k,p),
                                      binom_dist_gt  (m,k,p)) for k in range(0, user_limit+1)]):
    print('%02d' % index, '%09.7f %09.7f %09.7f' % valtriple)

	
def binom_coeff(n, k):
  return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binom_dist_eq(n, k, p):
  return binom_coeff(n,k) * (p ** k) * ((1 - p) ** (n - k))

def binom_dist_lteq(n, k, p):
  v = 0.0
  for i in range(0, k+1):
    v += binom_dist_eq(n, i, p)
  return v

def binom_dist_gt(n, k, p):
  return 1.0-binom_dist_lteq(n, k, p)

if __name__ == '__main__':
  main()
