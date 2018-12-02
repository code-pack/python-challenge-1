
#NOTE_ for all readers.. 
### I decided to not only report votes by candidate, I also wanted to report Votes by STATE and also Votes by State by Candidate.

import os
import csv
import operator

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


def print_results(votes_dictionary):

    total_votes = 0.0

    for state in votes_dictionary:
        total_votes += sum(votes_dictionary[state].values())

    with open("Election_Results_Report.txt", "w") as text_file:

        print('\nElection Results\n------------------------------------')
        print('\nElection Results\n------------------------------------', file=text_file)
        print(f'Total Votes: {total_votes:.0f}\n------------------------------------')
        print(f'Total Votes: {total_votes:.0f}\n------------------------------------', file=text_file)

        my_tmp_dic ={} 
        for state in votes_dictionary:
            for candidate in votes_dictionary[state]:
                if candidate in my_tmp_dic:
                    my_tmp_dic[candidate] += votes_dictionary[state][candidate]
                else:
                    my_tmp_dic[candidate] = votes_dictionary[state][candidate]

        for candidate in my_tmp_dic:
            print(f'{candidate}: {((my_tmp_dic[candidate]*100)/total_votes):.3f}% ({my_tmp_dic[candidate]})')
            print(f'{candidate}: {((my_tmp_dic[candidate]*100)/total_votes):.3f}% ({my_tmp_dic[candidate]})', file=text_file)

        winner = max(my_tmp_dic.items(), key=operator.itemgetter(1))[0]

        print('------------------------------------')
        print('------------------------------------', file=text_file)
        print(f'Winner: {winner}')
        print(f'Winner: {winner}', file=text_file)
        print('------------------------------------')
        print('------------------------------------', file=text_file)

        print('\n\nVotes by State\n------------------------------------')
        print('\n\nVotes by State\n------------------------------------', file=text_file)

        #print votes by state

        top_state = next(iter(votes_dictionary))

        for state in votes_dictionary:
            state_votes = sum(votes_dictionary[state].values())
            top_state_votes = sum(votes_dictionary[top_state].values())
            print(f'{state}: {((state_votes*100)/total_votes):.3f}% ({state_votes})')
            print(f'{state}: {((state_votes*100)/total_votes):.3f}% ({state_votes})', file=text_file)
            if top_state_votes < state_votes:
                top_state = state

        print('------------------------------------')
        print('------------------------------------', file=text_file)
        print(f'State with most voters: {top_state}')
        print(f'State with most voters: {top_state}', file=text_file)
        print('------------------------------------')
        print('------------------------------------', file=text_file)

        tmp_votes = 0.0
        tmp_votes_b = 0.0

        print('\n\nVotes by State by Candidate\n------------------------------------')
        print('\n\nVotes by State by Candidate\n------------------------------------', file=text_file)
        for state in votes_dictionary:
            tmp_votes = sum(votes_dictionary[state].values())
            print(f'\n{state}: {(tmp_votes*100)/total_votes:.3f}% ({tmp_votes})')
            print(f'\n{state}: {(tmp_votes*100)/total_votes:.3f}% ({tmp_votes})', file=text_file)
            for candidate in votes_dictionary[state]:
                tmp_votes_b = votes_dictionary[state][candidate]
                print(f'---> {candidate}: {( ( tmp_votes_b*100 ) / tmp_votes ):.3f}% ({tmp_votes_b})')
                print(f'---> {candidate}: {( ( tmp_votes_b*100 ) / tmp_votes ):.3f}% ({tmp_votes_b})', file=text_file)

        print('\n------------------------------------')
        print('\n------------------------------------', file=text_file)

    return


def print_csv(my_dict):

    with open("Election_Results_Table.csv", "w") as my_csvfile:
        print('Candidate,State,Votes', file=my_csvfile)
        for states in my_dict:
            for candidates in my_dict[states]:
                print(f'{candidates},{states},{my_dict[states][candidates]}', file=my_csvfile)

    print('CSV file generated at: /Election_Results_Table.csv')

    return


##------------------------------------------------------##
## Main


# Path to collect data from the Resources folder
electiondataCSV = os.path.join('Resources/election_data.csv')

election_votes_dictionary = get_votes(electiondataCSV)

print_results(election_votes_dictionary)

#print results to a csv file
print_csv(election_votes_dictionary)