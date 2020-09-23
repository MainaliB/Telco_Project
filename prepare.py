#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import telco_acquire
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix


# In[13]:


def split_data(df):
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=322, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size= 0.2,
                                       random_state = 322, stratify = train_validate.churn)
    return train, test, validate


# In[3]:


def prep_telco():
    
    telco = telco_acquire.get_telco_data()
    
    telco.total_charges = pd.to_numeric(telco.total_charges, errors = 'coerce')
    
    telco = telco[telco.tenure != 0]
    
    conditions = [(telco['partner']== "Yes") & (telco['dependents'] == 'Yes'),
             (telco['partner']== "No") & (telco['dependents'] == 'No')]



    values = [True, False]




    telco['partner_dependents'] = np.select(conditions, values)
    
    
    conditions1 = [(telco['phone_service'] == 'Yes') & (telco['multiple_lines'] == 'Yes'),
              (telco['phone_service']  == 'Yes') & (telco['multiple_lines'] == 'No'), 
              (telco['phone_service']  == 'Yes') & (telco['multiple_lines'] == 'No phone service'),
              (telco['phone_service']  == 'No') & (telco['multiple_lines'] == 'No'),
             (telco['phone_service']  == 'No') & (telco['multiple_lines'] == 'Yes'),
              (telco['phone_service']  == 'No') & (telco['multiple_lines'] == 'No phone service')   
             ]

    values1 = [True, False, False, False, False,False ]

    telco['phone_and_multiple_lines'] = np.select(conditions1, values1)
    
    
    
    conditions2 = [(telco['streaming_tv']=='Yes') & (telco['streaming_movies'] == 'Yes'),
              (telco['streaming_tv']=='No') & (telco['streaming_movies'] == 'No')]


    values2 = [True, False ]


    telco['streaming_tv_movie'] = np.select(conditions2, values2)
    
    
    
    
    
    
    conditions3 = [(telco['online_security']=='Yes') & (telco['online_backup'] == 'Yes'),
              (telco['online_security']=='No') & (telco['online_backup'] == 'No')]

    values3 = [True, False]
    
    
    telco['online_security_and_backup'] = np.select(conditions3, values3)
    
    
    telco = telco.replace({'payment_type':{'Bank transfer (automatic)':'payment_auto', 'Credit card (automatic)': 'payment_auto',
                                      'Mailed check': 'payment_not_auto', 'Electronic check': 'payment_not_auto'}})

    telco = telco.rename(columns = {'payment_type': 'payment_auto'})
    
    telco = telco.replace({'payment_auto': {'payment_auto': 1, 'payment_not_auto': 0}})
    
    telco = telco.replace({'churn':{'Yes':1, 'No': 0}})
    
    telco = telco.replace({'partner':{'Yes':1, 'No': 0}})
    
    telco = telco.replace({'dependents':{'Yes':1, 'No': 0}})
    
    telco = telco.replace({'paperless_billing':{'Yes':1, 'No': 0}})
    
    telco = telco.replace({'phone_service':{'Yes':1, 'No': 0}})
    
    dummies_contract_type = pd.get_dummies(telco.contract_type)
    
    
    
    dummies_internet_type = pd.get_dummies(telco.internet_service_type)
    
    telco = pd.concat([telco, dummies_contract_type, dummies_internet_type], axis = 1)
    
    telco = telco.replace({'streaming_tv': {'Yes': 1, 'No internet service': 0, 'No':0}})
    
    telco = telco.replace({'streaming_movies': {'Yes': 1, 'No internet service': 0, 'No':0}})
    
    telco = telco.replace({'multiple_lines': {'Yes': 1, 'No internet service': 0, 'No':0, 'No phone service': 0}})
    
    telco = telco.replace({'online_security': {'Yes': 1, 'No internet service': 0, 'No':0}})
    
    telco = telco.replace({'online_backup': {'Yes': 1, 'No internet service': 0, 'No':0}})
    
    telco = telco.replace({'device_protection': {'Yes': 1, 'No internet service': 0, 'No':0}})
    
    telco = telco.replace({'tech_support': {'Yes': 1, 'No internet service': 0, 'No':0}})

    
    cols_to_drop = ['internet_service_type', 'None','contract_type', 'payment_type_id', 
                    'internet_service_type_id','contract_type_id','gender', 'None']
    
    
    telco = telco.drop(columns = cols_to_drop)
    
    
    train, test, validate = split_data(telco)
    return train, test, validate
        


# In[ ]:




