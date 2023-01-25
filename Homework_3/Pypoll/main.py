# modules 
import os 
import csv

#Variables 
total_votes = 0
vote_count = 0 

#list of data 
all_votes =[]
candidates_name_list = []
votes_count_list= []
votes_percent_list = []

# define function to print out the following line 
def skip_row():
    print("-------------------------")

# open and red file
csvpath= os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader) #skip the header 

    # for loop go through the entire csv file 
    for row in csvreader:
       #counts the votes 
        total_votes= total_votes + 1 
        # to all all of the votes to the vote list 
        all_votes.append(row[2])
   
    # find candidate names and their vote count and percentages in the poll. 
    for name in all_votes:
        # This will only happen when the name is not in the candidate name list
        if name not in set(candidates_name_list): 
            # add the candidate name in the list 
            candidates_name_list.append(name)
            # count how manny votes of this candidtae in all votes list, then the count to the list 
            vote_count = all_votes.count(name)
            votes_count_list.append(vote_count) 
            # caculate teh percentage of the candidate vote count, then return to the list 
            vote_percentage = round(100 * vote_count/total_votes,3) # round the percentage to 3 decimal place values 
            votes_percent_list.append(vote_percentage)
               
#Terminal     
# Display all of the results on Terminal     
print("```text")
print("Election Results")
skip_row()
print("Total Votes: " + str(total_votes))
skip_row()
# print all the candiate names and their votes coutn and percentage at once using loop
for i in range(len(candidates_name_list)):
    print(f"{candidates_name_list[i]} : {votes_percent_list[i]}% ({votes_count_list[i]})")
skip_row()    
# find the winner 
for j in range(len(votes_count_list)):
    if votes_count_list[j] == max(votes_count_list):
        print("The winner is: " + str(candidates_name_list[j]))
skip_row()
print("``````")

#Output file 
#open the path and write the result in the output file 
output_path = os.path.join("Analysis", "output.csv")
with open(output_path,"w") as output_file:
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(["```text"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes: " + str(total_votes)])
    csvwriter.writerow(["-------------------------"])
    for x in range(len(candidates_name_list)):
        csvwriter.writerow([f"{candidates_name_list[x]} : {votes_percent_list[x]}% ({votes_count_list[x]})"])
    csvwriter.writerow(["-------------------------"])
    for y in range(len(votes_count_list)):
        if votes_count_list[y] == max(votes_count_list):
            csvwriter.writerow(["The winner is: " + str(candidates_name_list[y])])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["``````"])
    
