#!/usr/bin/env python
# coding: utf-8
# Kushal Kumar Reddy 
# kreddy#chapman.edu

print("*******------------BEGIN------------******\n********* SOLUTION TO PROBLEM 1 BEGINS ********")

###Assignment 1
# This assignment focuses on calculating probabilities using both combinatorics and/or a python simulation.

### Problem 1

### Assignment 1 Question 1 Solution
import itertools

#list with the colors
all_colors=['b','p','o']
#Initiating an iteration with the combinations that are possible for b + p + o = 72 
#It is similar to assuming that there are 72 glasses and they need to be of the three colors 
#(case is irrelevant as each glass is equally likely)

#itertools has inbuilt combination function that allows replacement and gives all the possible 72 colors from the input 3
color_combinations=itertools.combinations_with_replacement(all_colors, 72)

#combinations of color of interest with condition
occurence=0

#overall combinations counter
overall_comb=0

#looping in our combinations obtained
for given_comb in color_combinations:
    #counting the number of black glasses
    p_count=given_comb.count('b')
    
    #inreasing counter as we have a combination
    overall_comb+=1
    
    #increasing counter as the ball is black
    if p_count>23:
        occurence+=1
        
#printing output
print(f'The black glass appears greater than 23 (at least 24) times in cases, p: {occurence}')
print(f'The total combinations of colors possible for the 72 glasses, N: {overall_comb}')
print(f'Hence the probability, p/N: {occurence/overall_comb}')


print("*******------------BREAK------------******\n********* SOLUTION TO PROBLEM 2 BEGINS ********")
# ## Problem 2

### Assignment 1, Question 2 Solution

import itertools
import random

# initiating the suit and rank lists with the string characters
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = ['H', 'D', 'C', 'S']

# creating the list of cards by multiplying lists
cards_iter=list(itertools.product(suits,ranks))

print ("Your deck of cards is ",cards_iter,'\n')
##removing the four cards that make consecutive cards

#noting down the first four cards
first_four=cards_iter[:4]

#removing the first four cards
cards_iter=cards_iter[4:]

#shuffling the cards list
random.shuffle(cards_iter)

#removing the additional card that is not in either side
for i in range(48):
    if cards_iter[i][1]!='A' and cards_iter[i][1]!='6':
        del cards_iter[i]
        break


#shuffling cards 
random.shuffle(cards_iter)

#printing
print('The first four cards in the straight were: ',first_four,'\n','\nThe following are the draws for 5th card which give a full straight: \n')

count=0
for i in cards_iter:
    if i[1]=='A' or i[1]=='6': 
        count+=1        
        print(f'Count {count} : A straight with 5th card as {i}')

print(f'\nSince there are total {count} possibilities for the one card to make a straight and the total cards left after discarding one card is {len(cards_iter)} the probability is {count/len(cards_iter)}')

print("*******------------THE END------------******")

## Combinatorics
# Out of 52 Cards, 4 are the used cards which are consecutive
# The one discarded card is also removed
# We have 47 Cards
# The either side of the 4 Cards can be filled in by the 4 cards from the four suits
# 4 choose 1 + 4 choose 1 are the possible cases 
# Total cases are 47 choose 1
# The probability is 4+4/47 = 8/47"



