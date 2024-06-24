#import libraries
import pandas as pd # for dataframes 
import matplotlib.pyplot as plot # for graphs
# Load the Excel file
excel_file = pd.ExcelFile('dataset3.xlsx')
# Get the list of sheet names in the Excel file
sheet_names = excel_file.sheet_names
# Access a specific sheet by name
sheet_nameaa = 'All Modules'  # Replace with the name of the sheet you want to access
SheetAll = excel_file.parse(sheet_nameaa)
sheet_name = 'A'  # Replace with the name of the sheet you want to access
SheetA = excel_file.parse(sheet_name)
sheet_nameC = 'C'  # Replace with the name of the sheet you want to access
SheetC= excel_file.parse(sheet_nameC)
sheet_nameD = 'D'  # Replace with the name of the sheet you want to access
SheetD= excel_file.parse(sheet_nameD)
sheet_nameW = 'W'  # Replace with the name of the sheet you want to access
SheetW= excel_file.parse(sheet_nameW)
#making a separate bundle of only Bugs rows by filtering the dataframe
Bugs= SheetAll[SheetAll['type']=='Bug']
#count of bugs after grouping the data on basis of priority
BugsCount=Bugs['priority'].value_counts()
#create histogram for all modules
plot.figure(figsize=(8,6))
plot.bar(BugsCount.index, BugsCount.values, color='black')
plot.title('Module All - Number of Bugs Reported by Priority')
plot.xlabel('Priority')
plot.ylabel('Number of Bugs Reported')
plot.tight_layout() # ensure all elements fit well
#module A
BugsA= SheetA[SheetA['type']=='Bug']
#count of bugs after grouping the data on basis of priority
BugsCount1=BugsA['priority'].value_counts()
#create histogram
plot.figure(figsize=(8,6))
plot.bar(BugsCount1.index, BugsCount1.values, color='pink')
plot.title('Module A - Number of Bugs Reported by Priority')
plot.xlabel('Priority')
plot.ylabel('Number of Bugs Reported')
plot.tight_layout() # ensure all elements fit well

#module C
BugsC= SheetC[SheetC['type']=='Bug']
#count of bugs after grouping the data on basis of priority
BugsCount2=BugsC['priority'].value_counts()
#create histogram
plot.figure(figsize=(8,6))
plot.bar(BugsCount2.index, BugsCount2.values, color='royalblue')
plot.title('Module C - Number of Bugs Reported by Priority')
plot.xlabel('Priority')
plot.ylabel('Number of Bugs Reported')
plot.tight_layout() # ensure all elements fit well

#module D
BugsD= SheetD[SheetD['type']=='Bug']
#count of bugs after grouping the data on basis of priority
BugsCount3=BugsD['priority'].value_counts()
#create histogram
plot.figure(figsize=(8,6))
plot.bar(BugsCount3.index, BugsCount3.values, color='green')
plot.title('Module D - of Bugs Reported by Priority')
plot.xlabel('Priority')
plot.ylabel('Number of Bugs Reported')
plot.tight_layout() # ensure all elements fit well

#module W
BugsW= SheetW[SheetW['type']=='Bug']
#count of bugs after grouping the data on basis of priority
BugsCount4=BugsW['priority'].value_counts()
#create histogram
plot.figure(figsize=(8,6))
plot.bar(BugsCount4.index, BugsCount4.values, color='red')
plot.title('Module W - of Bugs Reported by Priority')
plot.xlabel('Priority')
plot.ylabel('Number of Bugs Reported')
plot.tight_layout() # ensure all elements fit well

plot.show()