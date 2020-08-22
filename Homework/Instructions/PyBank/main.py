#Import dependencies
import os
import csv

#Define Variables
current_month_changes = 0
last_month_result = 0
profit_loss_total = 0
Total_Months = 0
Greatest_Increase = 0
Greatest_Decrease = 0
month_greatest_increase = " "
month_greatest_decrease = " "
total_change = 0
average_change = 0

# Path to collect data from the Resources folder
budget_data_location = os.path.join('.', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data_location) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    header = next(csvreader)
    #print(header)

    # Loop through the data
    for row in csvreader:
        if Total_Months != 0:
            current_month_changes = int(row[1]) - last_month_result

        # compare current month profit/loss to greatest increase/decrease
        if (current_month_changes > Greatest_Increase):
            Greatest_Increase = current_month_changes
            month_greatest_increase = row[0]
        elif (current_month_changes < Greatest_Decrease):
            Greatest_Decrease = current_month_changes
            month_greatest_decrease = row[0]
        
        #Total amount of profits/losses
        profit_loss_total = int(row[1]) + profit_loss_total 

        # total change calculation
        total_change = total_change + current_month_changes

        last_month_result = int(row[1]) 

        # The total number of months included in the dataset
        Total_Months += 1      
  
#The average of the changes in "Profit/Losses" over the entire period
average_change = round((total_change / (Total_Months -1)), 2)

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {Total_Months}")
print(f"Total:  ${profit_loss_total}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {month_greatest_increase} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits:  {month_greatest_decrease} (${Greatest_Decrease})")
    
# Export a text file with the results
budget_file = os.path.join("budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {Total_Months}\n")
    outfile.write(f"Total:  ${profit_loss_total}\n")
    outfile.write(f"Average Change:  ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits:  {month_greatest_increase} (${Greatest_Increase})\n")
    outfile.write(f"Greatest Decrease in Profits:  {month_greatest_decrease} (${Greatest_Decrease})\n")

    csvfile.close()
    