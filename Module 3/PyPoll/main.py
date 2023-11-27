# Importing Libraries
import csv
from collections import Counter

# Initialize a Counter object to hold the votes for each candidate
votes = Counter()

# Initialize a variable to hold the total number of votes
total_votes = 0

# Read in the CSV file
with open('PyPoll//Resources//election_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Read the header row
    header = next(csvreader)
    
    # Loop through the rows in the csv
    for row in csvreader:
        # Increment the total votes
        total_votes += 1
        # Count the votes for each candidate
        votes[row[2]] += 1

# Determine the winner
winner = max(votes, key=votes.get)

# Create a list to store the formatted candidate results
candidate_results = [
    f"{candidate}: {votes[candidate]/total_votes:.3%} ({votes[candidate]})"
    for candidate in votes
]

# Format the overall results
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"\n".join(candidate_results) +
    f"\n-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the output to terminal
print(output)

# Export the results to a text file
with open('PyPoll/election_results.txt', 'w') as textfile:
    textfile.write(output)

# Return the path to the output file for download
output_file_path = 'PyPoll/election_results.txt'
output_file_path
