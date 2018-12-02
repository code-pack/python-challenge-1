import os
import csv

#import the State Abbreviations
from Resources.us_state_abbrev import *

# Path to collect data from the Resources folder
employeedataCSV = os.path.join('Resources/employee_data.csv')
# Path to write the new format
newemployeedatacsv = os.path.join('new_employee_data.csv')


# Read in the CSV file
with open(employeedataCSV, 'r') as csvfile:

    # Split the data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Pass header
    csv_header = next(csvreader)

    #open the Output file
    with open(newemployeedatacsv, 'w') as csv_output:

        employee_writer = csv.writer(csv_output, delimiter=',')

        #write the new header
        employee_writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

        
        # Loop through the data
        for row in csvreader:
            #store locally the origin variables
            emp_id = row[0]
            fullname = row[1]
            dob = row[2]
            ssn = row[3]
            state = row[4]

            #split the name by the last space of the Full name -- this is to include names with 2 names
            split_index = fullname.rfind(' ') 
            firstname = fullname[0:split_index]
            lastname = fullname[split_index+1:]

            #formatting the date  yyyy-mm-dd  into mm/dd/yyyy
            tmp_dob =  dob.split('-')
            newdate = tmp_dob[1] + '/' + tmp_dob[2] + '/' + tmp_dob[0]

            #encripting the Social Security Number
            enc_ssn = '***-**-' + ssn[-4:]

            #Converting the state names into their abbreviations
            new_state = us_state_abbrev[state]

            #writing the row to the OutPut file
            employee_writer.writerow([emp_id,firstname,lastname,newdate,enc_ssn,new_state])


print('The new csv has been generated: /new_employee_data.csv')

