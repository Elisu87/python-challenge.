# access csv budget_data csv
import os
import csv
csvpath = os.path.join('python-challenge.','budget_data.csv')
with open(csvpath,'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Create lists to store date input & profit and lost input
    months = []
    amount = []
    for row in csvreader:
        months.append(row[0])
        amount.append(int(row[1]))
# Print number of months within the database and amount over entire period
print(len(months))
print(len(amount))
#Calculate total months and total value 
print(f'Total Months:((len(amount))')   
total = sum(amount)
print(f'Total:[total]')
# Calculating the avarage in changes 
changes = []
for index in range(len(amount)-1):
    changes.append(amount[index+1]-amount[index])
    print(sum(changes)/len(changes))
    avg_changes = sum(changes)/len(changes)
    print(f'Average Change:$[avg_changes]')
#Calculating Greatest increase in profit and Greatest decrease
    print(f'Greatest Increase in Profits: (max(changes))')
    print(f'Greatest Decrease in Profits: ((max(changes))')
# Export text file with results
with open(f"{PyBank}/analysis.txt","w") as f:
    f.write(f"Finanancial Analysis\n")
    f.write(f"--------------------------\n")
    f.write(f"Total Months:{len(amount)})\n")
    f.write(f"Total:{total}\n")
    f.write(f"Average Change:${avg_changes}\n")
    f.write(f"Greatest Increase in Profits:{max(changes)})\n")
    f.write(f"Greatest Decrease in Profits: {max(changes)})\n")
