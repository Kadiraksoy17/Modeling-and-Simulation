#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import simpy as sp
import scipy.stats as stats






# # My values are negligibly different, but I don't know why Average station times differ so much in terms of confidence intervals. I want to know why. My simulation is working perfectly fine. I left print("{:s} arrives the c1 for type 1 at {:.2f}.".format(name, env.now)) below so that they can be checked one by one.

# In[2]:


def generate_randomness():
    PROP = np.random.rand()
    return PROP


# In[3]:





def job_stations(env, name, c1, c2, c3, c4):
    LUCK = generate_randomness()
    if LUCK <= 0.4:
        #print("{:s} arrives the c1 for type 1 at {:.2f}.".format(name, env.now))
        typ1_entering_time = env.now        
        job_request = c1.request()
        yield job_request
        
        #print("{:s} enters the c1 for type 1 at {:.2f}.".format(name, env.now))
        typ1_entering_time_c1 = env.now
        service_time_c1_typ1 = np.random.normal(loc=20, scale=3, size=None)
        yield env.timeout(service_time_c1_typ1)
                
        #print("{:s} leaves the c1 for type 1 at {:.2f}.".format(name, env.now))
        typ1_leaving_time_c1 = env.now
        if typ1_leaving_time_c1 > 200 or typ1_entering_time_c1 > 200:
            times_for_station1.append(typ1_leaving_time_c1 - typ1_entering_time_c1)
        c1.release(job_request)
            
        #print("{:s} arrives the c2 for type 1 at {:.2f}.".format(name, env.now))
        job_request = c2.request()
        yield job_request
               
        #print("{:s} enters the c2 for type 1 at {:.2f}.".format(name, env.now))
        typ1_entering_time_c2 = env.now
        service_time_c2_typ1 = np.random.normal(loc=30, scale=5, size=None)
        yield env.timeout(service_time_c2_typ1)
        
        #print("{:s} leaves the c2 for type 1 at {:.2f}.".format(name, env.now))
        typ1_leaving_time_c2 = env.now
        if typ1_leaving_time_c2 > 200 or typ1_entering_time_c2 > 200:
            times_for_station2.append(typ1_leaving_time_c2 - typ1_entering_time_c2)
        c2.release(job_request)

        #print("{:s} arrives the c3 for type 1 at {:.2f}.".format(name, env.now))
        job_request = c3.request()
        yield job_request
        
        #print("{:s} enters the c3 for type 1 at {:.2f}.".format(name, env.now))
        typ1_entering_time_c3 = env.now
        service_time_c3_typ1 = np.random.normal(loc=75, scale=4, size=None)
        yield env.timeout(service_time_c3_typ1)
        
        #print("{:s} leaves the c3 for type 1 at {:.2f}.".format(name, env.now))
        typ1_leaving_time_c3 = env.now
        if typ1_leaving_time_c3 > 200 or typ1_entering_time_c3 > 200:
            times_for_station3.append(typ1_leaving_time_c3 - typ1_entering_time_c3)
        c3.release(job_request)
        
        #print("{:s} arrives the c4 for type 1 at {:.2f}.".format(name, env.now))
        job_request = c4.request()
        yield job_request

        #print("{:s} enters the c4 for type 1 at {:.2f}.".format(name, env.now))
        typ1_entering_time_c4 = env.now
        service_time_c4_typ1 = np.random.normal(loc=20, scale=3, size=None)
        yield env.timeout(service_time_c4_typ1)
        
        #print("{:s} leaves the c4 for type 1 at {:.2f}.".format(name, env.now))
        typ1_leaving_time_c4 = env.now
        typ1_leaving_time = env.now        
        if typ1_leaving_time_c4 > 200 or typ1_entering_time_c4 > 200:
            times_for_station4.append(typ1_leaving_time_c4 - typ1_entering_time_c4)
        if typ1_leaving_time > 200 or typ1_entering_time > 200:
            times_for_typ1.append(typ1_leaving_time - typ1_entering_time)
        c4.release(job_request)
    elif LUCK <= 0.7:
        #print("{:s} arrives the c1 for type 2 at {:.2f}.".format(name, env.now))
        typ2_entering_time = env.now        
        job_request = c1.request()
        yield job_request

        #print("{:s} enters the c1 for type 2 at {:.2f}.".format(name, env.now))
        typ2_entering_time_c1 = env.now
        service_time_c1_typ2 = np.random.normal(loc=18, scale=2, size=None)
        yield env.timeout(service_time_c1_typ2)

        #print("{:s} leaves the c1 for type 2 at {:.2f}.".format(name, env.now))
        typ2_leaving_time_c1 = env.now
        if typ2_leaving_time_c1 > 200 or typ2_entering_time_c1 > 200:
            times_for_station1.append(typ2_leaving_time_c1 - typ2_entering_time_c1)
        c1.release(job_request)

        #print("{:s} arrives the c3 for type 2 at {:.2f}.".format(name, env.now))
        job_request = c3.request()
        yield job_request

        #print("{:s} enters the c3 for type 2 at {:.2f}.".format(name, env.now))
        typ2_entering_time_c3 = env.now
        service_time_c3_typ2 = np.random.normal(loc=60, scale=5, size=None)
        yield env.timeout(service_time_c3_typ2)

        #print("{:s} leaves the c3 for type 2 at {:.2f}.".format(name, env.now))
        typ2_leaving_time_c3 = env.now
        if typ2_leaving_time_c3 > 200 or typ2_entering_time_c3 > 200:
            times_for_station3.append(typ2_leaving_time_c3 - typ2_entering_time_c3)
        c3.release(job_request)

        #print("{:s} arrives the c4 for type 2 at {:.2f}.".format(name, env.now))
        job_request = c4.request()
        yield job_request

        #print("{:s} enters the c4 for type 2 at {:.2f}.".format(name, env.now))
        typ2_entering_time_c4 = env.now
        service_time_c4_typ2 = np.random.normal(loc=10, scale=1, size=None)
        yield env.timeout(service_time_c4_typ2)

        #print("{:s} leaves the c4 for type 2 at {:.2f}.".format(name, env.now))
        typ2_leaving_time_c4 = env.now
        typ2_leaving_time = env.now        
        if typ2_leaving_time_c4 > 200 or typ2_entering_time_c4 > 200:
            times_for_station4.append(typ2_leaving_time_c4 - typ2_entering_time_c4)
        if typ2_leaving_time > 200 or typ2_entering_time > 200:
            times_for_typ2.append(typ2_leaving_time - typ2_entering_time)
        c4.release(job_request)
        
    elif LUCK <= 0.9:
        #print("{:s} arrives the c2 for type 3 at {:.2f}.".format(name, env.now))
        typ3_entering_time = env.now        
        job_request = c2.request()
        yield job_request

        #print("{:s} enters the c2 for type 3 at {:.2f}.".format(name, env.now))
        typ3_entering_time_c2 = env.now
        service_time_c2_typ3 = np.random.normal(loc=20, scale=2, size=None)
        yield env.timeout(service_time_c2_typ3)

        #print("{:s} leaves the c2 for type 3 at {:.2f}.".format(name, env.now))
        typ3_leaving_time_c2 = env.now
        if typ3_leaving_time_c2 > 200 or typ3_entering_time_c2 > 200:
            times_for_station2.append(typ3_leaving_time_c2 - typ3_entering_time_c2)
        c2.release(job_request)

        #print("{:s} arrives the c3 for type 3 at {:.2f}.".format(name, env.now))
        job_request = c3.request()
        yield job_request

        #print("{:s} enters the c3 for type 3 at {:.2f}.".format(name, env.now))
        typ3_entering_time_c3 = env.now
        service_time_c3_typ3 = np.random.normal(loc=50, scale=8, size=None)
        yield env.timeout(service_time_c3_typ3)

        #print("{:s} leaves the c3 for type 3 at {:.2f}.".format(name, env.now))
        typ3_leaving_time_c3 = env.now
        if typ3_leaving_time_c3 > 200 or typ3_entering_time_c3 > 200:
            times_for_station3.append(typ3_leaving_time_c3 - typ3_entering_time_c3)
        c3.release(job_request)

        #print("{:s} arrives the c4 for type 3 at {:.2f}.".format(name, env.now))
        job_request = c4.request()
        yield job_request

        #print("{:s} enters the c4 for type 3 at {:.2f}.".format(name, env.now))
        typ3_entering_time_c4 = env.now
        service_time_c4_typ3 = np.random.normal(loc=10, scale=1, size=None)
        yield env.timeout(service_time_c4_typ3)

        #print("{:s} leaves the c4 for type 3 at {:.2f}.".format(name, env.now))
        typ3_leaving_time_c4 = env.now
        typ3_leaving_time = env.now        
        if typ3_leaving_time_c4 > 200 or typ3_entering_time_c4 > 200:
            times_for_station4.append(typ3_leaving_time_c4 - typ3_entering_time_c4)
        if typ3_leaving_time > 200 or typ3_entering_time > 200:
            times_for_typ3.append(typ3_leaving_time - typ3_entering_time)
        c4.release(job_request)
        
    else:
        #print("{:s} arrives the c1 for type 4 at {:.2f}.".format(name, env.now))
        typ4_entering_time = env.now        
        job_request = c1.request()
        yield job_request

        #print("{:s} enters the c1 for type 4 at {:.2f}.".format(name, env.now))
        typ4_entering_time_c1 = env.now
        service_time_c1_typ4 = np.random.normal(loc=30, scale=5, size=None)
        yield env.timeout(service_time_c1_typ4)

        #print("{:s} leaves the c1 for type 4 at {:.2f}.".format(name, env.now))
        typ4_leaving_time_c1 = env.now
        if typ4_leaving_time_c1 > 200 or typ4_entering_time_c1 > 200:
            times_for_station1.append(typ4_leaving_time_c1 - typ4_entering_time_c1)
        c1.release(job_request)

        #print("{:s} arrives the c4 for type 4 at {:.2f}.".format(name, env.now))
        job_request = c4.request()
        yield job_request

        #print("{:s} enters the c4 for type 4 at {:.2f}.".format(name, env.now))
        typ4_entering_time_c4 = env.now
        service_time_c4_typ4 = np.random.normal(loc=15, scale=2, size=None)
        yield env.timeout(service_time_c4_typ4)

        #print("{:s} leaves the c4 for type 4 at {:.2f}.".format(name, env.now))
        typ4_leaving_time_c4 = env.now
        typ4_leaving_time = env.now        
        if typ4_leaving_time_c4 > 200 or typ4_entering_time_c4 > 200:
            times_for_station4.append(typ4_leaving_time_c4 - typ4_entering_time_c4)
        if typ4_leaving_time > 200 or typ4_entering_time > 200:
            times_for_typ4.append(typ4_leaving_time - typ4_entering_time)
        c4.release(job_request)

    
    


        

