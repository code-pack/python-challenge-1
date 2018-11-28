
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
            tmp_candcountr.append((row[1],row[2])) #sería mejor almacenar

        candcountr = set(tmp_candcountr)
        
        tmp_count = 0 #count votes for each candcountry

        tmp_candcountr_2 = [] #this will store a list of candcountr

        ## this is not an optimal approach because I'm reading the file four times.. 
        for candcountryname in candcountr:

            for row in tmp_candcountr:

                if row[0] == candcountryname[0] and row[1] == candcountryname[1]:
                    tmp_count += 1

            tmp_candcountr_2.append([candcountryname[1],candcountryname[0],tmp_count])

            tmp_count = 0

    tmp_candcountr_2.sort(key=lambda x: x[2], reverse=True)

    return tmp_candcountr_2


def unique_list_ordered(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]  # comprehension list
    #Note that this relies on the fact that set.add() returns None.



## Main

# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')

votes_by_candcountry = get_votes(electiondataCSV)

total_votes = 0.0
candidate_list = []
country_list = []

for rows in votes_by_candcountry:
    total_votes += rows[2]

    candidate_list.append(rows[0])
    country_list.append(rows[1])

#count votes by candidate
unique_candidates = unique_list_ordered(candidate_list)
unique_candidates_votes = []
for un_cand in unique_candidates:
    unique_candidates_votes.append([un_cand,0])

for name in unique_candidates_votes:
    for votess in votes_by_candcountry:
        if name[0] == votess[0]:
            name[1] += votess[2]

#count votes by countries
unique_countries = unique_list_ordered(country_list)
unique_countries_votes = []
for un_coun in unique_countries:
    unique_countries_votes.append([un_coun,0])

for name in unique_countries_votes:
    for votess in votes_by_candcountry:
        if name[0] == votess[1]:
            name[1] += votess[2]



#print results to screen

print('\nElection Results\n------------------------------------')
print(f'Total Votes: {total_votes:.0f}\n------------------------------------')

for candidate_i in unique_candidates_votes:
    print(f'{candidate_i[0]}: {( ( candidate_i[1]*100 ) / total_votes ):.3f}% ({candidate_i[1]})')
print('------------------------------------')
print(f'Winner: {unique_candidates_votes[0][0]}')

print('------------------------------------')

print('\n\nVotes by Country\n------------------------------------')

for country_i in unique_countries_votes:
    print(f'{country_i[0]}: {( ( country_i[1]*100 ) / total_votes ):.3f}% ({country_i[1]})')

print('------------------------------------')
print(f'Country with most voters: {unique_countries_votes[0][0]}')

print('------------------------------------')

print('\n\nVotes by Country by Candidate\n------------------------------------')
for country_i in unique_countries_votes:
    print(f'\n{country_i[0]}: {( ( country_i[1]*100 ) / total_votes ):.3f}% ({country_i[1]})')
    for candcountry_i in votes_by_candcountry:
        if country_i[0] == candcountry_i[1] :
            print(f'---> {candcountry_i[0]}: {( ( candcountry_i[2]*100 ) / country_i[1] ):.3f}% ({candcountry_i[2]})')

print('\n------------------------------------')


#save results to a file
with open("Election_Results_Report.txt", "w") as text_file:
    print('\nElection Results\n------------------------------------', file=text_file)
    print(f'Total Votes: {total_votes:.0f}\n------------------------------------', file=text_file)

    for candidate_i in unique_candidates_votes:
        print(f'{candidate_i[0]}: {( ( candidate_i[1]*100 ) / total_votes ):.3f}% ({candidate_i[1]})', file=text_file)
    print('------------------------------------', file=text_file)
    print(f'Winner: {unique_candidates_votes[0][0]}', file=text_file)

    print('------------------------------------', file=text_file)

    print('\n\nVotes by Country\n------------------------------------', file=text_file)

    for country_i in unique_countries_votes:
        print(f'{country_i[0]}: {( ( country_i[1]*100 ) / total_votes ):.3f}% ({country_i[1]})', file=text_file)

    print('------------------------------------', file=text_file)
    print(f'Country with most voters: {unique_countries_votes[0][0]}', file=text_file)

    print('------------------------------------', file=text_file)

    print('\n\nVotes by Country by Candidate\n------------------------------------', file=text_file)
    for country_i in unique_countries_votes:
        print(f'\n{country_i[0]}: {( ( country_i[1]*100 ) / total_votes ):.3f}% ({country_i[1]})', file=text_file)
        for candcountry_i in votes_by_candcountry:
            if country_i[0] == candcountry_i[1] :
                print(f'---> {candcountry_i[0]}: {( ( candcountry_i[2]*100 ) / country_i[1] ):.3f}% ({candcountry_i[2]})', file=text_file)

    print('\n------------------------------------', file=text_file)

#print results to a csv file
with open("Election_Results_Table.csv", "w") as my_csvfile:
    print('Candidate,Country,Votes', file=my_csvfile)
    for candcountry_i in votes_by_candcountry:
        print(f'{candcountry_i[0]},{candcountry_i[1]},{candcountry_i[2]}', file=my_csvfile)

print('CSV file generated at: /Election_Results_Table.csv')