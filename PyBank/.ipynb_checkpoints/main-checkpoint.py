
import os
import csv

# Specify the file to write to
output_path = os.path.join( "Resources", "budget_data.csv")
total_months = 0

# Open the file using mode. Specify the variable to hold the contents
with open(output_path) as financial_data:

    # Initialize csv.reader 
    csvreader = csv.reader(financial_data, delimiter=',')

    # Write the first row (column headers)
    header = next(csvreader)

    for row in csvreader:
        month = row[0]
        profit = int(row[1])
        total_months = total_months + 1
        print(month)
        
#Find total number of months in budget data file


#Find the net total amount of Prft/losses over the period


#Find the average of the changes in the pfrt/losses

#Find the greatest increase in profits (date and amount) over entire period

#Find the greatest decrease in losses (date and amount) over the entire period