
import os
import csv

# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')

votes = 0.0

votes_by_candidate = []

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
    
    tmp_count = 0 #count votes for each candidate

    ## this is not an optimal approach because I'm reading the file four times.. ask Rafa or Eduardo
    for candidatename in candidates:
        csvfile.seek(0)

        for row in csvreader:

            if row[2] == candidatename:
                tmp_count += 1

        votes_by_candidate.append((candidatename,tmp_count))

        tmp_count = 0

votes_by_candidate.sort(key=lambda x: x[1], reverse=True)


#print results

print('\nElection Results\n------------------------------------')
print(f'Total Votes: {votes:.0f}\n------------------------------------')

for candidate_i in votes_by_candidate:
    print(f'{candidate_i[0]}: {( ( candidate_i[1]*100 ) / votes ):.3f}% ({candidate_i[1]})')
print('------------------------------------')
print(f'Winner: {votes_by_candidate[0][0]}')

print('------------------------------------')



#save results to a file
with open("Election_Results_Report.txt", "w") as text_file:
    print('\nElection Results\n------------------------------------', file=text_file)
    print(f'Total Votes: {votes:.0f}\n------------------------------------', file=text_file)

    for candidate_i in votes_by_candidate:
        print(f'{candidate_i[0]}: {( ( candidate_i[1]*100 ) / votes ):.3f}% ({candidate_i[1]})', file=text_file)
        
    print('------------------------------------', file=text_file)
    print(f'Winner: {votes_by_candidate[0][0]}', file=text_file)
    print('------------------------------------', file=text_file)
    



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

print('\n')
print('Insights')
print('------------------------------------')
print(f'The Candidate {Dict["candidate"]} had a total voting of {Dict["total_votes"]}, Winning on Trandee by {Dict["countries"]["Trandee"]}.\n')



votes = 0.0

votes_by_country = []

# Read in the CSV file
with open(electiondataCSV, 'r') as csvfile:

    # Split the data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Pass header
    csv_header = next(csvreader)
    #print(csv_header)

    tmp_countrys = [] #this will store a list of countrys
    
    # Loop through the data
    for row in csvreader:
        tmp_countrys.append(row[1])
        votes += 1
    
    countrys = set(tmp_countrys)
    
    tmp_count = 0 #count votes for each country

    ## this is not an optimal approach because I'm reading the file four times.. ask Rafa or Eduardo
    for countryname in countrys:
        csvfile.seek(0)

        for row in csvreader:

            if row[1] == countryname:
                tmp_count += 1

        votes_by_country.append((countryname,tmp_count))

        tmp_count = 0

votes_by_country.sort(key=lambda x: x[1], reverse=True)


#print results

print('\nElection Results\n------------------------------------')
print(f'Total Votes: {votes:.0f}\n------------------------------------')

for country_i in votes_by_country:
    print(f'{country_i[0]}: {( ( country_i[1]*100 ) / votes ):.3f}% ({country_i[1]})')
print('------------------------------------')
print(f'Winner: {votes_by_country[0][0]}')

print('------------------------------------')