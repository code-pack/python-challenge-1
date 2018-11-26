
import os
import csv

# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')

votes = 0.0

# Read in the CSV file
with open(electiondataCSV, 'r') as csvfile:

    # Split the data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Pass header
    csv_header = next(csvreader)
    #print(csv_header)

    tmp_candidates = [] #this will store a list of candidates
    
    # Loop through the data
    for row in csvreader:
        tmp_candidates.append(row[2])
        votes += 1
    
    candidates = set(tmp_candidates)
    
    print('\nElection Results\n------------------------------------')
    print(f'Total Votes: {votes:.0f}\n------------------------------------')

    tmp_count = 0 #count votes for each candidate

    ## this is not an optimal approach because I'm reading the file four times.. maybe a Dictionary?
    for candidatename in candidates:
        csvfile.seek(0)

        for row in csvreader:

            if row[2] == candidatename:
                tmp_count += 1


        print(f'{candidatename}: {((tmp_count*100)/votes):.3f}% ({tmp_count})')
        tmp_count = 0


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



## Additional challenge for me..
    #I want to show who won on wich country
    #maybe I can define a dictionary

Dict = {"candidate": 'Berns',
            "countries": {
                "March": 12,
                "Queen": 34,
                "Trandee": 90
            },
            "total_votes": 136}

print('\n\n')
print('Insights')
print('------------------------------------')
print(f'The Candidate {Dict["candidate"]} had a total voting of {Dict["total_votes"]}, Winning on Trandee by {Dict["countries"]["Trandee"]}.\n')