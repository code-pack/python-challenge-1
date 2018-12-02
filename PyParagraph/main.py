import os
import csv

# Path to collect data from the Resources folder
txt_to_analyze = os.path.join('Resources/test.txt')

words_count = 0
sentences_count = 0
letters_count = 0.0

# Read in the CSV file
with open(txt_to_analyze, 'r') as myfile:

    for line in myfile:
        #for word in line.replace('\n','').replace(',','').replace('-',' ').replace("'",' ').split():
        for word in line.split():
            print(word)

            words_count += 1
            
            letters_count += len(word)

            if '.' in word:
                sentences_count += 1


print('----------------------\nParagraph Analysis\n----------------------')
print(f'Approximate Word Count: {words_count}')
print(f'Approximate Sentence Count: {sentences_count}')
print(f'-> Letter Count: {letters_count}')
print(f'Average Letter Count: {letters_count/words_count}')
print(f'Average Sentence Length: {words_count/sentences_count}')

print('\nThe file has been read\n')