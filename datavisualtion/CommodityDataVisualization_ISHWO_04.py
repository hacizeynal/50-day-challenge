"""
Program: Commodity Data Visualization
Author: Ishwor Upreti
Purpose: Program to filter the data from the csv for visualization of price
        in Chicago over the time
Revisions:
        00: Import the libraries
        01: Read the data from csv file
        02: Modify Data from CSV file as required.
        03: Initialize  plot
        04: Add the required component to the plot and show the plot.
"""
# import required module
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

print('Commodity Data Visualization')
# open file and read using csv module
with open('produce_csv.csv', 'r') as csvfile:
    # get the list of all the lines as list and store in data
    data = [row for row in csv.reader(csvfile)]

# start data Collection for plotting
# experimented given line with list comprehension
modData = [[float(item.replace('$', ''))
            if '$' in item else datetime.strptime(item, '%m/%d/%Y') \
                if '/' in item else item for item in row ]for row in data]
# for row in data:
#     newRow = list()
#     for item in row:
#         if '$' in item:  # if item have the $ in it's the amount value
#             newRow.append(float(item.replace('$', '')))  # add amount as number
#         elif '/' in item:  # if item have / its data associated with the date
#             newRow.append(datetime.strptime(item, '%m/%d/%Y'))
#         else:
#             newRow.append(item)
#     modData.append(newRow)

# print(modData)

# first get the first row 2nd items onwards as locations
locations = modData.pop(0)[2:]

records = list()  # initialize empty list
for row in modData:
    newRow = row[:2]
    for loc, price in zip(locations, row[2:]):
        # create a new list including name,date location and price
        records.append(newRow + [loc, price])

# print(records)
# filter the data as based on location and  commodities
select = list(filter(lambda x: (x[0].lower() == 'oranges' and x[2].lower() == 'chicago'), records))

dates = [x[1] for x in select]  # x-axis data
prices = [x[3] for x in select]  # y-axis data

# start data plot
fig = plt.figure()  # create figure object from plt
ax = fig.add_subplot()  # add and axis object to the figure

# Add title to th graph
plt.suptitle('The Cost of Oranges in  Chicago')
plt.title('from 2/21/17 through 2/25/18')

# plot the graph with markers
plt.plot(dates, prices, label="Oranges in Chicago")
# set x and y label
plt.xlabel('Date')
plt.ylabel('Price of Oranges')

# add formatting to the price
fmt = '${x:,.2f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# enable legend
plt.legend()

# display the graph
plt.show()
