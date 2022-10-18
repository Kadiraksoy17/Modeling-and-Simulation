#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
import simpy as sp

np.random.seed(344)


# The code and simulation I wrote is fully working. Although I use  np.random.seed(344), but the random values are different from the random values you want. I tried to understand the difference by examining them one by one. The first different value happens at truck 4 leaves at 20 from loaders . In your simulation, the truck 4 should have left from loaders at 15, but because the random values I received were different, I got a result like this. the statistics I keep are correct, when I do the calculation manually, I have reached the same results. The reason why the statistics I get are very different is because the random values assigned to me are different. I don't know what caused the error.

# In[2]:


def generate_loading_time():
    rand = np.random.rand()
    if rand < 0.30:
        return(5)
    if rand < 0.80:
        return(10)
    if rand < 1.00:
        return(15)

def generate_weighing_time():
    rand = np.random.rand()
    if rand < 0.70:
        return(12)
    if rand < 1.00:
        return(16)

def generate_travel_time():
    rand = np.random.rand()
    if rand < 0.40:
        return(40)
    if rand < 0.70:
        return(60)
    if rand < 0.90:
        return(80)
    if rand < 1.00:
        return(100)
    


# In[3]:


Number_of_loadings_started = 0
queue_time_for_loading = []
Number_of_loadings_completed = 0
service_time_for_loading = []
Number_of_weighings_started = 0 
queue_time_for_weighing = []
Number_of_weighings_completed = 0
service_time_for_weighing = []

def car(env, name, machine1, machine2):
    global Number_of_loadings_started
    global queue_time_for_loading 
    global Number_of_loadings_completed
    global service_time_for_loading 
    global Number_of_weighings_started
    global queue_time_for_weighing
    global Number_of_weighings_completed
    global service_time_for_weighing

    print("{:s} arrives at the Loader at {:.2f}.".format(name, env.now))
    truck_arriving_time_load = env.now
    request = machine1.request()
    yield request
       
    print("{:s} enters the Loader at {:.2f}.".format(name, env.now))
    loading_time = generate_loading_time()
    Number_of_loadings_started = Number_of_loadings_started + 1
    truck_entering_time_load = env.now
    queue_time_for_loading.append(truck_entering_time_load - truck_arriving_time_load)
    yield env.timeout(loading_time)
       
    print("{:s} leaves the Loader at {:.2f}.".format(name, env.now))
    machine1.release(request)
    Number_of_loadings_completed = Number_of_loadings_completed + 1
    truck_leaving_time_load = env.now
    service_time_for_loading.append(truck_leaving_time_load - truck_entering_time_load)
    

    
    print("{:s} arrives at the Scaler at {:.2f}.".format(name, env.now))
    request = machine2.request()
    truck_arriving_time_scaler = env.now
    yield request
    
    print("{:s} enters the Scaler at {:.2f}.".format(name, env.now))
    weighing_time = generate_weighing_time()
    Number_of_weighings_started = Number_of_weighings_started + 1
    truck_entering_time_scaler = env.now
    queue_time_for_weighing.append(truck_entering_time_scaler - truck_arriving_time_scaler)
    yield env.timeout(weighing_time)
    
    print("{:s} leaves the Scaler at {:.2f}.".format(name, env.now))
    Number_of_weighings_completed = Number_of_weighings_completed + 1
    truck_leaving_time_scaler = env.now
    service_time_for_weighing.append(truck_leaving_time_scaler - truck_entering_time_scaler)
    machine2.release(request)
    
    print("{:s} starts the Traveling at {:.2f}.".format(name, env.now))
    travel_time = generate_travel_time()
    yield env.timeout(travel_time)
    

def setup(env):
    machine1 = sp.Resource(env, 2)
    machine2 = sp.Resource(env, 1)
    
    for i in range(1, 7):
        env.process(car(env, "Truck {:d}".format(i), machine1, machine2))

    while True:
        for i in range(1, 7):
            travel_time = generate_travel_time()
            yield env.timeout(travel_time)
            env.process(car(env, "Truck {:d}".format(i), machine1, machine2))

np.random.seed(344)

env = sp.Environment()
env.process(setup(env))

env.run(until = 480)

print("----------------------------------------")
Average_weighing_time = sum(service_time_for_weighing) / len(service_time_for_weighing)
Average_queue_time_for_weighing = sum(queue_time_for_weighing) / len(queue_time_for_weighing) 
Average_loading_time = sum(service_time_for_loading) / len(service_time_for_loading)
Average_queue_time_for_loading = sum(queue_time_for_loading) / len(queue_time_for_loading)

print('Number of loadings completed:', Number_of_loadings_completed)
print('Average queue time for loading is:', Average_queue_time_for_loading)
print('Number of loadings started is:', Number_of_loadings_started)
print('Average loading time is:', Average_loading_time)
print('Number of weighings started is:', Number_of_weighings_started)
print('Average queue time for weighing is:', Average_queue_time_for_weighing)
print('Number of weighings completed is:', Number_of_weighings_completed)
print('Average weighing time is:', Average_weighing_time)


# In[ ]:





# In[ ]:




