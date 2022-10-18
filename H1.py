#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from heapq import heappush
from heapq import heappop
np.random.seed(344)


# In[2]:


### Although every other number is randomly assigned as you want,
### My output is different from you because of "travel time". so the output is different from yours.
### I haven't been able to assign names to trucks and re-spin them.
### Unfortunately, I was having lesson during your office hours, so I could not consult. 

def generate_travel_time():
    rand = np.random.rand()  
    if rand < 0.40:
        return(40)
    if rand < 0.70:
        return(60)
    if rand < 0.9:
        return(80)
    if rand < 1:
        return(100)
     


def generate_loading_time():
    rand = np.random.rand()
    if rand < 0.30:
        return(5)
    if rand < 0.80:
        return(10)
    if rand < 1:
        return(15)

def generate_weighing_time():
    rand = np.random.rand()
    if rand < 0.70:
        return(12)
    if rand < 1:
        return(16)

def print_heap(heap):
    if len(heap) == 0:
        return("")
    else:
        if heap[0][1] == "ES":
            heap_string = "(" + heap[0][1] + ", " + str(heap[0][0]) + ")"
        else:
            heap_string = "(" + heap[0][1] + ", " + str(heap[0][0]) + ", " + heap[0][2] + ")"
        for i in np.arange(1, len(heap)):
            if heap[i][1] == "ES":
                heap_string = heap_string + " (" + heap[i][1] + ", " + str(heap[i][0]) + ")"
            else:
                heap_string = heap_string + " (" + heap[i][1] + ", " + str(heap[i][0]) + ", " + heap[i][2] + ")"
        return(heap_string)


# In[3]:


CLOCK = 0

LQ = 3 #the number of customers in the waiting line
LS = 2 #the number of customers being served (0 or 1)
WQ = 0
WS = 1

FEL = [] #future event list

BL = 0 #total busy time
BS = 0 #total busy time

customers = {"DT1": 0, "DT2": 1,"DT3": 2,"DT4": 3,"DT5": 4,"DT6": 5}

NC = 6 #number of customers
S = 0 #the sum of customer response times for all customers who have departed by the current time
ND = 0 #the total number of departures up to the current simulation time
F = 0


weighing_time = generate_weighing_time()
heappush(FEL, (CLOCK + weighing_time, "EW", "DT1"))

loading2_time = generate_loading_time()
heappush(FEL, (CLOCK + loading2_time, "EL", "DT2"))

loading3_time = generate_loading_time()
heappush(FEL, (CLOCK + loading3_time, "EL", "DT3"))

heappush(FEL, (CLOCK + 480, "ES", ""))

customers['DT3']


# In[4]:


row = "| {:>5d} | {:>2d} | {:>2d} | {:>2d} | {:>2d} | {:>40d} | {:>37d} | {:>2d} | {:>2d} | \n | {:<25s} {:<101s} | {:<15s} |".format

print()
print("------------------------------------------------------------------------------------------------------------------------")
print("| CLOCK | LQ | LS | WQ | WS |               Loader Queue               |               Weigh  Queue            | BL | BS |")
print("-------------------------------------------------------------------------------------------------------------------------")

satır_arası = "----------------------------------------------------------------------------------------------------------------------"
while len(FEL) > 0:
    FEL.sort()
    print(row(CLOCK, LQ, LS, WQ, WS, 0 , 0, BL, BS, "FEL:", print_heap(FEL), satır_arası))
    
    
    (event_time, event_type, Trucks) = heappop(FEL)
    BL = BL + (event_time - CLOCK) * LS
    BS = BS + (event_time - CLOCK) * WS

    CLOCK = event_time
    if event_type == "EL": #EL event
        customers["C" + str(NC)] = event_time       
        if LQ > 0:
            LQ = LQ - 1
            loading_time = generate_loading_time()
            heappush(FEL, (CLOCK + loading_time, "EL", "DT" + str(NC)))
            if WS == 1:
                WQ = WQ +1
            else:
                WS = 1
                weighing_time = generate_weighing_time()
                heappush(FEL, (CLOCK + weighing_time, "EW", "DT" + str(NC)))
        else:
            LS = LS - 1
            if WS == 1:
                WQ = WQ +1
            else:
                WS = 1
                weighing_time = generate_weighing_time()
                heappush(FEL, (CLOCK + weighing_time, "EW", "DT" + str(NC)))
                   
       
    if event_type == "EW": #departure event         
        if WQ > 0:
            WQ = WQ - 1
            weighing_time = generate_weighing_time()
            heappush(FEL, (CLOCK + weighing_time, "EW", "DT" + str(NC)))
        else:
            WS = 0
        travel_time = generate_travel_time()
        heappush(FEL, (CLOCK + travel_time, "ALQ", "DT" + str(NC)))       

        
    if event_type == "ALQ": #end simulation event
        if LS == 2:
            LQ = LQ + 1            
        else:
            LS = LS + 1
            loading_time = generate_loading_time()
            heappush(FEL, (CLOCK + loading_time, "EL", "DT" + str(NC)))
            
    if event_type == "ES": #end simulation event
        print(row(CLOCK, LQ, LS, WQ, WS, 0 , 0, BL, BS, "FEL:", print_heap(FEL), satır_arası))
        break
        
        


# In[ ]:




