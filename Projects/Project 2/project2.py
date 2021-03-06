# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/kushalkrd/computational_economics/blob/main/Projects/Project2.ipynb

# Project 2

Project is to write a genetic algorithm that solves the optimal investment pattern in the health care experiment. Below are the details of the experiment and the parameters from the class

### General Aspects
- There will be 10 periods. Players begin with 70 health.
- Each period, the player harvests some amount of money (this amount is detailed below)
- After harvesting, the player's health degenerates (this amount is detailed below)
- After health degeneration, the player must spend money on Health Investments and Life Investments. Money spent on Health Investments increases health, while money spent on Life Investments gives the player Life Enjoyment. Any money not spent carries over into the next period.
- A player dies if their health ever goes below 0. If a player dies, they receive 0 Life Enjoyment for the remaining periods.
- The goal is to maximize total Life Enjoyment across all periods.
 

### Functions
 

#### Harvesting:
1. The player earns income by harvesting black dots in a region designated by M x N cells. In our parameters (M = N = 100)
2. The player can select any set of contiguous W columns to harvest. In our parameters (W = 10)
3. When fully healthy, there are T black dots dispersed across M x W cells each period. Each black dot is worth v. In our parameters T = 100 and v = 1
4. The number of rows that can be harvested each period are given by: 
$$ HarvestRows(H) = M  (1 - \gamma \frac{100 - H}{100})$$
 where (𝛾=1)

5. The number of rows are reduced by disabling the rows in the upper and lower regions of the selected columns.
6. With these parameters, if health is 50 at the start of the period, the player has only 500 cells in which they can harvest black dots. With 80 health, they have 800 cells.
 

#### Degeneration:
Each period, the player loses (10 + CurrentPeriod) in health. i.e. 11 health the first period, 12 the second period, up to 20 in the last period.


#### Health Regeneration:
The equation for the amount of health regained given a certain Health Investment, I, and health after harvesting, H, is given by: 

$$ \textrm{HealthRegained}(I,H)=100 \left(\frac{e^{k*I}}{e^{k*I} + \frac{100 - H}{H}}\right) - H $$


where (k = 0.01021).  Health cannot exceed 100, and is always rounded down to the nearest integer.

#### Life Enjoyment:
The equation for the amount of Life Enjoyment given a certain Life Investment, L, is given by: 

$$ \text{LifeEnjoyment}(L,\text{CurrentHealth})=c\left(\frac{\text{CurrentHealth}}{100}\right) \left(\frac{L}{L + \alpha}\right) $$

where (c = 464.53) and (𝛼=32)
(
α
=
32
)
.

CurrentHealth is the health the player has during the investment phase **INCLUDING** the amount regained this period through investments in health.

 

The first part of your grade will be based upon how well you can optimize this parameter set. On the due date, I will give a new set of parameters. You will have 1 hour to find the optimal investment pattern for this new set. Your algorithm's performance on this parameter set will determine the rest of your grade.

 

We can change any of the following:

- Harvesting grid size, selection width, dot density, and dot value.
- Regeneration parameters
- Life Enjoyment parameters
- Number of Periods
- Degeneration per period

*Pretty much anything.*

# Solution

## Class Parameters
"""

class Params_healthcare:
  periods = 10
  init_health = 70
  M = 100
  N = 100
  T = 100
  W = 10
  degen = 10 
  health_max = 100 
  health_min = 0
  v = 1
  gamma = 1 
  k = 0.01021
  alpha = 32
  c = 464.53

class Params_ga:
  iterations = 100
  size_population = 100
  ratio_children = 0.05
  chance_mutate = 0.02

class Agent:
    """An Agent Class representing Each Agent"""
    def __init__(self, share_I, share_L, share_money, health, enjoyment, money):
        self.share_I = share_I
        self.share_L = share_L
        self.share_money = share_money
        self.health = health
        self.enjoyment = enjoyment
        self.money = money

"""## Functions """

import numpy as np 
params_healthcare = Params_healthcare
params_ga = Params_ga

def harvest(params_healthcare,health):
  return params_healthcare.T * params_healthcare.v *(1 - (params_healthcare.gamma * ((100 - health) / 100)))

def val_regenerate(params_healthcare,I,health):
  ki_exp=np.exp(params_healthcare.k*I)
  value= np.floor(params_healthcare.health_max * ( ki_exp/(ki_exp+((params_healthcare.health_max-health)/health))) - health)
  if value < 0:
    value = 0 
  print(value)
  return value if value <params_healthcare.health_max else params_healthcare.health_max

def val_degenerate(params_healthcare,period):
  return params_healthcare.degen+period

def life_enjoyment(params_healthcare,L,health):
        return (L / (L + params_healthcare.alpha)) * params_healthcare.c * health / 100

def update_values(self):
    for i in range(len(health)-1):
        curr_period = i + 1
        self.health[curr_period] = self.health[i] - degenerate(curr_period) + regenerate(I_prop * self.money[i], self.health[i])
        self.enjoyment = self.enjoyment[i] + enjoyment(self.L_props[curr_period] * self.money[i], self.health[i])
        self.money = (money_list[i] * money_prop) + harvest(curr_period)

def generate_population(params_healthcare, params_ga):
  population=[]
  for i in np.arange(params_ga.size_population):
    a_health=[params_healthcare.init_health]
    a_enjoyment = [0]
    a_money = [harvest(params_healthcare,params_healthcare.init_health)]
    a_share_I = [0]
    a_share_L = [0]
    a_share_M = [0]
    for period in np.arange(params_healthcare.periods-1):
      if a_health[period]<=params_healthcare.health_min:
        a_share_I.append(0);
        a_share_L.append(0);
        a_share_M.append(0);
        a_health.append(a_health[period]);
        a_enjoyment.append(a_enjoyment[period]);
        a_money.append(a_money[period]);
      else:
        share_I=np.round(np.random.rand(),2);
        if share_I>=1:
          share_L=np.random.randint(0,100*(1.01-share_I))/100;
        else:
          share_L=np.random.randint(0,100*(1-share_I))/100;
        share_M=np.round(1-share_I-share_L,2);
        a_share_I.append(share_I);
        a_share_L.append(share_L);
        a_share_M.append(share_M);

        a_enjoyment.append(a_enjoyment[period]+life_enjoyment(params_healthcare,a_money[period]*share_L,a_health[period])) ;
        period_health = a_health[period] + val_regenerate(params_healthcare,a_money[period]*share_I,a_health[period]) - val_degenerate(params_healthcare,period)
        health = period_health if period_health > params_healthcare.health_min else 0 ;
        a_health.append(health);
        a_money.append(a_share_M[period]*a_money[period]+harvest(params_healthcare,health))
    population.append(Agent(a_share_I,a_share_L,a_share_M,a_health,a_enjoyment,a_money));
  return population
def show_population(agents_list):
   return [(agents.share_I,agents.share_L,agents.share_money,agents.health,agents.enjoyment,agents.money) for agents in agents_list ]

agents_a=generate_population(params_healthcare, params_ga)

pl=show_population(agents_a)
print(pl)

