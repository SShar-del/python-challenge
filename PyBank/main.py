import os
import csv

# Path to collect data from the Resources folder

pybank_csv = os.path.join('Resources', 'budget_data.csv')


# Lists to store data

months = []
profit_loss = []
profit_loss_change = []


# Define the function to analyze the financial data

def bank_analysis(months,profit_loss):

#Calculate the total number of months included in the dataset
      
    total_month_count = len(months) 
            
    
#Calculate the net total amount of "Profit/Losses" over the entire period
   
    
    net_profit_loss = sum(profit_loss)
    

# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
    
    for i in range(1, total_month_count):

        plchange = int(profit_loss[i]) - int(profit_loss[i-1])
        profit_loss_change.append(plchange)
        
    total_plchange = sum(profit_loss_change)
             
    avg_change= total_plchange/len(profit_loss_change)
    
 
# Calculate the greatest increase in profits (date and amount) over the entire period

    max_profit = max(profit_loss_change)
    max_profit_month = months[profit_loss_change.index(max_profit)+1]
    
 
# Calculate the greatest decrease in profits (date and amount) over the entire period
    
    min_profit = min(profit_loss_change)
    min_profit_month = months[profit_loss_change.index(min_profit)+1]
   

# Print the financial analysis to the terminal 

    print(f"Financial Analysis \n {'-'*40} \n" )
    print(f"Total Months:{total_month_count}")
    print(f"Total Profit and Loss: ${net_profit_loss}")
    print(f"Average Change ${avg_change:.2f}")
    print(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})')
    print(f'Greatest Decrease in Profits: {min_profit_month} (${min_profit})')


# Specify the output file to write to

    output_path = os.path.join('analysis', 'analysis-output.txt')


# Create a variable to hold the output data title and all the previously calculated results
    
    L =  f" Financial Analysis \n {'-'*40} \n Total Months:{total_month_count} \n Total Profit and Loss: ${net_profit_loss} \n Average Change ${avg_change:.2f} \n Greatest Increase in Profits: {max_profit_month} $({max_profit}) \n Greatest Decrease in Profits: {min_profit_month} $({min_profit})"

    
# Open the file in "write" mode and write all lines of output (stored in L) in the output file and close file when done writing

    with open(output_path, 'w') as file:
        file.write(L)

    file.close()


# Read in the CSV file

with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

     # Read the header
    header = next(csvreader)


#for row in csvreader:to read the file and load the data in previously defined lists for processing

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

# Call the function

bank_analysis(months,profit_loss)  