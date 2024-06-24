#import libraries
import pandas as pd # for dataframes 
import matplotlib.pyplot as plot # for graphs
# read the excel file in dataframe
dataframe=pd.read_excel('dataset3.xlsx')
#making a separate bundle of only Bugs rows by filtering the dataframe
Bugs= dataframe[dataframe['type']=='Bug']
#count of bugs after grouping the data on basis of assignee
BugsCount=Bugs['assignee'].value_counts()
#sort the dataframe in descending order
BugsCount=BugsCount.sort_values(ascending=False)
#create pareto chart
fig,ax1=plot.subplots()
ax1.bar(BugsCount.index,BugsCount.values,color='grey',alpha=0.6,width=1)
ax1.set_ylabel('Number of Bugs')
ax1.set_xlabel('Assignee')
plot.title('Pareto Chart for Bugs Given To each Assignee')
plot.tight_layout() # ensure all elements fit well
plot.show()
