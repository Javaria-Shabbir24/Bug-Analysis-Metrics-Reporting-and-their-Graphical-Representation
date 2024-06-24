##import libraries
#import pandas as pd # for dataframes 
#import matplotlib.pyplot as plot # for graphs
## read the excel file in dataframe
#dataframe=pd.read_excel('dataset2.xlsx')
##making a separate dataframe of only Bugs rows by filtering the dataframe
#ID= dataframe[dataframe['ID'].notnull()]
##count of bugs after grouping the data on basis of priority
#IDCount=ID['Priority'].value_counts()
#print(IDCount)
## Create a mapping for your priorities to numerical values
#priority_mapping = {
#    1:1,
#    4:4,
#    'High': 5,  # Assigning 5 to 'High' 
#}
## Map the priorities to numerical values
#IDCount.index = IDCount.index.map(priority_mapping)
### Sort the DataFrame by the numerical values
#IDCount = IDCount.sort_index()
##create histogram
#plot.figure(figsize=(8,6))
#plot.bar(IDCount.index, IDCount.values,color="red")
#plot.title('Number of IDs Reported by Priority')
#plot.xlabel('Priority')
#plot.ylabel('Number of IDS Reported')
#plot.tight_layout() # ensure all elements fit well
#plot.show()