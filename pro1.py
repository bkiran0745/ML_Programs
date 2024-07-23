import pandas as pd
import numpy as np
data=pd.read_csv('lab1.csv')
data
features=np.array(data)[:,:-1]
features
target=np.array(data)[:,-1]
target
for i,val in enumerate(target):
    if val=='yes':
        specific_h=features[i].copy()
        break
print(specific_h)
for i,val in enumerate(features):
    if target[i]=='yes':
        for x in range(len(specific_h)):
            if val[x]!=specific_h[x]:
                specific_h[x]='?'
print(specific_h)

# Dataset:

# Outlook,Temperature,Humidity,Wind,Water,Forecast,PlayTennis
# sunny,warm,normal,strong,warm,same,yes
# sunny,warm,high,strong,warm,same,yes
# rainy,cold,high,weak,warm,change,no
# sunny,warm,high,strong,cool,change,yes
# rainy,warm,normal,strong,warm,change,no
