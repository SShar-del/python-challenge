import os
import csv

# Path to collect data from the Resources folder

pypoll_csv = os.path.join('Resources', 'election_data.csv')

# Lists to store data

voter_ids =[]
county =[]
candidates =[]

# Define the function to analyze the election data and print the poll analysis

def poll_analysis(voter_ids,county,candidates):


#Calculate the total number of votes cast

	total_votes_count = len(voter_ids)

	
#Calculate the total number of votes each candidate won- create a dictionary with unique candidate names as key and count of voter ids as values
	
	unique_candidate = {}

	for idx in range (len(candidates)):
		if candidates[idx] in unique_candidate:
			unique_candidate[candidates[idx]] = unique_candidate[candidates[idx]] + 1
		else:
			unique_candidate[candidates[idx]] = 1

	
#Calculate the percentage of votes each candidate won
	
	Data=[]
	for candidate in unique_candidate.keys():
		line=f'{candidate} : {unique_candidate[candidate]*100/total_votes_count:.3f}% ({unique_candidate[candidate]})'
		Data.append(line + '\n ')
		

#Calculate the winner of the election based on popular vote

	max_votes= max(list(unique_candidate.values()))
	for winner in unique_candidate.keys():
		if unique_candidate[winner]== max_votes:
			line_end= f"Winner : {winner}"
			

# Print the analysis to the terminal 


	print(f"Election Results \n {'-'*30} \n")
	print(f"Total Votes:{total_votes_count}\n {'-'*30} \n")
	for line in Data:
		print(line)
	print('-'*30 +'\n '+line_end + '\n '+'-'*30 )

# Specify the output text file to write to 

	output_path = os.path.join('analysis', 'analysis_output.txt')

# Create a variable to hold the output data title and total votes result
    
	L1 = f" Election Results \n {'-'*30} \n Total Votes:{total_votes_count} \n {'-'*30} \n "
    
# Open the file in "write" mode and write all lines of output (stored in L1, Data, and line_end) in the file and close file when done writing

	with open(output_path, 'w') as file:
		file.write(L1)
		file.writelines(Data)
		file.write('-'*30 +'\n '+line_end + '\n '+'-'*30 )
    
	file.close()


# Read in the CSV file

with open(pypoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header
    header = next(csvreader)


#for row in csvreader: to read the file and load the data in previously defined lists for processing

    for row in csvreader:
    	voter_ids.append(row[0])
    	county.append(row[1])
    	candidates.append(row[2])

# Call the function

poll_analysis(voter_ids, county,candidates)  