import pandas as pd
import csv
import random 
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

#fig=ff.create_distplot([data],["Math_score"], show_hist=False)
#fig.show()

print(statistics.mean(data))
print(statistics.stdev(data))

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        rIndex=random.randint(0,len(data)-1)
        value=data[rIndex]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return mean

meanList=[]
for i in range(0,1000):
    setofmeans=randomsetofmean(100)
    meanList.append(setofmeans)

std=statistics.stdev(meanList)
mean=statistics.mean(meanList)
print(mean,std) 

fig=ff.create_distplot([meanList],["Student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fsds,fsde=mean-std,mean+std
ssds,ssde=mean-2*std,mean+2*std
tsds,tsde=mean-3*std,mean+3*std

print(fsds,fsde)
print(ssds,ssde)
print(tsds,tsde)

#fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode="lines",name="mean"))
# fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode="lines",name="mean"))
# fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode="lines",name="mean"))
# fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode="lines",name="mean"))
# fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode="lines",name="mean"))
# fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
meanofsample1=statistics.mean(data)

fig=ff.create_distplot([meanList],["Student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample1,meanofsample1],y=[0,0.17],mode="lines",name="mean"))
fig.show()

zscore=(meanofsample1-mean)/std
print(zscore)