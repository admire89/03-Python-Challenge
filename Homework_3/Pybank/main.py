#Pybank 
# modules 
import os 
import csv 

# lists for data 
profit = []
monthly_change = []
date=[]

# set the path for csv file 
budget_csv_path= os.path.join("Resources", "budget_data.csv")

#variables 
month_count= 0
total_profit = 0
total_profit_change = 0
month_start = 0

# open the file 
with open(budget_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader) #skip the header 

# for loop to read the file all at once 
    for row in csvreader:
        # count the mmonths 
        month_count = month_count + 1
        # store all of the date data to the date list 
        date.append(row[0])
        # store all of the profit data to the profit list 
        profit.append(row[1])
        # caculate the total profit
        total_profit = total_profit + int(row[1])
        
        # Calculate the month profit changes 
        if month_start ==0:
            month_start = int(row[1])
        month_end = int(row[1])
        monthly_change_profit = month_end - month_start 
        monthly_change.append(monthly_change_profit)
        total_profit_change += monthly_change_profit
        month_start = month_end
        # greatest profit change 
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
        # to return the date that match with the graetest increase and decraese in profit
        increase_date = date[monthly_change.index(greatest_increase)]
        decrease_date = date[monthly_change.index(greatest_decrease)]

#Average month_change. Months -1 since we compare the 85 changes between 86 months.
average_month_change = round((total_profit_change/(int(month_count)-1)),2)

#Terminal
# Display all of the results on Terminal 
print ("```text````")
print ("Finacial Analysis")
print ("----------------------------")
print ("Total months: " + str(month_count))    
print ("Total: $" + str(total_profit))    
print( "Average Change: " + str(average_month_change))
print(f"Greatest Increase in Profit: {str(increase_date)} (${str(greatest_increase)})") 
print(f"Greatest Decrease in Profit: {str(decrease_date)} (${str(greatest_decrease)})")
print("````")

#Output file
#set the path for the outpul fie 
output_path = os.path.join("Analysis", "output.csv")

# open the output file,  then write the analysis in the output file 
with open (output_path,"w") as outputfile:
    csvwriter = csv.writer(outputfile)
    csvwriter.writerow(["```text````"])
    csvwriter.writerow(["Finacial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total months: " + str(month_count)])
    csvwriter.writerow (["Total: $" + str(total_profit)])
    csvwriter.writerow( ["Average Change: " + str(average_month_change)])
    csvwriter.writerow([f"Greatest Increase in Profit: {str(increase_date)}  (${str(greatest_increase)})"] )
    csvwriter.writerow([f"Greatest Decrease in Profit: {str(decrease_date)} (${str(greatest_decrease)})"])
    csvwriter.writerow(["````"])