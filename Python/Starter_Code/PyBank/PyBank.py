import csv
import os



file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")


total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_changes = []
months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    for row in csvreader:
        
        total_months += 1

        
        total_profit_loss += int(row[1])

        
        change = int(row[1]) - previous_profit_loss
        profit_changes.append(change)
        months.append(row[0])

        
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

       
        previous_profit_loss = int(row[1])


average_change = sum(profit_changes) / len(profit_changes)


results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)


print(results)


with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

print("Analysis saved to PyBank_analysis.txt.")
