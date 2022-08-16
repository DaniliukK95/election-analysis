#the data we need to retrieve
#add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("resources" , "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1a) the total number of votes cast. initialize a total vote counter
total_votes = 0

#2a) candidate options
candidate_options = []

#3a) declare the empty dictionary
candidate_votes = {}

#5a Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read the header row in the CSV file.
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #1b) add to to the total vote count
        total_votes += 1

        #2b) print the candidate name from each row
        candidate_name = row[2]

        #2c) If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            #2d) Add the candidate name to the list of candidates.
            candidate_options.append(candidate_name)

            #3b) begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        #3c) Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.       
#4a. Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    #4b. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    #4c. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 5b Determine winning vote count and candidate
    # 5b. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
       
        # 5c. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
       
        # 5d. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    #5e To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#5f code to print out the winning candidate summary.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    #4d) Print the candidate name and percentage of votes.
    ##print(f"{candidate_name}: received {vote_percentage}% of the vote.") 

#1c) print the total votes
##print("total votes:", total_votes)

#2e) print the candidate list
##print("candidate list:", candidate_options)

#3d) print the candidate vote dictionary
##print("candidate vote count:", candidate_votes)

