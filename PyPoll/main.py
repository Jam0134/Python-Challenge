
import os
import csv

# Specify the file to write to
output_path = os.path.join( "election_data.csv")
total_votes = 0.0
candidates_received_votes =[]
Percent_each_won = 0.0
total_votes_each_won = 0.0
winner = ""



# Open the file using mode. Specify the variable to hold the contents
with open("election_data.csv") as election_hw:

    # Initialize csv.reader 
    csvreader = csv.reader(election_hw, delimiter=',')

    print(csvreader)

    header = next(csvreader)

#The total number of votes cast
    for row in csvreader:
        total_votes=total_votes+1 
        #candidates_received_votes

# A complete list of candidates who received votes
        if (row[2] not in candidates_received_votes)
            candidates_received_votes.append(row[2])

  
#print(candidates_received_votes)
# The percentage of votes each candidate won

def print_percentages(election)
    voter_id = int(election[0])
    county = str(election[1])
    candidate = str(election[2])


 # The total number of votes each candidate won

    total_cand_votes = total_cand_votes


# Print totals

    print("total_votes", total_votes)
    print("candidates_received_votes",candidates_received_votes)
    print("Percent_each_won")
    print("total_votes_each_won")
    print("winner")


# writing to csv file  
election_output = "my_election_output.txt"

with open(election_output, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    writer = csv.writer(my_election_output) 
        
    # writing the data rows  
    writer.writerows(myData)