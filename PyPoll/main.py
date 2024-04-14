# ## Instructions
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote

# import modules
import os   # facilitates calling files by formatting path name specific to os scrip[t is being ran on
import csv  # imports functions for writing to .csv files

# Set Paths
election_csv = os.path.join('Resources', 'election_data.csv')       # Path to initial data from resources folder
output_path = os.path.join('Analysis', 'Analysis_Results.txt')  # Path to write data to text file in analysis folder


# ---------------------------------------------------------------

# intialize variables    
candidateList = []      # Holds candidate names, matching index in voteCountList will hold candidate's votecount
voteCountList = []      # Holds candidate votecount, matching index in candidateList will hold candidate's votecount 
mostVotes = ["",0]      # name, voteCount
voteTotal = 0           # Holds total of all votes cast across candidates
spacer = "------------------------------------------"   # will use to separate output sections

with open(election_csv, 'r') as csvfile:  # Read in the CSV file

    csvreader = csv.reader(csvfile, delimiter=',')  # Split the data on commas
    header = next(csvreader)            # Grab Header row ([0] Ballot ID, [1] County, [2] Candidate)

    for row in csvreader:           # runs throgh csv file row by row, header has already been burned. will run through row 2 to end.
        voteTotal += 1              # Will increment as runs through rows. since every row has a unique vote will return a count of votes           
        currentCandidate = str(row[2])          # Grabs candidate name
        if currentCandidate in candidateList:   # checks if candidate name has already been added to list of candidates
            index = candidateList.index(currentCandidate)   # if candidate name exists, grab index of cnadidate
            voteCountList[index] += 1                       # increment votecount for candidate at index grabbed above
        else:                                               # If candidate is not already in candidate list
            candidateList.append(currentCandidate)          # Add candidate to list
            voteCountList.append(1)                         # add votecount at list with one vote


# -------------------------------------------------

# Saving output to list. Will call list when printing to terminal and printing to text file
output=[                  # First few lines are added when intializing output list
    ("Election Results"),                                                         
    (spacer),   
    (f'Total Votes: {voteTotal}'),
    (spacer)
    ]

for i in range(len(candidateList)):     # iterator to run through candidate list
    if voteCountList[i] > mostVotes[1]: # checking to see if candidate i has most votes
        mostVotes = [candidateList[i], voteCountList[i]]    # assigns candidate i to mostVotes if it has the most votes so far
    output.append(f'{candidateList[i]}: {format(voteCountList[i]/voteTotal,".3%")} ({voteCountList[i]})')    # adds candidate name, calculates % of vote, and adds final votecount
 
output.append(spacer)
output.append(f'Winner: {mostVotes[0]}')  #print out winner
output.append(spacer)   

for printLine in output: # iterator to print output to terminal
    print(printLine)    


# -----------------------------------------

textwriter = open(output_path, 'w') # Open/creating text file using "write" mode.

for textline in output:             # iterator to print output to text file
    textwriter.write(textline)      
    textwriter.write("\n")          # new line character needed after printing line above since .write does not move to next line on its own

textwriter.close()                  # closing textwriter