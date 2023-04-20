import os
import csv

poll_csv = os.path.join("PyPoll/resources/election_data.csv")

# Define Variables
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0


# open the csv File using the correct path and read data
with open(poll_csv, "r") as poll_data:
    poll_reader = csv.reader(poll_data, delimiter = ',')
    header = next(poll_reader) #skip header

    # Increment Total votes
    for row in poll_reader:
        total_votes += 1
        
        # Check if candidate is already in dictioonary, if not add
        # Add the total votes per candidate in the dictionary, for every time their name appears
        if row[2] not in candidates:
            candidates[row[2]] = 1

        else: 
            candidates[row[2]] += 1

# calculate total number of votes and every candidates Percent of vote
# print candidate name, percent of vote and their total number votes
x = {}
for candidates, votes in candidates.items():
    percentage = round((votes/total_votes)*100, 3)
    
    
    x.append(print("{candidates}: {percentage}% ({votes}"))


    # check if which candidate has the highest votes
#     if votes > winning_votes:
#         winning_votes = votes
#         winner = candidates


# # Export the result as a text file

# P_D = open('PyPoll/Analysis/Poll_Data.txt', "w")

# P_D.writelines("") 
# P_D.writelines("Election Results", )
# P_D.write("\n")
# P_D.writelines("----------------------------------")
# P_D.write("\n")
# P_D.writelines("Total Votes: " + str(total_votes))
# P_D.write("\n")
# P_D.writelines("----------------------------------")
# P_D.write("\n")
# P_D.writelines(x)
# P_D.write("\n")
# P_D.writelines("----------------------------------")
# P_D.write("\n")
# P_D.writelines(f"winner: {winner}  {votes}")

# P_D.close()


