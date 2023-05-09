import csv

# Set the path for the CSV file
csvpath = 'Resources/budget_data.csv'

# Initialize variables
total_entries = 0
total_profit_loss = 0
previous_profit_loss = None
profit_loss_changes = []

# Open the CSV file and read the header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Increment the total number of entries
        total_entries += 1

        # Extract the profit/loss for the current row
        profit_loss = int(row[1])

        # Add the profit/loss to the total
        total_profit_loss += profit_loss

        # If this is not the first row, calculate the profit/loss change
        if previous_profit_loss is not None:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

        # Set the current profit/loss as the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average profit/loss change
average_profit_loss_change = sum(profit_loss_changes) / (total_entries - 1)

# Find the greatest increase in profits (date and amount)
max_increase = max(profit_loss_changes)
max_increase_date = None
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if int(row[1]) - previous_profit_loss == max_increase:
            max_increase_date = row[0]
            break

# Find the greatest decrease in losses (date and amount)
max_decrease = min(profit_loss_changes)
max_decrease_date = None
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if int(row[1]) - previous_profit_loss == max_decrease:
            max_decrease_date = row[0]
            break

# Format the results as a report
report = f"""
Financial Analysis
----------------------------
Total Months: {total_entries}
Total: ${total_profit_loss}
Average Change: ${average_profit_loss_change:.2f}
Greatest Increase in Profits: {max_increase_date} (${max_increase})
Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})
"""

# Print the report
print(report)

# Save the report to a text file
filepathtosave = 'analysis/analysis2.txt'
with open(filepathtosave, 'w') as f:
    f.write(report)

print(f"Analysis report saved to {filepathtosave}")