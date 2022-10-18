#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import simpy as sp
np.random.seed(344)


# # The simulation I coded works but my values are different, I showed the simulation step by step to see if there are errors, but I could not find any errors. Just the random values assigned to me are different, PLEASE you can check them below

# In[2]:


#### FOR 2 DOCTORS ####


times_to_first_doctor_for_NIA_patients = []
times_to_first_doctor_for_CW_patients = []
times_to_second_doctor_for_NIA_patients = []
times_to_second_doctor_for_CW_patients = []
discharge_for_NIA_patients = []
discharge_for_CW_patients = []
service_times = []
queue_times = []

def patients(env, name, doctors):
    

    if np.random.rand() < 0.2:
        NIA_arriving_time_hospital = env.now
        print("{:s} arrives at the NIA FIRST at {:.2f}.".format(name, env.now))
        doctor_request = doctors.request(-3)
        yield doctor_request
        
        print("{:s} enters the  NIA FİRST at {:.2f}.".format(name, env.now))
        service_time_NIA_first = np.random.randint(3, 77)        
        NIA_entering_time_first = env.now        
        if NIA_arriving_time_hospital > 2880 or NIA_entering_time_first > 2880:
            times_to_first_doctor_for_NIA_patients.append(NIA_entering_time_first - NIA_arriving_time_hospital)
            service_times.append(service_time_NIA_first)
            queue_times.append(NIA_entering_time_first-NIA_arriving_time_hospital)
        yield env.timeout(service_time_NIA_first)
        
        
        print("{:s} leaves the NIA FİRST at {:.2f}.".format(name, env.now))
        doctors.release(doctor_request)
        
        print("{:s} arrives at the NIA SECOND at {:.2f}.".format(name, env.now))
        NIA_arrives_second = env.now
        doctor_request = doctors.request(-2)
        yield doctor_request
        
        print("{:s} enters the NIA SECOND at {:.2f}.".format(name, env.now))
        service_time_NIA_second = np.random.randint(5, 55)
        NIA_entering_time_second = env.now
        if NIA_arriving_time_hospital > 2880 or NIA_entering_time_second > 2880:
            times_to_second_doctor_for_NIA_patients.append(NIA_entering_time_second - NIA_arriving_time_hospital)
            service_times.append(service_time_NIA_second)
            queue_times.append(NIA_entering_time_second-NIA_arrives_second)
        yield env.timeout(service_time_NIA_second)
        
        print("{:s} leaves the NIA SECOND at {:.2f}.".format(name, env.now))
        NIA_discharge_time= env.now
        if NIA_arriving_time_hospital > 2880 or NIA_discharge_time > 2880:
            discharge_for_NIA_patients.append(NIA_discharge_time - NIA_arriving_time_hospital)
        doctors.release(doctor_request)

    else:
        CW_arriving_time_hospital = env.now
        print("{:s} arrives at the CW FİRST at {:.2f}.".format(name, env.now))
        doctor_request = doctors.request(-1)
        yield doctor_request
        
        print("{:s} enters the CW first at {:.2f}.".format(name, env.now))
        service_time_CW_first = np.random.randint(1, 29)
        CW_entering_time_first = env.now
        if CW_arriving_time_hospital > 2880 or CW_entering_time_first > 2880:
            times_to_first_doctor_for_CW_patients.append(CW_entering_time_first-CW_arriving_time_hospital)
            service_times.append(service_time_CW_first)
            queue_times.append(CW_entering_time_first-CW_arriving_time_hospital)

        yield env.timeout(service_time_CW_first)
        
        
        print("{:s} leaves the CW first at {:.2f}.".format(name, env.now))
        doctors.release(doctor_request)

        

        print("{:s} arrives at the CW SECOND at {:.2f}.".format(name, env.now))
        CW_arrives_second = env.now
        doctor_request = doctors.request(-2)
        yield doctor_request    
    

    
        print("{:s} enters the CW SECOND at {:.2f}.".format(name, env.now))        
        service_time_CW_second = np.random.randint(2, 18)
        CW_entering_time_second = env.now
        if CW_arriving_time_hospital > 2880 or CW_entering_time_second > 2880:
            times_to_second_doctor_for_CW_patients.append(CW_entering_time_second - CW_arriving_time_hospital)
            service_times.append(service_time_CW_second)
            queue_times.append(CW_entering_time_second-CW_arrives_second)

        yield env.timeout(service_time_CW_second)

        print("{:s} leaves the CW SECOND at {:.2f}.".format(name, env.now))
        CW_discharge_time= env.now
        if CW_arriving_time_hospital > 2880 or CW_discharge_time > 2880:
            discharge_for_CW_patients.append(CW_discharge_time - CW_arriving_time_hospital)        
        doctors.release(doctor_request)

    

    


        

