
import os
import csv

# Path to collect data from the Resources folder
budgetdataCSV = os.path.join('Resources/budget_data.csv')

dates = [] #this will store a list of the dates.
total_amount = 0.00 #this will store the total amount of profit/loss

amounts = [] 
changes = [] #this will store the change 

# Read in the CSV file
with open(budgetdataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Pass header
    csv_header = next(csvreader)
    #print(csv_header)

    # Loop through the data
    for row in csvreader:

        dates.append(row[0])
        total_amount += float(row[1])
        amounts.append(float(row[1]))

#Title
print('\nFinancial Analysis\n------------------------------------')

#The total number of months included in the dataset
months = len(set(dates))
print(f'Total Months: {months}')

#The total net amount of "Profit/Losses" over the entire period
print(f'Total: ${total_amount:.2f}')

#The average change in "Profit/Losses" between months over the entire period
changes.append(0) #first month didn't have changes
for i in range(1,months):
    changes.append(amounts[i] - amounts[i-1])

sum_changes = 0

for i in changes:
    sum_changes += i

print(f'Average Change: ${sum_changes/(months-1):.2f}')

#The greatest increase in profits (date and amount) over the entire period
tmp_index = 0

for i in range(len(changes)):
    if changes[i] > changes[tmp_index]:
        tmp_index = i

print(f'Greatest Increase in Profits: {dates[tmp_index]} (${changes[tmp_index]:.2f})')

#The greatest decrease in losses (date and amount) over the entire period
tmp_index = 0

for i in range(len(changes)):
    if changes[i] < changes[tmp_index]:
        tmp_index = i

print(f'Greatest Decrease in Profits: {dates[tmp_index]} (${changes[tmp_index]:.2f})')