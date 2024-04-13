## Instructions
#  Your task is to create a Python script that analyzes the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

# import modules
import os   # facilitates calling files by formatting path name specific to os scrip[t is being ran on
import csv  # imports functions for writing to .csv files

# Set Paths
budget_csv = os.path.join('Resources', 'budget_data.csv')       # Path to initial data from resources folder
output_path = os.path.join('Analysis', 'Analysis_Results.txt')  # Path to write data to text file in analysis folder

with open(budget_csv, 'r') as csvfile:  # Read in the CSV file

    csvreader = csv.reader(csvfile, delimiter=',')  # Split the data on commas
   
    header = next(csvreader)        # Grab Header row
    firstRow = next(csvreader)      # Grab First row 
    netTotal = int(firstRow[1])     # Will Hold Running total of all profit/losses, intialized with first row's profit/loss
    lastMonth = netTotal            # Grabbing last month, will hold prior row's profit/loss so we can compare
    monthCount = 1                  # will increment on each run through rows to count number of months. Starting at one since we already burned the first row
    thisMonthChange = 0             # will hold change from last month to this month to compare to greatestInc and greatestDec
    totalChange = 0.00              # Will hold sum of all changes for final average change calculation on print
    greatestInc = [" ", 0]          # Holds greatest increase [Month name, amount of greatest increase]
    greatestDec = [" ", 0]          # holds greatest decrease [Month name, amount of greatest decrease]
    
    for row in csvreader:           # runs throgh csv file row by row, header and first row have already been burned. will run through row 3 to end.
       
        monthCount += 1             # Will increment as runs through rows. since every row has a unique month will return a count of months

        netTotal += int(row[1])     # adds amount at current row, column b to running netTotal

        thisMonthChange = int(row[1]) - lastMonth       # captures the change in profit/loss for this month from prior month
        totalChange += thisMonthChange                  # adds the monthly change to running total of all monthly changes, wil use to calculate average change
        lastMonth = int(row[1])                         # capture profit\loss for use in next iteration's comparison

        if thisMonthChange > greatestInc[1]:      # checks current month change against greatest increase
            greatestInc[0] = str(row[0])
            greatestInc[1] = thisMonthChange
        elif thisMonthChange < greatestDec[1]:    # checks current month change against greatest decrease
            greatestDec[0] = str(row[0])
            greatestDec[1] = thisMonthChange                
   
    output=[                   # Saving output to list. Will call list when printing to terminal and printing to text file
        ("Financial Analysis"),                                                         
        ("------------------------------------------"),                                 
        (f'Total Months: {monthCount}'),                                                
        (f"Total: ${netTotal}"),                                                        
        (f"Average Change: $"'{0:.2f}'.format(totalChange/(monthCount-1))),         # using .format to print out two decimal points           
        (f'Greatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})'),        
        (f'Greatest Decrease in Profits: {greatestDec[0]} (${greatestDec[1]})')     
        ]

    for printLine in output: # iterator to print output to terminal
        print(printLine)
  
textwriter = open(output_path, 'w')  # Open/creating text file using "write" mode.

for textline in output:             # iterator to print output to text file
    textwriter.write(textline)      
    textwriter.write("\n")          # new line character needed after printing line above since .write does not move to next line on its own

textwriter.close()  # closing textwriter