def setup(env):
    doctors = sp.PriorityResource(env, 2)
    for i in np.arange(1):
        env.process(patients(env, "patient {:d}".format(i), doctors))
    while True:
        interarrival_time = np.random.randint(21, 59)
        yield env.timeout(interarrival_time)
        i = i + 1
        env.process(patients(env, "patient {:d}".format(i), doctors))


env = sp.Environment()
env.process(setup(env))
    
env.run(until=31680)



# In[3]:


#### STATISTICS FOR 2 DOCTORS ####


Average_time_to_first_doctor_for_NIA_patients = sum(times_to_first_doctor_for_NIA_patients)/len(times_to_first_doctor_for_NIA_patients)
Average_time_to_first_doctor_for_CW_patients = sum(times_to_first_doctor_for_CW_patients)/len(times_to_first_doctor_for_CW_patients)
Average_time_to_second_doctor_for_NIA_patients = sum(times_to_second_doctor_for_NIA_patients)/len(times_to_second_doctor_for_NIA_patients)
Average_time_to_second_doctor_for_CW_patients = sum(times_to_second_doctor_for_CW_patients)/len(times_to_second_doctor_for_CW_patients)

Average_time_to_discharge_for_NIA_patients = sum(discharge_for_NIA_patients)/len(discharge_for_NIA_patients)
Average_time_to_discharge_for_CW_patients = sum(discharge_for_CW_patients)/len(discharge_for_CW_patients)

Average_doctor_utilization = sum(service_times) / 57600
Average_queue_time = sum(queue_times) / 57600
Average_queue_length = (Average_queue_time * 2) / Average_doctor_utilization
print('Average time to first doctor for NIA patients = ', Average_time_to_first_doctor_for_NIA_patients)
print('Average time to first doctor for CW patients = ', Average_time_to_first_doctor_for_CW_patients)
print('Average time to second doctor for NIA patients = ', Average_time_to_second_doctor_for_NIA_patients)
print('Average time to second doctor for CW patients = ', Average_time_to_second_doctor_for_CW_patients)
print('Average time to discharge for NIA patients = ', Average_time_to_discharge_for_NIA_patients)
print('Average time to discharge for CW patients = ', Average_time_to_discharge_for_CW_patients)
print('Average doctor utilization = ', Average_doctor_utilization)
print('Average queue length = ', Average_queue_length)


# In[4]:


#### FOR 1 DOCTORS ####


times_to_first_doctor_for_NIA_patients = []
times_to_first_doctor_for_CW_patients = []
times_to_second_doctor_for_NIA_patients = []
times_to_second_doctor_for_CW_patients = []
discharge_for_NIA_patients = []
discharge_for_CW_patients = []
service_times = []
queue_times = []

