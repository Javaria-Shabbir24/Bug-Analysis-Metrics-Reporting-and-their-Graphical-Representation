#import pandas as pd
## read excel file
#data = pd.read_excel('dataset2.xlsx')
##converting to datetime objects 
#data['Start date'] = pd.to_datetime(data['Start date'])
#data['Finish date'] = pd.to_datetime(data['Finish date'])
##calculating response time in hours (time between problem opened and closed)
#data['Response time'] = (data['Finish date'] - data['Start date']).dt.total_seconds() / 3600
##mean taken to calculate fix response time
#MeanResponseTime = data.groupby('Priority')['Response time'].mean()
#MeanResponseTime.index.name = "Mean Response Time Grouped By Priority"
#print(MeanResponseTime)