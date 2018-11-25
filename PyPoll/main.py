
import os
import csv

# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')


profits = [] #this will store a list of profit/loss amounts.
changes = [] #this will store a lisf of values of change of profit between months
votes = 0.0

# Read in the CSV file
with open(electiondataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Pass header
    csv_header = next(csvreader)
    #print(csv_header)

    tmp_candidates = [] #this will store a set of dates.
    # Loop through the data
    for row in csvreader:

        tmp_candidates.append(row[2])
        votes += 1
    
    candidates = set(tmp_candidates)
    
    print('\nElection Results\n------------------------------------')
    print(f'Total Votes: {votes:.0f}\n------------------------------------')

    count = 0
    for candidatename in candidates:
        csvfile.seek(0)

        for row in csvreader:

            if row[2] == candidatename:
                count += 1


        print(f'{candidatename}: {((count*100)/votes):.3f}% ({count})')
        count = 0


    print('------------------------------------')

    print(f'Winner: <Insert Candidate Name>\n------------------------------------')
     



#The total number of votes cast


#A complete list of candidates who received votes



#The percentage of votes each candidate won



#The total number of votes each candidate won



#The winner of the election based on popular vote.





#print results




#save results to a file
with open("Election_Results_Report.txt", "w") as text_file:
    print('\nElection Results\n------------------------------------', file=text_file)
