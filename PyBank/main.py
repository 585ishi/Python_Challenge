import os
import csv

budget_csv = os.path.join("PyBank/resources/budget_data.csv")

#set up empty lists too store data

dates = []
profit = []
loss = []
profit_changes = []
loss_changes = []
total = []


#read in the dataset snd store data in empty lists

with open(budget_csv,"r") as budget_data:
    reader = csv.reader(budget_data, delimiter  = ',')
    header = next(reader) #skip header row

    for row in reader:
        dates.append(row[0])
        profit_loss = int(row[1])

        if profit_loss > 0:
            profit.append(profit_loss)
            total.append(profit_loss)
            


        if profit_loss < 0:
            loss.append(profit_loss)
            total.append(profit_loss)
            
    
#calculate teh total number of months
num_months = len(dates)

#calculate the net total amount of profits and losses over the time perid
net_profit = sum(profit)
net_loss = sum(loss)
net_total = net_profit + net_loss

#calculate the changes in profits
#calculate the changes in losses
#calculate the total changes
profit_changes = [profit[i+1]-profit[i] for i in range(len(profit)-1)]
loss_changes = [loss[i+1]-loss[i] for i in range(len(loss)-1)]
total_changes = [total[i+1]-total[i] for i in range(len(total)-1)]

#calculate the average changes
avg_changes = round(sum(total_changes)/len(total_changes), 2)

#calculate the maximum profit increase and the corresponding date
max_profit = max(total_changes)
max_total_date = total_changes.index(max(total_changes)) + 1
max_profit_date = dates[max_total_date]

#calculate the greatest decrease in profits and the corresponding date
max_loss = min(total_changes)
min_total_date = total_changes.index(min(total_changes)) + 1
max_loss_date = dates[min_total_date]


B_D = open('PyBank/Analysis/Budget_Data.txt', "w")

B_D.writelines("") 
B_D.writelines("financial Analysis", )
B_D.write("\n")
B_D.writelines("---------------------------------")
B_D.write("\n")
B_D.writelines("Total Months: " + str(num_months))
B_D.write("\n")
B_D.writelines(f"Total: ${net_total}")
B_D.write("\n")
B_D.writelines("Average Change: $" + str(avg_changes))
B_D.write("\n")
B_D.writelines(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})")
B_D.write("\n")
B_D.writelines(f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})")

B_D.close()