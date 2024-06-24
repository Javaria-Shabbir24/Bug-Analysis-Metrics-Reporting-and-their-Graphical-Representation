##import libraries
#from multiprocessing import Value
#import pandas as pd # for dataframes 
#import matplotlib.pyplot as plot # for graphs
## read the excel file in dataframe
#dataframe=pd.read_excel('dataset2.xlsx')
##initializing a new column
#dataframe['Schedule Estimation Accuracy']=0
##iterating through each row
#for index, row in dataframe.iterrows():
#   try:
#       estimated_time=row['Estimated time']
#       spent_time=row['Spent time (hrs)']
#       #check for division by zero (exceptional handling)
#       if estimated_time==0:
#           raise ValueError("Estimated time is zero")
#       accuracy=spent_time/estimated_time
#       dataframe.at[index,'Schedule Estimation Accuracy']=accuracy
#   except Exception as e:
#       dataframe.at[index, 'Schedule Estimation Accuracy'] = 'Error: ' + str(e)

#print(dataframe[['ID','Status','Estimated time','Spent time (hrs)','Schedule Estimation Accuracy']])
