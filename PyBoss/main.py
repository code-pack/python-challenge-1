import os
import csv

from Resources.us_state_abbrev import *

# Path to collect data from the Resources folder
employeedataCSV = os.path.join('Resources/employee_data.csv')

newemployeedatacsv = os.path.join('new_employee_data.csv')


# Read in the CSV file
with open(employeedataCSV, 'r') as csvfile:

    # Split the data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    with open(newemployeedatacsv, 'w') as csv_output:


        employee_writer = csv.writer(csv_output, delimiter=',')

        #Pass header
        csv_header = next(csvreader)

        employee_writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

        
        # Loop through the data
        for row in csvreader:
            emp_id = row[0]
            fullname = row[1]
            dob = row[2]
            ssn = row[3]
            state = row[4]

            split_index = fullname.rfind(' ') 
            firstname = fullname[0:split_index]
            lastname = fullname[split_index+1:]

            newdate =  dob[5:7] + '/' + dob[8:] + '/' + dob[0:4]

            enc_ssn = '***-**-' + ssn[-4:]

            new_state = us_state_abbrev[state]

            employee_writer.writerow([emp_id,firstname,lastname,newdate,enc_ssn,new_state])


print('The new csv has been generated: /new_employee_data.csv')

