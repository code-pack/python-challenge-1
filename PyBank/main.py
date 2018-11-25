
import os
import csv

# Path to collect data from the Resources folder
budgetdataCSV = os.path.join('Resources/budget_data.csv')

months = [] #this will store a list of dates.
profits = [] #this will store a list of profit/loss amounts.
changes = [] #this will store a lisf of values of change of profit between months

# Read in the CSV file
with open(budgetdataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Pass header
    csv_header = next(csvreader)
    #print(csv_header)

    # Loop through the data
    for row in csvreader:

        months.append(row[0])
        profits.append(float(row[1]))
        #total_amount += float(row[1]) #I know I could sum the profit in here.. but I'll do it after. with the sum() function


#The total number of months included in the dataset
months_total = len(set(months))


#The total net amount of "Profit/Losses" over the entire period
total_amount = sum(profits)


#The average change in "Profit/Losses" between months over the entire period
    #the value change will reference the new month.. that's why month 1 is 0, month two change = month two - month one.
changes.append(0) 
for i in range(1,months_total):
    changes.append(profits[i] - profits[i-1])

    #ommiting the first value of the string that is 0 
avg_change = sum(changes[1:]) / len(changes[1:])


#The greatest increase in profits (date and amount) over the entire period
max_index = 0

for i in range(len(changes)):
    if changes[i] > changes[max_index]:
        max_index = i


#The greatest decrease in losses (date and amount) over the entire period
min_index = 0

for i in range(len(changes)):
    if changes[i] < changes[min_index]:
        min_index = i



#print results

print('\nFinancial Analysis\n------------------------------------')
print(f'Total Months: {months_total}')
print(f'Total: ${total_amount:,.2f}')
print(f'Average Change: ${avg_change:,.2f}')
print(f'Greatest Increase in Profits: {months[max_index]} (${changes[max_index]:,.2f})')
print(f'Greatest Decrease in Profits: {months[min_index]} (${changes[min_index]:,.2f})')

#save results to a file
with open("Financial_Analysis_Report.txt", "w") as text_file:
    print('\nFinancial Analysis\n------------------------------------', file=text_file)
    print(f'Total Months: {months_total}', file=text_file)
    print(f'Total: ${total_amount:,.2f}', file=text_file)
    print(f'Average Change: ${avg_change:,.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {months[max_index]} (${changes[max_index]:,.2f})', file=text_file)
    print(f'Greatest Decrease in Profits: {months[min_index]} (${changes[min_index]:,.2f})', file=text_file)
    #print(f"Purchase Amount: {TotalAmount}", file=text_file)