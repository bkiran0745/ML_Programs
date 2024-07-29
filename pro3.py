import pandas as pd
from collections import Counter
import math
tennis=pd.read_csv('playtennis.csv')
print("\n Given Play Tennis Data Set:\n\n",tennis)
def entropy(alist):
    c=Counter(x for x in alist)
    instances=len(alist)
    prob=[x / instances for x in c.values()]
    return sum( [-p*math.log(p,2)for p in prob])
def information_gain(d,split,target):
    splitting=d.groupby(split)
    n=len(d.index)
    agent=splitting.agg({target :[entropy,lambda x:len(x)/n]})[target]
    agent.columns=['entropy','observations']
    newentropy=sum(agent['entropy']* agent['observations'])
    oldentropy=entropy(d[target])
    return oldentropy-newentropy
def id3(sub,target,a):
    count=Counter(x for x in sub[target])
    if len(count)==1:
        return next(iter(count))
    else:
        gain =[information_gain(sub,attr,target)for attr in a]
        print("\n Gain=",gain)
        maximum=gain.index(max(gain))
        best=a[maximum]
        print("\n best attribute:",best)
        tree={best:{}}
        remaining=[i for i in a if i != best]
        
        for val,subset in sub.groupby(best):
            subtree=id3(subset,target,remaining)
            tree[best][val]=subtree
        return tree
names=list(tennis.columns)
print("\n List of Attributes:", names)
names.remove('PlayTennis')
print("\n predicting Attributes:",names)

tree=id3(tennis,'PlayTennis',names)
print("\n The resultant decision tree is :\n")
print(tree)



#Data set

# outlook,temperature,humidity,wind,PlayTennis
# answer sunny,hot,high,weak,no
# sunny,hot,high,strong,no
# overcast,hot,high,weak,yes
# rain,mild,high,weak,yes
# rain,cool,normal,weak,yes
# rain,cool,normal,strong,no
# overcast,cool,normal,strong,yes
# sunny,mild,high,weak,no
# sunny,cool,normal,weak,yes
# rain,mild,normal,weak,yes
# sunny,mild,normal,strong,yes
# overcast,mild,high,strong,yes
# overcast,hot,normal,weak,yes
# rain,mild,high,strong,no