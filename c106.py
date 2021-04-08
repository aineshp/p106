import csv
import plotly.express as px
import pandas as pd
import numpy as np
#with open('C:/Users/aines/Desktop/Python/SalesComparison.csv') as f:
  #  data1=csv.DictReader(f)
   # print(data1)    
   # fig=px.scatter(data1,x='Temperature',y='Ice-cream Sales( â‚¹ )')    
#fig.show()
#with open('C:/Users/aines/Desktop/Python/TvData.csv') as f2:
 #   data2=csv.DictReader(f2)
 #   print(data2)
 #   fig2=px.scatter(data2,x='Size of TV',y='	Average time spent watching TV in a week (hours)')
#fig2.show()    
#with open('C:/Users/aines/Desktop/Python/Coffee.csv') as f:    
    #data3=csv.DictReader(f)
  #  print(data3)
  #  fig=px.scatter(data3,x='Coffee in ml',y='sleep in hours')
#fig.show()
#with open('C:/Users/aines/Desktop/Python/Academics.csv') as f:
 #   data4=csv.DictReader(f)
  #  fig=px.scatter(data4,x='Days Present',y='sleep In Percentage')
#fig.show()    
def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    with open(dataPath) as f:
        csvRead1=csv.DictReader(f)
        for row in csvRead1:
            coffee.append(float(row['Temperature']))    
            sleep.append(float(row['Ice-cream Sales( â‚¹ )']))
        return{'x':coffee,'y':sleep}
def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation Coefficient: ', corelation[0,1])
def setup():
    dataPath='C:/Users/aines/Desktop/Python/SalesComparison.csv'
    dataSource=getDataSource(dataPath)
    findCorelation(dataSource)
setup()       