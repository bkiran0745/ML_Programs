import numpy as np
import pandas as pd
data=pd.read_csv('lab1.csv')

features=np.array(data)[:,:-1]

target=np.array(data)[:,-1]

specific_h=features[0].copy()
print("initilazation of specific_h and general_h")
print(specific_h)
general_h=[["?"for  i in range(len(specific_h))]for i in range(len(specific_h))]
print(general_h)
for i,h in enumerate(features):
    if target[i]=="yes":
        for x in range(len(specific_h)):
            if h[x]!=specific_h[x]:
                specific_h[x]='?'
                general_h[x][x]='?'
    if target[i]=="no":
        for x in range(len(specific_h)):
            if h[x]!=specific_h[x]:
                general_h[x][x]=specific_h[x]
            else:
                general_h[x][x]='?'
print(specific_h,"\n")
print(general_h,"\n")
indices=[i for i,val in enumerate(general_h)if val==['?','?','?','?','?','?']]
for i in indices:
    general_h.remove(['?','?','?','?','?','?'])
print("\n final specific_h",specific_h,sep="\n")
print("\n final general_h",general_h,sep="\n")


# Dataset:

# Outlook,Temperature,Humidity,Wind,Water,Forecast,PlayTennis
# sunny,warm,normal,strong,warm,same,yes
# sunny,warm,high,strong,warm,same,yes
# rainy,cold,high,weak,warm,change,no
# sunny,warm,high,strong,cool,change,yes
# rainy,warm,normal,strong,warm,change,no
