import pandas as pd
#for all modules 

# read excel file
dataframe = pd.read_excel('dataset3.xlsx')
# Convert 'created' and 'resolved' to datetime and also handle errors
dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
dataframe['resolved'] = pd.to_datetime(dataframe['resolved'], errors='coerce')
# Remove rows with invalid dates such as missing values
dataframe = dataframe.dropna(subset=['created', 'resolved'])
#calculating response time in hours (time between problem opened and closed)
dataframe['Response time'] = (dataframe['resolved'] - dataframe['created']).dt.total_seconds() / 3600
#median taken to calculate fix response time as outliers were affecting the value of mean
MedianResponseTime = dataframe.groupby('priority')['Response time'].median()
MedianResponseTime.index.name = "Fix Response Time Grouped By Priority For DataSet 3"
print(MedianResponseTime)

#for module A 

# read excel file
dataframe = pd.read_excel('dataset3.xlsx',sheet_name='A')
# Convert 'created' and 'resolved' to datetime and also handle errors
dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
dataframe['resolved'] = pd.to_datetime(dataframe['resolved'], errors='coerce')
# Remove rows with invalid dates such as missing values
dataframe = dataframe.dropna(subset=['created', 'resolved'])
#calculating response time in hours (time between problem opened and closed)
dataframe['Response time'] = (dataframe['resolved'] - dataframe['created']).dt.total_seconds() / 3600
#median taken to calculate fix response time as outliers were affecting the value of mean
MedianResponseTime = dataframe.groupby('priority')['Response time'].median()
MedianResponseTime.index.name = "Fix Response Time Grouped By Priority For Module A"
print(MedianResponseTime)

#for module C 

# read excel file
dataframe = pd.read_excel('dataset3.xlsx',sheet_name='C')
# Convert 'created' and 'resolved' to datetime and also handle errors
dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
dataframe['resolved'] = pd.to_datetime(dataframe['resolved'], errors='coerce')
# Remove rows with invalid dates such as missing values
dataframe = dataframe.dropna(subset=['created', 'resolved'])
#calculating response time in hours (time between problem opened and closed)
dataframe['Response time'] = (dataframe['resolved'] - dataframe['created']).dt.total_seconds() / 3600
#median taken to calculate fix response time as outliers were affecting the value of mean
MedianResponseTime = dataframe.groupby('priority')['Response time'].median()
MedianResponseTime.index.name = "Fix Response Time Grouped By Priority For Module C"
print(MedianResponseTime)


#for module D

# read excel file
dataframe = pd.read_excel('dataset3.xlsx',sheet_name='D')
# Convert 'created' and 'resolved' to datetime and also handle errors
dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
dataframe['resolved'] = pd.to_datetime(dataframe['resolved'], errors='coerce')
# Remove rows with invalid dates such as missing values
dataframe = dataframe.dropna(subset=['created', 'resolved'])
#calculating response time in hours (time between problem opened and closed)
dataframe['Response time'] = (dataframe['resolved'] - dataframe['created']).dt.total_seconds() / 3600
#median taken to calculate fix response time as outliers were affecting the value of mean
MedianResponseTime = dataframe.groupby('priority')['Response time'].median()
MedianResponseTime.index.name = "Fix Response Time Grouped By Priority For Module D"
print(MedianResponseTime)

#for module W

# read excel file
dataframe = pd.read_excel('dataset3.xlsx',sheet_name='W')
# Convert 'created' and 'resolved' to datetime and also handle errors
dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
dataframe['resolved'] = pd.to_datetime(dataframe['resolved'], errors='coerce')
# Remove rows with invalid dates such as missing values
dataframe = dataframe.dropna(subset=['created', 'resolved'])
#calculating response time in hours (time between problem opened and closed)
dataframe['Response time'] = (dataframe['resolved'] - dataframe['created']).dt.total_seconds() / 3600
#median taken to calculate fix response time as outliers were affecting the value of mean
MedianResponseTime = dataframe.groupby('priority')['Response time'].median()
MedianResponseTime.index.name = "Fix Response Time Grouped By Priority For Module W"
print(MedianResponseTime)
