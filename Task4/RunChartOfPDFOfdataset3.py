#import pandas as pd
#import matplotlib.pyplot as plt
## Read the Excel data into a Pandas DataFrame
#dataframe = pd.read_excel('dataset3.xlsx')
## Convert 'created' and 'resolved' to datetime and also handle errors
#dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce')
#dataframe['resolved'] = pd.to_datetime(dataframe['resolved'], errors='coerce')
## Remove rows with invalid dates such as missing values
#dataframe = dataframe.dropna(subset=['created', 'resolved'])
## Calculate time taken to resolve each defect in hours
#dataframe['Resolving Time'] = (dataframe['resolved'] - dataframe['created']).dt.total_seconds() / 3600
## Create a new column to mark defects as delinquent
#dataframe['delinquent rows'] = dataframe['Resolving Time'] > 4 #given
## Group data by year and month, then count total defects and delinquent defects for each group
#dataframe['created'] = dataframe['created'].dt.strftime('%Y-%m')
##number of fixes that exceeded the response time by severity level
#MonthWiseDelinquentFixes= dataframe[dataframe['delinquent rows']].groupby('created').size()
##calculating number of fixes delivered in a specified time
#NumberOfFixesDeliveredInASpecifiedTime = dataframe.groupby('created').size()
##calculating percent delinquent fixes
#PercentDelinquentFixes = (MonthWiseDelinquentFixes / NumberOfFixesDeliveredInASpecifiedTime) * 100
## Create the time run chart
#plt.figure(figsize=(12, 6))
#plt.plot(PercentDelinquentFixes.index, PercentDelinquentFixes.values, marker='o', linestyle='-')
#plt.title("Time Run Chart of Delinquent Fixes")
#plt.xlabel("Year-Month")
#plt.ylabel("Percentage of Delinquent Fixes (%)")
#plt.grid(True)
#plt.xticks(fontsize=5,rotation=45)
#plt.tight_layout()
#plt.show()
