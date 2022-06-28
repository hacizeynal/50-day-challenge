"""
Program: Commodity Data Visualization
Author: Ishwor Upreti
Purpose: Program to filter the data from the csv for visualization of price
        in Chicago over the time
Revisions:
        00: Import the libraries
        01: Read the data from csv file
        02: Modify Data from CSV file as required.
        03: Print the product list and ask user to select the product from the 
            list and repeat the same for the date.
        04: Get user input for the location.
        05: Filter the data based on selected product, date and locations
        06: Collect data and calcualte average based on location.
        07: Set up plotly layout and plot the graph.     
"""

# import required module
import csv
from datetime import datetime
import plotly.offline as plt
import plotly.graph_objs as pg


def calculateAverage(var:list)->float:
    '''cal avaerage of list based'''
    return 0.0 if len(var) == 0 else sum(var)/len(var)

def formatedStrYmd(date:datetime)->str:
    '''accept parameter date and return formatted date as str'''
    return datetime.strftime(date,'%Y-%m-%d')

def dateTimeYmd(date:str)->datetime:
    '''return datetime from str date'''
    if '/' in date:
        return datetime.strptime(date,  '%m/%d/%Y')
    return datetime.strptime(date, '%Y-%m-%d')

# check the start/end date number entered by user is valid
def checkDateValidity():
    startDate, endDate = [int(x) for x in input("\nEnter start/end date numbers seperated by a space: ").split()]
    while startDate > endDate:
        print('End date mustn\'t exceeds start date!!')
        startDate, endDate = [int(x) for x in input("Enter start/end date numbers seperated by a space: ").split()]
    return [startDate, endDate]


# function to print multiple columns of proudct
def printPrdColumn(itemList, enum=1, wid=20):
    s = ''
    for n, item in enumerate(itemList):
        if len(s) < 3 * (wid + enum + 2):
            if enum:
                s += f'<{n:{enum}}> '
            s += f'{item:<20}'
        else:
            print(s)
            s = ''
            if enum:
                s += f'<{n:{enum}}> '
            s += f'{item:<20}'
    if s:
        print(s)

# define function to print the dates
def dateColumnPrint(dateList, enum=1, wid=30):
    s = ''
    for n, item in enumerate(dateList):
        if len(s) < 3 * (wid + enum+2):
            if enum:
                s += f'<{n:{enum}}> '
            strDate = formatedStrYmd(item)
            s += f'{strDate:<20}'
        else:
            print(s)
            s = ''
            if enum:
                s += f'<{n:{enum}}> '
            newDate = formatedStrYmd(item)
            s += f'{newDate:<20}'

# Announcement
print(f"{'='*26}\nAnalysis of Commodity Data\n{'='*26}")

# open file and read using csv module
with open('produce_csv.csv', 'r') as csvfile:
    # get the list of all the lines as list and store in data
    data = [row for row in csv.reader(csvfile)]

# Data Cleansing with $ and /
modData = [[float(item.replace('$', '')) if '$' in item else dateTimeYmd(item) if '/' in item else item for item in row]for row in data]

# first get the first row 2nd items onwards as locations
locations = modData.pop(0)[2:]

records = list()  # initialize empty list
for row in modData:
    newRow = row[:2]
    for loc, price in zip(locations, row[2:]):
        # create a new list including name,date location and price
        records.append(newRow + [loc, price])

# sorted unique product list
prdList = sorted(list(set([x[0] for x in records])))

# Show prodcut columns by calling function printPrdColumn
printPrdColumn(prdList, enum = 2)

# taking input from user for the number of items to show in graph
productNumbers = [int(x) for x in input("\nEnter product numbers separated by space: ").split()]

# get list of selected products
selectedPrds = [prdList[i] for i in productNumbers]
print(f'Selected products: {" ".join(selectedPrds)}')
# get the unique date  list from records and sort it
sortedDate = sorted(list(set([x[1] for x in records])))

print('\n\nSELECT DATE RANGE BY NUMBER ...')
# Show prodcut columns by calling function
dateColumnPrint(sortedDate, enum = 2)

# printing the very first date with datetime formating
print(f'Earliest available date is: {formatedStrYmd(sortedDate[0])}\nLatest available date is: {formatedStrYmd(sortedDate[-1])}') 

#selected date from user
dates = [formatedStrYmd(sortedDate[item]) for item in checkDateValidity()]

print(f"Dates from: {dates[0]} to {dates[1]}")
startDate, endDate = [dateTimeYmd(x) for x in dates ] # getting values for date with unpacking

# get the locations
locations = sorted(list(set([x[2] for x in records])))

print('\nSELECT LOCATIONS BY NUMBER ...')
# print the location list
[print(f"<{i}> {j}") for i, j in enumerate(locations)]

#get locations number list
locationNumbers = [int(x) for x in input("\nEnter location numbers separated by spaces: ").split()]
selectedLocations = [locations[i] for i in locationNumbers]
print(f'Selected products: {" ".join(selectedLocations)}')
# filter the recodrs using selected Prdocuts, start, end date and locations
selectedAll = list(filter(lambda x: (x[0] in selectedPrds and (startDate <= x[1] <= endDate) and x[2] in selectedLocations), records))

print(f'\n{len(selectedAll)} record have been selected.')

# make dict of locations
selectedDict = {location: [] for location in selectedLocations}

#update dictinary with location and calculate average
[selectedDict[location].append(calculateAverage([i[3] for i in selectedAll if i[0] == x and i[2] == location])) for x in selectedPrds for location in selectedDict]

# the final list
listToShow = [pg.Bar(x=selectedPrds, y=average, name=location) for location, average in selectedDict.items()]

# set graph title
graphTitle = 'Produce Prices from  ' + formatedStrYmd(startDate) + ' through  ' +formatedStrYmd(endDate)

# defining layout for the plot and title and
plotLayout = pg.Layout(barmode='group',
        title=dict(text='<b> ' + graphTitle +'</b>', x=0.5, xanchor="center"),
        xaxis=dict(title='Product'),yaxis=dict(title='Average Price',tickprefix="$", tickformat=".2f"),
        font=dict(family="Times new roman", size=13, color="#000000"))

# plot layout to the chart 
fig = pg.Figure(data = listToShow, layout = plotLayout)
plt.plot(fig, filename= 'Grouped_BarChart-FinalProject_ISHWO.html')