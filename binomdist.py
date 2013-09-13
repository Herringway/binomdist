#!/usr/bin/python

import sys
import math

def main():
  total_link_speed = 1000000#bits per second, total bandwidth available
  individual_link_speed = 100000#bits per second, bandwidth allocated to each user
  transmit_percent = 10#chance of a user transmitting
  user_count = 35#number of users
  user_limit = 10#limit the number of users, since the values are useless beyond a certain point
  print(' n   P(x=n)    P(x≤n)    P(x>n)')#print column headers
  m = user_count
  p = transmit_percent / 100#convert from percent to decimal
  for index, valtriple in enumerate([(binom_dist_eq  (m,k,p),#calculate probabilities for every n in 0..user_limit
                                      binom_dist_lteq(m,k,p),
                                      binom_dist_gt  (m,k,p)) for k in range(0, user_limit+1)]):
    print('%02d' % index, '%09.7f %09.7f %09.7f' % valtriple)


#handles (n) style statements
#        (k)
def binom_coeff(n, k):
  return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

#calculates value for the P(x=n) column using a probability mass function
def binom_dist_eq(n, k, p):
  return binom_coeff(n,k) * (p ** k) * ((1 - p) ** (n - k))

#calculates value for the P(x<=n) column
def binom_dist_lteq(n, k, p):
  v = 0.0
  for i in range(0, k+1):
    v += binom_dist_eq(n, i, p)
  return v

#calculates value for the P(x>n) column
def binom_dist_gt(n, k, p):
  return 1.0-binom_dist_lteq(n, k, p)

#call main() only if script is executed directly
if __name__ == '__main__':
  main()
