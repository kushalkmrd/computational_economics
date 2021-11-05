# -*- coding: utf-8 -*-
#Assignment 2 
#Ascending Clock Auction

#Kushal Kumar Reddy
#kreddy@cxhapman.edu

import random 

#Setting up Parameters
iterations=10000
buyers=5
incre_clock=1
start_cost=20

def ascend_clock(buyers,incre_clock,start_cost=20,iterations=100000):
  #Iterate over the iterations
  buyer_range=range(21,100)
  revenues=[]
  for i in range(iterations):
    buyer_values=[random.choice(buyer_range) for x in range(buyers)] #Assign random buyer values
    ticker=1 # set a ticker to stop the function later
    current_cost=start_cost #setting initial cost
    value_max=max(buyer_values) #checking maximum value
    costs=[]

    #The clock ticks while the ticker is non-zero  
    while ticker>0:
      if value_max<=current_cost: #if the maximum value is less than current cost, the loop stops
        ticker=0      

      current_cost+=incre_clock #increment in cost
      costs.append(current_cost)

    revenues.append(costs[-2]) # revenues in each period are the last before periods cost

  return revenues


#A 
revenues=ascend_clock(5,1)
print(f"In case A the revenue is {sum(revenues)/len(revenues)}")

#B 
revenues=ascend_clock(5,10)
print(f"In case B the revenue is {sum(revenues)/len(revenues)}")
# The value increases here as the increment of 10 to this value of ~90 would mean no one will bid 

#C
revenues=ascend_clock(20,1)
print(f"In case C the revenue is {sum(revenues)/len(revenues)}")
#We are drawing a random sample of values of the buyers and here 20 buyers gives more to draw from which adds more higher values and hence a higher revenue