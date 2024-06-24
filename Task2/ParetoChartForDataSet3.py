##import libraries
#import pandas as pd # for dataframes 
#import matplotlib.pyplot as plot # for graphs
## Load the Excel file
#excel_file = pd.ExcelFile('dataset3.xlsx')
## Get the list of sheet names in the Excel file
#sheet_names = excel_file.sheet_names
## Access a specific sheet by name
#sheet_nameaa = 'All Modules'  # Replace with the name of the sheet you want to access
#SheetAll = excel_file.parse(sheet_nameaa)
#sheet_name = 'A'  # Replace with the name of the sheet you want to access
#SheetA = excel_file.parse(sheet_name)
#sheet_nameC = 'C'  # Replace with the name of the sheet you want to access
#SheetC= excel_file.parse(sheet_nameC)
#sheet_nameD = 'D'  # Replace with the name of the sheet you want to access
#SheetD= excel_file.parse(sheet_nameD)
#sheet_nameW = 'W'  # Replace with the name of the sheet you want to access
#SheetW= excel_file.parse(sheet_nameW)
###making a separate bundle of only Bugs rows by filtering the dataframe
#BugsAA= SheetAll[SheetAll['type']=='Bug']
#BugsA= SheetA[SheetA['type']=='Bug']
#BugsC= SheetC[SheetC['type']=='Bug']
#BugsD= SheetD[SheetD['type']=='Bug']
#BugsW= SheetW[SheetW['type']=='Bug']
###count of bugs after grouping the data on basis of priority
#BugsCount=len(BugsAA)
#ListOfBugs=[len(BugsAA),len(BugsA),len(BugsC),len(BugsD),len(BugsW)]
##sort the dataframe in descending order
## Create a list of bug labels 
#bug_labels = ['ModuleAll', 'ModuleA', 'ModuleC', 'ModuleD', 'ModuleW']
## Combine bug labels and counts into a list of tuples
#bug_data = list(zip(bug_labels, ListOfBugs))
## Sort the bug data in descending order based on counts
#sorted_bug_data = sorted(bug_data, key=lambda x: x[1], reverse=True)
## Unzip the sorted data into separate lists
#sorted_labels, sorted_counts = zip(*sorted_bug_data)
## Create a bar chart
#fig,ax1=plot.subplots()
#ax1.bar(sorted_labels, sorted_counts, color='royalblue',width=1)
## Add labels and title
#ax1.set_ylabel('Number of Bugs')
#plot.title('Pareto Chart of Bugs Of Each Mdule')
## Show the chart
#plot.tight_layout()
#plot.show()


