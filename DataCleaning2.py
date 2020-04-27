import numpy as np
import pandas as pd

def data_cleaning(csvfile):

    df= pd.read_csv(csvfile, parse_dates=['last_trip_date', 'signup_date'])
    df['phone']=df['phone'].fillna(value='iPhone')
    df['Is_iPhone'] = df['phone'].apply(lambda x: 1 if x == 'iPhone' else 0)
    
    
    df['Astapor'] = df['city'].apply(lambda x: 1 if x == 'Astapor' else 0)
    df['Winterfell'] = df['city'].apply(lambda x: 1 if x == 'Winterfell' else 0)
    df["King's Landing"] = df['city'].apply(lambda x: 1 if x == "King's Landing" else 0)
    
    df['luxury_car_user'] = df['luxury_car_user'].apply(lambda x: 1 if x == True else 0)
    
    df.drop(columns=['phone','city'],axis=1,inplace=True)
    
    df['avg_rating_by_driver']=df['avg_rating_by_driver'].fillna(value=df['avg_rating_by_driver'].median())
    df['avg_rating_of_driver']=df['avg_rating_of_driver'].fillna(value=df['avg_rating_of_driver'].median())
    pd.to_datetime(df['last_trip_date'])
    pd.to_datetime(df['signup_date'])
    
    
    df['Result']= (df['last_trip_date'] >= '2014-06-01')

    y=df['Result'].values
    df.drop(axis=1,columns=['Result', 'last_trip_date', 'signup_date'],inplace=True)
    X= df.values
    
    return X,y



def eda(csvfile):

    df= pd.read_csv(csvfile, parse_dates=['last_trip_date', 'signup_date'])
    df['phone']=df['phone'].fillna(value='iPhone')
    df['Is_iPhone'] = df['phone'].apply(lambda x: 1 if x == 'iPhone' else 0)
    
    
    df['Astapor'] = df['city'].apply(lambda x: 1 if x == 'Astapor' else 0)
    df['Winterfell'] = df['city'].apply(lambda x: 1 if x == 'Winterfell' else 0)
    df["King's Landing"] = df['city'].apply(lambda x: 1 if x == "King's Landing" else 0)
    
    df['luxury_car_user'] = df['luxury_car_user'].apply(lambda x: 1 if x == True else 0)
    
    df.drop(columns=['phone','city'],axis=1,inplace=True)
    
    df['avg_rating_by_driver']=df['avg_rating_by_driver'].fillna(value=df['avg_rating_by_driver'].median())
    df['avg_rating_of_driver']=df['avg_rating_of_driver'].fillna(value=df['avg_rating_of_driver'].median())
    pd.to_datetime(df['last_trip_date'])
    pd.to_datetime(df['signup_date'])
    
    
    df['Result']= (df['last_trip_date'] >= '2014-06-01')
    
    return df