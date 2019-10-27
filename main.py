# access csv budget_data csv
import os
import csv
from collection import defaultdict
csvpath = os.path.join('python-challenge.', 'election_data.csv')

with open(csvpath,'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Create lists to input the votes and candidates 
    
    total_votes = 0
    candidates = set()
    votes_num= []
    ballots =[]
    
    #Iterate to search for number of vote and candidates with votes 
    for row in csvreader:
        total_votes+= 1
        candidates.add(row[2])
        votes_num.append()
        if ballot.get(int(row[2]))is None:
            ballots(int(row[2])) = 0
        else:
            ballots(row[2])+= 1
print(total_votes)
print(candidates)
print(ballots)
#Printing percent per candidate
for candidate in candidates:
    candidate_vote = ballots.get(candidate)
    percent = f"{(candidate_votes / total_votes*100)}"
    print(f'{candidate} {percent}% {ballots[candidate]}')
#Printing winner
print(f"Winner:{max(ballot2, key=ballots.get)}")
#Export as a txt file 
with open(f"{dir_path}/results.txt","w") as f:
f.write(f"Election Results\n")
f.write(f"--------------------------\n")
f.write("Total Votes:{(total_votes}\n")
    for candidate in candidates:
    candidate_vote = ballots.get(candidate)
    percent = (f"{ballots.get(candidate/total_votes*100:)})
    print(f'{candidate}%{percent}'%{ballots[candidates]})')
f.write(f"Winner: {max(ballots, key=ballots.get)}\n")

