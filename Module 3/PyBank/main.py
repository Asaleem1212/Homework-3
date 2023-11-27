import csv

# Initialize variables
total_months = 0
net_total = 0
monthly_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Read in the CSV file
with open('PyBank\\Resources\\budget_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Read the header row
    header = next(csvreader)
    
    # Extract the first row to avoid appending to monthly_change list
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])
    
    # Loop through the rows in the csv
    for row in csvreader:
        # Track the total
        total_months += 1
        net_total += int(row[1])
        
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        monthly_change.append(net_change)
        
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
# Calculate the Average Net Change
average_change = sum(monthly_change) / len(monthly_change)

# Generate output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output to terminal
print(output)

# Export the results to a text file
with open('PyBank\\financial_analysis.txt', 'w') as textfile:
    textfile.write(output)

# Return the path to the output file for download
output_file_path = 'PyBank/financial_analysis.txt'
output_file_path