def setup(env):
    c1 = sp.Resource(env, 8)
    c2 = sp.Resource(env, 8)
    c3 = sp.Resource(env, 20)
    c4 = sp.Resource(env, 7)
    for i in np.arange(1):
        env.process(job_stations(env, "job {:d}".format(i), c1, c2, c3, c4))
    while True:
        interarrival_time = np.random.poisson(lam=4.0, size=None)
        yield env.timeout(interarrival_time)
        i = i + 1
        env.process(job_stations(env, "job {:d}".format(i), c1, c2, c3, c4))



# In[4]:


Average_worker_utilization_of_Station1_s = []
Average_worker_utilization_of_Station2_s = []
Average_worker_utilization_of_Station3_s = []
Average_worker_utilization_of_Station4_s = []
Mean_total_response_time_of_Job_type1_s = []
Mean_total_response_time_of_Job_type2_s = []
Mean_total_response_time_of_Job_type3_s = []
Mean_total_response_time_of_Job_type4_s = []

for i in range(344,364):
    times_for_station2 = []
    times_for_station3 = []
    times_for_station4 = []
    times_for_station1 = []
    times_for_typ1 = []
    times_for_typ2 = []
    times_for_typ3 = []
    times_for_typ4 = []
    
    stream = np.random.RandomState(seed = i)
    env = sp.Environment()
    env.process(setup(env))
    env.run(until=800)
    
    total_working_time_of_Station1 = sum(times_for_station1)
    total_working_time_of_Station2 = sum(times_for_station2)
    total_working_time_of_Station3 = sum(times_for_station3)
    total_working_time_of_Station4 = sum(times_for_station4)

    Mean_total_response_time_of_Job_type1 = np.mean(times_for_typ1)
    Mean_total_response_time_of_Job_type2 = np.mean(times_for_typ2)
    Mean_total_response_time_of_Job_type3 = np.mean(times_for_typ3)
    Mean_total_response_time_of_Job_type4 = np.mean(times_for_typ4)

    Average_worker_utilization_of_Station1 = (sum(times_for_station1) / (600*8))
    Average_worker_utilization_of_Station2 = (sum(times_for_station2) / (600*8))
    Average_worker_utilization_of_Station3 = (sum(times_for_station3) / (600*20))
    Average_worker_utilization_of_Station4 = (sum(times_for_station4) / (600*7))
    


    Average_worker_utilization_of_Station1_s.append(Average_worker_utilization_of_Station1)
    Average_worker_utilization_of_Station2_s.append(Average_worker_utilization_of_Station2)
    Average_worker_utilization_of_Station3_s.append(Average_worker_utilization_of_Station3)
    Average_worker_utilization_of_Station4_s.append(Average_worker_utilization_of_Station4)
    Mean_total_response_time_of_Job_type1_s.append(Mean_total_response_time_of_Job_type1)
    Mean_total_response_time_of_Job_type2_s.append(Mean_total_response_time_of_Job_type2)
    Mean_total_response_time_of_Job_type3_s.append(Mean_total_response_time_of_Job_type3)
    Mean_total_response_time_of_Job_type4_s.append(Mean_total_response_time_of_Job_type4)
    
    
    
    print("Performing simulation with seed {:s}".format(str(i)))
    print('Average worker utilization of Station#1:', Average_worker_utilization_of_Station1)
    print('Average worker utilization of Station#2:', Average_worker_utilization_of_Station2)
    print('Average worker utilization of Station#3:', Average_worker_utilization_of_Station3)
    print('Average worker utilization of Station#4:', Average_worker_utilization_of_Station4)
    print('Mean total response time of Job type#1:', Mean_total_response_time_of_Job_type1)
    print('Mean total response time of Job type#2:', Mean_total_response_time_of_Job_type2)
    print('Mean total response time of Job type#3:', Mean_total_response_time_of_Job_type3)
    print('Mean total response time of Job type#4:', Mean_total_response_time_of_Job_type4)
    print('------------------------------------------------------------------------------------------------------------')




