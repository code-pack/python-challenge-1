
import os
import csv

def get_votes(electiondataCSV):
    # Read in the CSV file
    with open(electiondataCSV, 'r') as csvfile:

        # Split the data by commas
        csvreader = csv.reader(csvfile, delimiter=',')

        #Pass header
        csv_header = next(csvreader)
        #print(csv_header)

        tmp_candcountr = [] #this will store a list of candcountr
        
        # Loop through the data
        for row in csvreader:
            tmp_candcountr.append((row[1],row[2]))

        candcountr = set(tmp_candcountr)
        
        tmp_count = 0 #count votes for each candcountry

        tmp_candcountr = [] #this will store a list of candcountr

        ## this is not an optimal approach because I'm reading the file four times.. 
        for candcountryname in candcountr:
            csvfile.seek(0)

            for row in csvreader:

                if row[1] == candcountryname[0] and row[2] == candcountryname[1]:
                    tmp_count += 1

            tmp_candcountr.append([candcountryname[1],candcountryname[0],tmp_count])

            tmp_count = 0

    tmp_candcountr.sort(key=lambda x: x[2], reverse=True)

    return tmp_candcountr



# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')

votes_by_candcountry = get_votes(electiondataCSV)

for votesss in votes_by_candcountry:
    print(votesss)