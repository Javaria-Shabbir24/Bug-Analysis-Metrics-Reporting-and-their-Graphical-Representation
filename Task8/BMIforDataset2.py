#import pandas as pd
## Read the Excel file 
#dataframe = pd.read_excel("dataset2.xlsx")
## Convert 'Start date' to datetime format
#dataframe['Start date'] = pd.to_datetime(dataframe['Start date'])
## Extracting the month and year from 'Start date'
#dataframe['Starting Month/Year'] = dataframe['Start date'].dt.strftime('%Y-%m')
## Number of problems arrived in each month
#ProblemsArrivedDuringAMonth = dataframe.groupby('Starting Month/Year').size()
## calculate closed problems
#dataframe['Closed Problems'] = dataframe['Status'] == 'Closed'
##month wise
#ProblemsClosedDuringAMonth= dataframe[dataframe['Closed Problems']].groupby('Starting Month/Year').size()
#BMI=(ProblemsClosedDuringAMonth/ProblemsArrivedDuringAMonth)*100
#BMI.index.name="BMI Month-Wise (Units %)"
#print(BMI)
