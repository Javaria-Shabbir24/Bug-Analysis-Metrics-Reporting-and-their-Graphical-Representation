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
#PercentDelinquentFixes.index.name = "Percent Delinquent Fixes Month-Wise (Units %) "
## Calculate the mean and standard deviation
#mean = PercentDelinquentFixes.mean()
#StandardDeviation = PercentDelinquentFixes.std()
## Calculate the upper and lower control limits
#UpperControlLimit = mean + 2 * StandardDeviation#formula
#LowerControlLimit = mean - 2 * StandardDeviation#formula
## Create the control chart
#plt.figure(figsize=(12, 6))
#plt.plot(PercentDelinquentFixes, marker='o', color='skyblue', label='Percent Delinquent Fixes')
#plt.axhline(UpperControlLimit, color='red', linestyle='--', label='Upper Control Limit')
#plt.axhline(LowerControlLimit, color='purple', linestyle='--', label='Lower Control Limit')
## Highlight points outside of the control limits
#out_of_control = PercentDelinquentFixes[
#    (PercentDelinquentFixes > UpperControlLimit) | (PercentDelinquentFixes < LowerControlLimit)
#]
## Adjusting marker size of out of control points 
#plt.scatter(out_of_control.index, out_of_control, color='royalblue', label='Out of Control', s=50, edgecolors='black', linewidths=2)
#plt.title("Control Chart for Percent Delinquent Fixes")
#plt.xlabel("Month")
#plt.ylabel("Percent Delinquent Fixes (%)")
#plt.legend()#table or small box that represents different things in a graph
#plt.xticks(fontsize=5,rotation=45)
#plt.tight_layout()
#plt.show()


