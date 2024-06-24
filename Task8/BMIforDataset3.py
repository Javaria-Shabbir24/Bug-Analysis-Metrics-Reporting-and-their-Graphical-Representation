#import pandas as pd
## Read the Excel file 
#dataframe = pd.read_excel("dataset3.xlsx")
## Convert 'created' and 'resolved' to datetime and also handle errors
#dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
## Remove rows with invalid dates such as missing values
#dataframe = dataframe.dropna(subset=['created'])
## Extracting the month and year from 'Start date'
#dataframe['Starting Month/Year'] = dataframe['created'].dt.strftime('%Y-%m')
## Number of problems arrived in each month
#ProblemsArrivedDuringAMonth = dataframe.groupby('Starting Month/Year').size()
## calculate closed problems
#dataframe['Closed Problems'] = dataframe['status'] == 'Closed'
##month wise
#ProblemsClosedDuringAMonth= dataframe[dataframe['Closed Problems']].groupby('Starting Month/Year').size()
#BMI=(ProblemsClosedDuringAMonth/ProblemsArrivedDuringAMonth)*100
#BMI.index.name="BMI Month-Wise (Units %)"
#print(BMI)
