#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from env import host, user, password
import os


# In[21]:


# Create a function that creates a a url for accessing the database

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    


# In[22]:


# query = sql statement to get the desired data

def get_data():
    query = '''select c.customer_id, c.gender, c.senior_citizen, c.partner, c.dependents, c.tenure, c.phone_service, c.multiple_lines, c.internet_service_type_id, c.online_security, c.online_backup,
c.device_protection, c.tech_support, c.streaming_tv, c.streaming_movies, c.contract_type_id, c.paperless_billing, c.payment_type_id, c.monthly_charges, c.total_charges,c.churn, ct.contract_type, ist.internet_service_type, pt.payment_type
from customers c
join contract_types ct on ct.contract_type_id = c.contract_type_id
join internet_service_types ist on ist.internet_service_type_id = c.internet_service_type_id
join payment_types pt on pt.payment_type_id = c.payment_type_id'''
    telco = pd.read_sql(query, get_connection('telco_churn'))
    telco.to_csv('telco.csv')
    return telco


# In[23]:


# creating a cache so that we wont have to run the whole get data every time

def get_telco_data(cached=False):
    '''
    This function reads in titanic data from Codeup database if cached == False 
    or if cached == True reads in titanic df from a csv file, returns df
    '''
    if cached or os.path.isfile('telco.csv') == False:
        telco = get_data()
    else:
        telco = pd.read_csv('telco.csv', index_col=0)
    return telco


# In[ ]:




