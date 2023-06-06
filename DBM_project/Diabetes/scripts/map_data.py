import pandas as pd
import numpy as np
from Diabetes.models import demographic_data

# Create your views here.


df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')

def getDataforMap(uniqueCOuntryName,df2):
    dataForMap=[]
    for i in uniqueCOuntryName:
        try:
            tempdf=df3[df3['name']==i]
            temp={}
            temp["code3"]=list(tempdf['code3'].values)[0]
            temp["name"]=i
            temp["value"]=df2[df2['Country/Region']==i]['values'].sum()
            temp["code"]=list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass
    print (len(dataForMap))
    return dataForMap


demo_data = demographic_data.objects.all()
df2= pd.DataFrame(list(demo_data.values('country','year_2021')))
df2.columns=['Country/Region','values']
df2=df2.sort_values(by='values',ascending=False)
countryNames=list(df2['Country/Region'].values)
countsVal=list(df2['values'].values)
maxVal=max(countsVal)
overallCount=sum(countsVal)
logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal )
uniqueCountryNames=pd.unique(df2['Country/Region'])
dataForMapGraph=getDataforMap(uniqueCountryNames,df2)
    
context = {'maxVal': maxVal, 'dataForMapGraph': dataForMapGraph, 'uniqueCountryNames': uniqueCountryNames, 'countryNames':countryNames, 'countsVal':countsVal,'logVals':logVals, 'overallCount':overallCount, 'df2':df2, 'demo_data': demo_data}

print(dataForMapGraph)


