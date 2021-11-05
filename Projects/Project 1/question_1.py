# Computational Economics, Chapman University Fall 2021
# Instructor: Dr. Ryan French
##Project 1 , Question 1
# Author: Kushal Kumar Reddy
# kreddy@chapman.edu

# Reserve Price in the Ascending Clock Auction

import matplotlib.pyplot as plt
import matplotlib
import random
import numpy as np


def ascend_clock(buyers,incre_clock,start_price,reserve_price,iterations=100000,max_value=150):
    min_value=start_price
    #Iterate over the iterations
    buyer_range=np.arange(5,100,5)
    revenues=[]
    for i in range(iterations):
        buyer_values=sorted([random.choice(buyer_range) for x in range(buyers)]) #Assign random buyer values
        rejected=buyer_values[-2]
        winner=buyer_values[-1]
        selling_price= start_price+np.floor((rejected-start_price)/incre_clock)*incre_clock
        if selling_price>=winner and selling_price>start_price:
            selling_price-=incre_clock
        if selling_price>=reserve_price:
            revenues.append(selling_price) # revenues in each period are the last before periods cost
        #elif winner==rejected and (selling_price-incre_clock)>=reserve_price:
            #revenues.append(selling_price-incre_clock)
    return revenues


revenues=[]
reserve_prices=np.arange(5,100,5)
for revenue_price in reserve_prices:
    revenue=ascend_clock(5,1,0,revenue_price)
    if len(revenue)>0:
        revenues.append(sum(revenue)/len(revenue))
    else:
        revenues.append(0)

reserve_max = reserve_prices[np.argmax(revenues)]
revenue_max = np.max(revenues)
text= "reserve_max={:.3f}, revenue_max={:.3f}".format(reserve_max,revenue_max)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
kw = dict(textcoords="axes fraction",arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")

ax=plt.gca()
fig = matplotlib.pyplot.gcf()
plt.plot(np.arange(5,100,5),revenues)
plt.title('Revenues Distribution for Reserve Price')
plt.xlabel('Reserve Prices')
plt.ylabel('Mean Revenue')
plt.grid()

ax.annotate(text, xy=(reserve_max, revenue_max), xytext=(0.94,0.96), **kw)
fig.set_size_inches(12, 8)
fig.savefig('revenue_reserve.png', dpi=100)
plt.show()
print(text)

