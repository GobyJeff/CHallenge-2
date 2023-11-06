import csv
import os

csv_file_path = os.path.join("Resources", "election_data.csv")
output_file_path = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidates = []
candidate_votes = {}


with open(csv_file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  

    for row in csvreader:
    
        total_votes += 1

        candidate_name = row[2]

    
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

    
        candidate_votes[candidate_name] += 1

winning_candidate = ""
winning_votes = 0

results = "Election Results\n" + "-" * 25 + "\n"

for candidate in candidates:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

results += "-" * 25 + "\n"
results += f"Winner: {winning_candidate}\n" + "-" * 25 + "\n"
print(results)

with open(output_file_path, "w") as output_file:
    output_file.write(results)

print("Analysis saved to PyPoll_analysis.txt.")
