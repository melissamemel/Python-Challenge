#Import dependencies
import os
import csv

#Define variables
candidate_list = []
candidate_name = []
candidate_winner = []
total_votes = 0
candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]

# Path to collect data from the Resources folder
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Read in the csv file
with open(csvpath) as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csv_reader)

     # Loop through the data
    for row in csv_reader:
        total_votes += 1
        candidate_list.append(str(row[2]))
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] += 1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1

    # % calculation of total vote for each candidate
    candidate_vote_percent[0] = round(100 * (candidate_vote[0] / total_votes), 4)
    candidate_vote_percent[1] = round(100 * (candidate_vote[1] / total_votes), 4)
    candidate_vote_percent[2] = round(100 * (candidate_vote[2] / total_votes), 4)
    candidate_vote_percent[3] = round(100 * (candidate_vote[3] / total_votes), 4)

    # Find the winner 
    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[3]

# print the report to the terminal screen
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
print("-----------------------------")
print(f"Winner: {candidate_winner}")
print("-----------------------------")

# Export a text file with the results
election_file = os.path.join("election_data.txt")
with open(election_file, 'w') as outfile:

    outfile.write("Election Results\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})\n")
    outfile.write(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})\n")
    outfile.write(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})\n")
    outfile.write(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Winner: {candidate_winner}\n")
    outfile.write("-----------------------------\n")

    csvfile.close()