def patients(env, name, doctors):
    

    if np.random.rand() < 0.2:
        NIA_arriving_time_hospital = env.now
        print("{:s} arrives at the NIA FIRST at {:.2f}.".format(name, env.now))
        doctor_request = doctors.request(-3)
        yield doctor_request
        
        print("{:s} enters the  NIA FİRST at {:.2f}.".format(name, env.now))
        service_time_NIA_first = np.random.randint(3, 77)        
        NIA_entering_time_first = env.now        
        if NIA_arriving_time_hospital > 2880 or NIA_entering_time_first > 2880:
            times_to_first_doctor_for_NIA_patients.append(NIA_entering_time_first - NIA_arriving_time_hospital)
            service_times.append(service_time_NIA_first)
            queue_times.append(NIA_entering_time_first-NIA_arriving_time_hospital)
        yield env.timeout(service_time_NIA_first)
        
        
        print("{:s} leaves the NIA FİRST at {:.2f}.".format(name, env.now))
        doctors.release(doctor_request)
        
        print("{:s} arrives at the NIA SECOND at {:.2f}.".format(name, env.now))
        NIA_arrives_second = env.now
        doctor_request = doctors.request(-2)
        yield doctor_request
        
        print("{:s} enters the NIA SECOND at {:.2f}.".format(name, env.now))
        service_time_NIA_second = np.random.randint(5, 55)
        NIA_entering_time_second = env.now
        if NIA_arriving_time_hospital > 2880 or NIA_entering_time_second > 2880:
            times_to_second_doctor_for_NIA_patients.append(NIA_entering_time_second - NIA_arriving_time_hospital)
            service_times.append(service_time_NIA_second)
            queue_times.append(NIA_entering_time_second-NIA_arrives_second)
        yield env.timeout(service_time_NIA_second)
        
        print("{:s} leaves the NIA SECOND at {:.2f}.".format(name, env.now))
        NIA_discharge_time= env.now
        if NIA_arriving_time_hospital > 2880 or NIA_discharge_time > 2880:
            discharge_for_NIA_patients.append(NIA_discharge_time - NIA_arriving_time_hospital)
        doctors.release(doctor_request)

    else:
        CW_arriving_time_hospital = env.now
        print("{:s} arrives at the CW FİRST at {:.2f}.".format(name, env.now))
        doctor_request = doctors.request(-1)
        yield doctor_request
        
        print("{:s} enters the CW first at {:.2f}.".format(name, env.now))
        service_time_CW_first = np.random.randint(1, 29)
        CW_entering_time_first = env.now
        if CW_arriving_time_hospital > 2880 or CW_entering_time_first > 2880:
            times_to_first_doctor_for_CW_patients.append(CW_entering_time_first-CW_arriving_time_hospital)
            service_times.append(service_time_CW_first)
            queue_times.append(CW_entering_time_first-CW_arriving_time_hospital)

        yield env.timeout(service_time_CW_first)
        
        
        print("{:s} leaves the CW first at {:.2f}.".format(name, env.now))
        doctors.release(doctor_request)

        

        print("{:s} arrives at the CW SECOND at {:.2f}.".format(name, env.now))
        CW_arrives_second = env.now
        doctor_request = doctors.request(-2)
        yield doctor_request    
    

    
        print("{:s} enters the CW SECOND at {:.2f}.".format(name, env.now))        
        service_time_CW_second = np.random.randint(2, 18)
        CW_entering_time_second = env.now
        if CW_arriving_time_hospital > 2880 or CW_entering_time_second > 2880:
            times_to_second_doctor_for_CW_patients.append(CW_entering_time_second - CW_arriving_time_hospital)
            service_times.append(service_time_CW_second)
            queue_times.append(CW_entering_time_second-CW_arrives_second)

        yield env.timeout(service_time_CW_second)

        print("{:s} leaves the CW SECOND at {:.2f}.".format(name, env.now))
        CW_discharge_time= env.now
        if CW_arriving_time_hospital > 2880 or CW_discharge_time > 2880:
            discharge_for_CW_patients.append(CW_discharge_time - CW_arriving_time_hospital)        
        doctors.release(doctor_request)

    

    


        

def setup(env):
    doctors = sp.PriorityResource(env, 1)
    for i in np.arange(1):
        env.process(patients(env, "patient {:d}".format(i), doctors))
    while True:
        interarrival_time = np.random.randint(21, 59)
        yield env.timeout(interarrival_time)
        i = i + 1
        env.process(patients(env, "patient {:d}".format(i), doctors))


env = sp.Environment()
env.process(setup(env))
    
env.run(until=31680)


# In[5]:


#### STATISTICS FOR 1 DOCTOR ####


Average_time_to_first_doctor_for_NIA_patients = sum(times_to_first_doctor_for_NIA_patients)/len(times_to_first_doctor_for_NIA_patients)
Average_time_to_first_doctor_for_CW_patients = sum(times_to_first_doctor_for_CW_patients)/len(times_to_first_doctor_for_CW_patients)
Average_time_to_second_doctor_for_NIA_patients = sum(times_to_second_doctor_for_NIA_patients)/len(times_to_second_doctor_for_NIA_patients)
Average_time_to_second_doctor_for_CW_patients = sum(times_to_second_doctor_for_CW_patients)/len(times_to_second_doctor_for_CW_patients)

Average_time_to_discharge_for_NIA_patients = sum(discharge_for_NIA_patients)/len(discharge_for_NIA_patients)
Average_time_to_discharge_for_CW_patients = sum(discharge_for_CW_patients)/len(discharge_for_CW_patients)

Average_doctor_utilization = sum(service_times) / 57600
Average_queue_time = sum(queue_times) / 57600
Average_queue_length = (Average_queue_time * 2) / Average_doctor_utilization
print('Average time to first doctor for NIA patients = ', Average_time_to_first_doctor_for_NIA_patients)
print('Average time to first doctor for CW patients = ', Average_time_to_first_doctor_for_CW_patients)
print('Average time to second doctor for NIA patients = ', Average_time_to_second_doctor_for_NIA_patients)
print('Average time to second doctor for CW patients = ', Average_time_to_second_doctor_for_CW_patients)
print('Average time to discharge for NIA patients = ', Average_time_to_discharge_for_NIA_patients)
print('Average time to discharge for CW patients = ', Average_time_to_discharge_for_CW_patients)
print('Average doctor utilization = ', Average_doctor_utilization)
print('Average queue length = ', Average_queue_length)


# In[6]:


#### FOR 3 DOCTORS ####


times_to_first_doctor_for_NIA_patients = []
times_to_first_doctor_for_CW_patients = []
times_to_second_doctor_for_NIA_patients = []
times_to_second_doctor_for_CW_patients = []
discharge_for_NIA_patients = []
discharge_for_CW_patients = []
service_times = []
queue_times = []

def patients(env, name, doctors):
    

    if np.random.rand() < 0.2:
        NIA_arriving_time_hospital = env.now
        print("{:s} arrives at the NIA FIRST at {:.2f}.".format(name, env.now))
        doctor_request = doctors.request(-3)
        yield doctor_request
        
        print("{:s} enters the  NIA FİRST at {:.2f}.".format(name, env.now))
        service_time_NIA_first = np.random.randint(3, 77)        
        NIA_entering_time_first = env.now        
        if NIA_arriving_time_hospital > 2880 or NIA_entering_time_first > 2880:
            times_to_first_doctor_for_NIA_patients.append(NIA_entering_time_first - NIA_arriving_time_hospital)
            service_times.append(service_time_NIA_first)
            queue_times.append(NIA_entering_time_first-NIA_arriving_time_hospital)
        yield env.timeout(service_time_NIA_first)
        
        
        print("{:s} leaves the NIA FİRST at {:.2f}.".format(name, env.now))
        doctors.release(doctor_request)
        
        print("{:s} arrives at the NIA SECOND at {:.2f}.".format(name, env.now))
        NIA_arrives_second = env.now
        doctor_request = doctors.request(-2)
        yield doctor_request
        
        print("{:s} enters the NIA SECOND at {:.2f}.".format(name, env.now))
        service_time_NIA_second = np.random.randint(5, 55)
        NIA_entering_time_second = env.now
        if NIA_arriving_time_hospital > 2880 or NIA_entering_time_second > 2880:
            times_to_second_doctor_for_NIA_patients.append(NIA_entering_time_second - NIA_arriving_time_hospital)
            service_times.append(service_time_NIA_second)
            queue_times.append(NIA_entering_time_second-NIA_arrives_second)
        yield env.timeout(service_time_NIA_second)
        
        print("{:s} leaves the NIA SECOND at {:.2f}.".format(name, env.now))
        NIA_discharge_time= env.now
        if NIA_arriving_time_hospital > 2880 or NIA_discharge_time > 2880:
            discharge_for_NIA_patients.append(NIA_discharge_time - NIA_arriving_time_hospital)
        doctors.release(doctor_request)

    else:
        CW_arriving_time_hospital = env.now
        print("{:s} arrives at the CW FİRST at {:.2f}.".format(name, env.now))
        doctor_request = doctors.request(-1)
        yield doctor_request
        
        print("{:s} enters the CW first at {:.2f}.".format(name, env.now))
        service_time_CW_first = np.random.randint(1, 29)
        CW_entering_time_first = env.now
        if CW_arriving_time_hospital > 2880 or CW_entering_time_first > 2880:
            times_to_first_doctor_for_CW_patients.append(CW_entering_time_first-CW_arriving_time_hospital)
            service_times.append(service_time_CW_first)
            queue_times.append(CW_entering_time_first-CW_arriving_time_hospital)

        yield env.timeout(service_time_CW_first)
        
        
        print("{:s} leaves the CW first at {:.2f}.".format(name, env.now))
        doctors.release(doctor_request)

        

        print("{:s} arrives at the CW SECOND at {:.2f}.".format(name, env.now))
        CW_arrives_second = env.now
        doctor_request = doctors.request(-2)
        yield doctor_request    
    

    
        print("{:s} enters the CW SECOND at {:.2f}.".format(name, env.now))        
        service_time_CW_second = np.random.randint(2, 18)
        CW_entering_time_second = env.now
        if CW_arriving_time_hospital > 2880 or CW_entering_time_second > 2880:
            times_to_second_doctor_for_CW_patients.append(CW_entering_time_second - CW_arriving_time_hospital)
            service_times.append(service_time_CW_second)
            queue_times.append(CW_entering_time_second-CW_arrives_second)

        yield env.timeout(service_time_CW_second)

        print("{:s} leaves the CW SECOND at {:.2f}.".format(name, env.now))
        CW_discharge_time= env.now
        if CW_arriving_time_hospital > 2880 or CW_discharge_time > 2880:
            discharge_for_CW_patients.append(CW_discharge_time - CW_arriving_time_hospital)        
        doctors.release(doctor_request)

    

    


        

def setup(env):
    doctors = sp.PriorityResource(env, 3)
    for i in np.arange(1):
        env.process(patients(env, "patient {:d}".format(i), doctors))
    while True:
        interarrival_time = np.random.randint(21, 59)
        yield env.timeout(interarrival_time)
        i = i + 1
        env.process(patients(env, "patient {:d}".format(i), doctors))


env = sp.Environment()
env.process(setup(env))
    
env.run(until=31680)


# In[7]:


#### STATISTICS FOR 3 DOCTORS ####


Average_time_to_first_doctor_for_NIA_patients = sum(times_to_first_doctor_for_NIA_patients)/len(times_to_first_doctor_for_NIA_patients)
Average_time_to_first_doctor_for_CW_patients = sum(times_to_first_doctor_for_CW_patients)/len(times_to_first_doctor_for_CW_patients)
Average_time_to_second_doctor_for_NIA_patients = sum(times_to_second_doctor_for_NIA_patients)/len(times_to_second_doctor_for_NIA_patients)
Average_time_to_second_doctor_for_CW_patients = sum(times_to_second_doctor_for_CW_patients)/len(times_to_second_doctor_for_CW_patients)

Average_time_to_discharge_for_NIA_patients = sum(discharge_for_NIA_patients)/len(discharge_for_NIA_patients)
Average_time_to_discharge_for_CW_patients = sum(discharge_for_CW_patients)/len(discharge_for_CW_patients)

Average_doctor_utilization = sum(service_times) / 57600
Average_queue_time = sum(queue_times) / 57600
Average_queue_length = (Average_queue_time * 2) / Average_doctor_utilization
print('Average time to first doctor for NIA patients = ', Average_time_to_first_doctor_for_NIA_patients)
print('Average time to first doctor for CW patients = ', Average_time_to_first_doctor_for_CW_patients)
print('Average time to second doctor for NIA patients = ', Average_time_to_second_doctor_for_NIA_patients)
print('Average time to second doctor for CW patients = ', Average_time_to_second_doctor_for_CW_patients)
print('Average time to discharge for NIA patients = ', Average_time_to_discharge_for_NIA_patients)
print('Average time to discharge for CW patients = ', Average_time_to_discharge_for_CW_patients)
print('Average doctor utilization = ', Average_doctor_utilization)
print('Average queue length = ', Average_queue_length)

