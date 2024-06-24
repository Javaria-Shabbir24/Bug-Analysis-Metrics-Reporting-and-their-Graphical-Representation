#import pandas as pd
##read the excel file
#dataframe = pd.read_excel("dataset2.xlsx")
## Filter rows where the fix wasn't closed within 4 hours
#dataframe['Start date'] = pd.to_datetime(dataframe['Start date'])#start date to date time format
#dataframe['Finish date'] = pd.to_datetime(dataframe['Finish date'])# end date to date time format
##dt total seconds method contain the interval in seconds 
##dividing by 3600 give the closing time in hours
#dataframe['Closing Time'] = (dataframe['Finish date'] - dataframe['Start date']).dt.total_seconds() / 3600
## checking which row has delinquent values stored as series of boolean values
#dataframe['Delinquent Rows'] = dataframe['Closing Time'] > 4 #greater than 4 given 
## converting in the format of year-month
## grouping month wise , if start date is same then they are in same month
## size calculates the number of delinquent fixes
#dataframe['Start date'] = dataframe['Start date'].dt.strftime('%Y-%m')
##number of fixes that exceeded the response time by severity level
#MonthWiseDelinquentFixes= dataframe[dataframe['Delinquent Rows']].groupby('Start date').size()
#NumberOfFixesDeliveredInASpecifiedTime = dataframe.groupby('Start date').size()
##calculating percent delinquent fixes
#PercentDelinquentFixes = (MonthWiseDelinquentFixes / NumberOfFixesDeliveredInASpecifiedTime) * 100
#PercentDelinquentFixes.index.name = "Percent Delinquent Fixes Month-Wise (Units %) "
#print(PercentDelinquentFixes)