import pandas as pd
import numpy as np
df = pd.read_csv("data.csv")
df2=pd.read_csv('data.csv')#creating dummy dataframe by reading the same data
df2.drop(df2.columns.difference(['y1','y2']), 1, inplace=True)# droping every columns except y1 and y2
a=0
b=7
for i in range(55):

   df2['avg'+str(i)]=np.mean(df.iloc[:,a:b],axis=1)
   a=b
   b=b+7
#after running for loop now our df2 is our  original dataframe (edited) 

df2.to_pickle("modelreadyfortraining.pkl")