A1 = stats.t.interval(alpha=0.95, df=len(Average_worker_utilization_of_Station1_s)-1, loc=np.mean(Average_worker_utilization_of_Station1_s), scale=stats.sem(Average_worker_utilization_of_Station1_s))
A2 = stats.t.interval(alpha=0.95, df=len(Average_worker_utilization_of_Station2_s)-1, loc=np.mean(Average_worker_utilization_of_Station2_s), scale=stats.sem(Average_worker_utilization_of_Station2_s))
A3 = stats.t.interval(alpha=0.95, df=len(Average_worker_utilization_of_Station3_s)-1, loc=np.mean(Average_worker_utilization_of_Station3_s), scale=stats.sem(Average_worker_utilization_of_Station3_s))
A4 = stats.t.interval(alpha=0.95, df=len(Average_worker_utilization_of_Station4_s)-1, loc=np.mean(Average_worker_utilization_of_Station4_s), scale=stats.sem(Average_worker_utilization_of_Station4_s))
M1 = stats.t.interval(alpha=0.95, df=len(Mean_total_response_time_of_Job_type1_s)-1, loc=np.mean(Mean_total_response_time_of_Job_type1_s), scale=stats.sem(Mean_total_response_time_of_Job_type1_s))
M2 = stats.t.interval(alpha=0.95, df=len(Mean_total_response_time_of_Job_type2_s)-1, loc=np.mean(Mean_total_response_time_of_Job_type2_s), scale=stats.sem(Mean_total_response_time_of_Job_type2_s))
M3 = stats.t.interval(alpha=0.95, df=len(Mean_total_response_time_of_Job_type3_s)-1, loc=np.mean(Mean_total_response_time_of_Job_type3_s), scale=stats.sem(Mean_total_response_time_of_Job_type3_s))
M4 = stats.t.interval(alpha=0.95, df=len(Mean_total_response_time_of_Job_type4_s)-1, loc=np.mean(Mean_total_response_time_of_Job_type4_s), scale=stats.sem(Mean_total_response_time_of_Job_type4_s))
print('------------------------------------------------------------------------------------------------------------')

print('95% CI for average worker utilization of Station#1 =', A1)
print('95% CI for average worker utilization of Station#2 =', A2)
print('95% CI for average worker utilization of Station#3 =', A3)
print('95% CI for average worker utilization of Station#4 =', A4)
print('95% CI for mean total response time of Job type#1 =', M1)
print('95% CI for mean total response time of Job type#2 =', M2)
print('95% CI for mean total response time of Job type#3 =', M3)
print('95% CI for mean total response time of Job type#4 =', M4)



# In[ ]:







# In[ ]:




