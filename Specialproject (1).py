#!/usr/bin/env python
# coding: utf-8

# Initialize. Call the commandoes:

# In[1]:


# Initialization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Class definition.
# The class is defined with the following variables:
# 
# Stream is the number or name of the stream
# 
# Flow is the flow for the specific stream [=] m3/h
# 
# Concentration is the concentration for the specific component [=] mol/m3
# 
# The class is now defined:

# In[2]:


class Batch:
    def __init__(self, Stream, Flow, Concentration):
        self.Stream = Stream
        self.Flow = Flow
        self.Concentration = Concentration

#For this example the calculations are done with two different streams obtaining the following names and values:
#For stream number 1 the flow is 100 m3/h and the concentration is 2 mol/m3
batch1 = Batch("Stream 1", 100, 2)
#For stream number 2 the flow is 50 m3/h and the concentration is 3 mol/m3
batch2 = Batch("Stream 2", 50, 3)


# In[3]:


# Constants definitions
#The time for the inflow is now defined. This specifies for how long the streams will go into the mixer.
#The unit is in hours. For this example the simulation will run for 100 h
T_inflow = 100


# In[4]:


# Variable definition
#The time is now made as an interval going from 1 to the T_inflow value 
time = np.arange(1,T_inflow)


# In[5]:


# Volume calculations 
# To calculate the volume for the streams the following equation is used: 
# V = flow*t 
#The two volumes are calculated:
V_stream1 = batch1.Flow*time
V_stream2 = batch2.Flow*time
# The total flow is the sum of the two volumes, which is then calculated:
V_total = (batch1.Flow+batch2.Flow)*time


# In[6]:


# The system is now calculated, and it is possible to plot the volume of the mixer.
# All 3 volumes are plotted.
# Plot of the volume in the mixer from t=0 to t=T_inflow 
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,V_stream1, label = 'Volume flow 1')
ax.plot(time,V_stream2, label = 'Volume flow 2')
ax.plot(time,V_total, label = 'Volume total flow')
plt.title('Legend inside')
ax.legend()
plt.show()


# In[7]:


#The concentrations in the mixer is then calculated. The concentration is constant and independent on the time. 
#The equation used is:
# C = V_stream*concentration/(V_total)
#Where the stream volume and the concentration is specific for the specie being calculated. 

#Concentration calculations are now possible:
C1 = (batch1.Flow*batch1.Concentration)/((batch1.Flow+batch2.Flow))
C2 = (batch2.Flow*batch2.Concentration)/((batch1.Flow+batch2.Flow))


# In[8]:


# The values of the concentrations are:
print('The value of C1 is ' + repr(C1) + ', and C2 is ' + repr(C2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




