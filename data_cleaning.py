#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

df = pd.read_csv('../data/Raw/crime.csv')
df.info()


# In[20]:


display(df.isnull().sum().sort_values(ascending=False))


# # Crime Data

# In[21]:


def crime_cleaner():
    
    # importing the 'CRIME' dataset
    data_path = "../data/Raw/crime.csv"

    # columns from the dataset to be used in the analysis
    crime_df_columns = ['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
                        'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE','REPORTED_DATE',
                        'DISTRICT_ID', 'PRECINCT_ID', 'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']

    # reading the data into a crime_df
    crime_df = pd.read_csv(data_path, 
                     usecols=crime_df_columns, 
                     dtype={
                         'OFFENSE_CODE': 'category',
                         'OFFENSE_TYPE_ID': 'category',
                         'OFFENSE_CATEGORY_ID': 'category',
                         'NEIGHBORHOOD_ID': 'category',
                         'DISTRICT_ID': 'category',
                         'PRECINCT_ID': 'category',
                         'IS_CRIME': 'bool',
                         'IS_TRAFFIC': 'bool'},
                     low_memory= False)

    # uppercasing text 
    crime_df['NEIGHBORHOOD_ID'] = crime_df['NEIGHBORHOOD_ID'].str.upper()
    crime_df['OFFENSE_TYPE_ID'] = crime_df['OFFENSE_TYPE_ID'].str.upper()
    crime_df['OFFENSE_CATEGORY_ID'] = crime_df['OFFENSE_CATEGORY_ID'].str.upper()

    # saving CRIME INFO to 'crime_info.csv' 
    crime_df.to_csv('../data/Clean/crime_info.csv', index=False)
    
    print('CRIME DATA CLEANED')


# # GEO Data

# In[22]:


def geo_cleaner():
    
    # importing the 'CRIME' dataset
    data_path = "../data/Raw/crime.csv"
    
    # columns from the dataset that provide geolocation information
    geo_fields = ['OFFENSE_ID', 'NEIGHBORHOOD_ID', 'INCIDENT_ADDRESS','GEO_X', 
                  'GEO_Y', 'GEO_LON', 'GEO_LAT']

    # saves the geolocation data separately
    geo_df = pd.read_csv(data_path,usecols=geo_fields,
                        dtype={'NEIGHBORHOOD_ID': 'category'},
                         low_memory=False)

    # uppercasing text
    geo_df['NEIGHBORHOOD_ID'] = geo_df['NEIGHBORHOOD_ID'].str.upper()

    # saving geo info to 'geo_info.csv' 
    geo_df.to_csv('../data/Clean/geo_info.csv', index=False)
    
    print('GEO DATA CLEANED')


# # Offense Codes Data

# In[23]:


def offense_cleaner():

    # importing the 'offense' dataset
    data_path = "../data/Raw/offense_codes.csv"

    # reading the data into a offense_df
    offense_df = pd.read_csv(data_path, 
                     dtype={
                         'OFFENSE_CODE': 'category',
                         'OFFENSE_CODE_EXTENSION': 'category',
                         'OFFENSE_TYPE_ID': 'category',
                         'OFFENSE_TYPE_NAME': 'category',
                         'OFFENSE_CATEGORY_ID': 'category',
                         'OFFENSE_CATEGORY_NAME': 'category',
                         'IS_CRIME': 'bool',
                         'IS_TRAFFIC': 'bool'})

    # uppercasing text
    offense_df['OFFENSE_TYPE_ID'] = offense_df['OFFENSE_TYPE_ID'].str.upper()
    offense_df['OFFENSE_TYPE_NAME'] = offense_df['OFFENSE_TYPE_NAME'].str.upper()
    offense_df['OFFENSE_CATEGORY_ID'] = offense_df['OFFENSE_CATEGORY_ID'].str.upper()
    offense_df['OFFENSE_CATEGORY_NAME'] = offense_df['OFFENSE_CATEGORY_NAME'].str.upper()

    # saving offense info to 'offense_info.csv' 
    offense_df.to_csv('../data/Clean/offense_info.csv', index=False)
    
    print('OFFENSE DATA CLEANED')


# In[24]:


crime_cleaner()
geo_cleaner()
offense_cleaner()

