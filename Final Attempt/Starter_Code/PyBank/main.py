import os
import csv

budget_csv = os.path.join("/Users/ishi/Desktop/DATA Analytics/Python_Challenge/Final Attempt/Starter_Code/PyBank/Resources/budget_data.csv")
file_to_output = os.path.join("/Users/ishi/Desktop/DATA Analytics/Python_Challenge/Final Attempt/Starter_Code/PyBank/analysis", "budget_analysis.txt")

# set up empty lists too store data

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0


# read in the dataset snd store data in empty lists

with open(budget_csv,"r") as budget_data:
    reader = csv.reader(budget_data, delimiter  = ',')
    header = next(reader) #skip header row
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    for row in reader:
         # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


            
    
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
