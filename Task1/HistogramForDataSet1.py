##import libraries
#import pandas as pd # for dataframes 
#import matplotlib.pyplot as plot # for graphs
## read the excel file in dataframe
#dataframe=pd.read_excel('dataset1.xlsx')
##making a separate bundle of only Bugs rows by filtering the dataframe
#Bugs= dataframe[dataframe['type']=='Bug']
##count of bugs after grouping the data on basis of priority
#BugsCount=Bugs['priority'].value_counts()
##create histogram
#plot.figure(figsize=(8,6))
#plot.bar(BugsCount.index, BugsCount.values, color='skyblue')
#plot.title('Number of Bugs Reported by Priority')
#plot.xlabel('Priority')
#plot.ylabel('Number of Bugs Reported')
#plot.tight_layout() # ensure all elements fit well
#plot.show()
 








