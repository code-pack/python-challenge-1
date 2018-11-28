
import os
import csv

def get_votes(electiondataCSV):

    my_dict = {}
    # Read in the CSV file
    with open(electiondataCSV, 'r') as csvfile:

        # Split the data by commas
        csvreader = csv.reader(csvfile, delimiter=',')

        #Pass header
        csv_header = next(csvreader)
        
        # Loop through the data
        for row in csvreader:
            candidate = row[2]
            state = row[1]

            if state in my_dict:
                if candidate in my_dict[state]:
                    my_dict[state][candidate] += 1
                else:
                    my_dict[state][candidate] = 1
            else:
                my_dict[state] = {}
                my_dict[state][candidate] = 1

    return my_dict


## Main

# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')

votes_dictionary = get_votes(electiondataCSV)

total_votes = 0.0

for state in votes_dictionary:
    total_votes += sum(votes_dictionary[state].values())

print('\nElection Results\n------------------------------------')
print(f'Total Votes: {total_votes:.0f}\n------------------------------------')

tmp_votes = 0.0
my_tmp_dic ={} 
for state in votes_dictionary:
    for candidate in votes_dictionary[state]:
        if candidate in my_tmp_dic:
            my_tmp_dic[candidate] += votes_dictionary[state][candidate]
        else:
            my_tmp_dic[candidate] = votes_dictionary[state][candidate]

for candidate in my_tmp_dic:
    print(f'{candidate}: {((my_tmp_dic[candidate]*100)/total_votes):.3f}% ({my_tmp_dic[candidate]})')

print('------------------------------------')
print(f'Winner: falta')
print('------------------------------------')

print('\n\nVotes by Country\n------------------------------------')


#print votes by state
tmp_votes = 0.0

for state in votes_dictionary:
    tmp_votes = sum(votes_dictionary[state].values())
    print(f'{state}: {((tmp_votes*100)/total_votes):.3f}% ({tmp_votes})')

print('------------------------------------')
print(f'Country with most voters: falta')
print('------------------------------------')

tmp_votes = 0.0
tmp_votes_b = 0.0

print('\n\nVotes by Country by Candidate\n------------------------------------')
for state in votes_dictionary:
    tmp_votes = sum(votes_dictionary[state].values())
    print(f'\n{state}: {(tmp_votes*100)/total_votes:.3f}% ({tmp_votes})')
    for candidate in votes_dictionary[state]:
        tmp_votes_b = votes_dictionary[state][candidate]
        print(f'---> {candidate}: {( ( tmp_votes_b*100 ) / tmp_votes ):.3f}% ({tmp_votes_b})')

print('\n------------------------------------')



'''


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

'''