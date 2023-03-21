import os
import csv

poll_csv = os.path.join("PyPoll/resources/election_data.csv")

total_votes = 0
candidates = {}
winner = ""
winning_votes = 0



with open(poll_csv, "r") as poll_data:
    poll_reader = csv.reader(poll_data, delimiter = ',')
    header = next(poll_reader)

    for row in poll_reader:
        total_votes += 1
        
        if row[2] not in candidates:
            candidates[row[2]] = 1

        else: 
            candidates[row[2]] += 1

for candidates, votes in candidates.items():
    percentage = round((votes/total_votes)*100, 3)

    if votes > winning_votes:
        winning_votes = votes
        winner = candidates



P_D = open('PyPoll/Analysis/Poll_Data.txt', "w")

P_D.writelines("") 
P_D.writelines("Election Results", )
P_D.write("\n")
P_D.writelines("----------------------------------")
P_D.write("\n")
P_D.writelines("Total Votes: " + str(total_votes))
P_D.write("\n")
P_D.writelines("----------------------------------")
P_D.write("\n")
P_D.writelines(f"{candidates}: {percentage}% ({votes})")
P_D.write("\n")
P_D.writelines("----------------------------------")
P_D.write("\n")
P_D.writelines(f"winner: {winner}")

P_D.close()


