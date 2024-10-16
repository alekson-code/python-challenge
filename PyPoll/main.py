# Import dependencies
import os, csv

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Declare Variables 
total_votes = 0 
Charle_CS_votes = 0
Diana_DeGette_votes = 0
Raymon_AD_votes = 0

# Open csv in default read mode with context manager
with open(file_to_load) as election_data:

    # Store data under the csvreader variable
    csvreader = csv.reader(election_data,delimiter=",")  #data collection

    # Skip the header row
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # With three candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            Charle_CS_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_AD_votes +=1
        

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charle_CS_votes, Diana_DeGette_votes, Raymon_AD_votes,]

# We zip candidates together, the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
Charle_CS_percent = (Charle_CS_votes/total_votes) *100
Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100
Raymon_AD_percent = (Raymon_AD_votes/total_votes)* 100


# Print the total vote count (to terminal)
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charle_CS_percent:.3f}% ({Charle_CS_votes})")
print(f"Diana DeGett: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_AD_percent:.3f}% ({Raymon_AD_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

 # Write the total vote count to the text file
with open(file_to_output,"w") as file:

    # Write methods to print to Elections_Results_Summary  into the file election_analysis.txt
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charle_CS_percent:.3f}% ({Charle_CS_votes})")
    file.write("\n")
    file.write(f"Diana DeGett: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_AD_percent:.3f}% ({Raymon_AD_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")     #Takes the winner from the dictionary and zip class 
    # - key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get), .get is a method
    file.write("\n")
    file.write(f"----------------------------")