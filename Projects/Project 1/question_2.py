# Computational Economics, Chapman University Fall 2021
# Instructor: Dr. Ryan French
##Project 1 , Question 2
# Author: Kushal Kumar Reddy
# kreddy@chapman.edu

# Vegas Hotel Problem

import numpy as np

#hotel_sequence=[0,1, 1, 2, 2, 2, 3, 3, 3, 3]
def hotel_profit(T):
  hotel_sequence=[0]
  for i in np.arange(T):
    delta=random.choice( [0,1])
    hotel_sequence.append(hotel_sequence[i]+delta)

  profit=0
  for i in np.arange(len(hotel_sequence)):
    t=i+1
    n=hotel_sequence[i]
    profit+= ((750+50*t)/(n+1))
  return profit
iterations=100000
profit=[]
T=10
for _ in range(iterations):
  profit.append(hotel_profit(T))

print( "The Expected Profit for given parameters is ",sum(profit)/len(profit))
