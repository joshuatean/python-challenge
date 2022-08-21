
import os
import csv
#import sys

#Path
os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join('Resources','budget_data.csv')

#Define
def financial_analysis(record):

    #Total
    total = sum(pl)

    #Find the difference between each profit/loss record
    difference = [pl[i+1]-pl[i] for i in range(len(pl)-1)]
    total_difference = sum(difference)

    #Find the average change
    average_change = total_difference/len(difference)
    format_average_change = "{:.2f}".format(average_change)

    #Total months
    total_months = len(date)
    
    #Greatest increase in profit
    update_date_list = date.pop(0)  #To remove first entry in the date list
    gdifference = dict.fromkeys(date)
    gdifference.update(zip(date,difference))

    #print(gdifference)
    max_increase = max(difference)
    max_decrease = min(difference)
    
    max_month = max(gdifference, key=gdifference.get)
    min_month = min(gdifference, key=gdifference.get)
    
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total months: {str(total_months)}")
    print(f"Total: ${str(total)}")
    print(f"Average Change: ${str(format_average_change)}")
    print(f"Greatest Increase in Profits: {str(max_month)} (${str(max_increase)})")
    print(f"Greatest Decrease in Profits: {str(min_month)} (${str(max_decrease)})")
    
    #os.chdir(os.path.dirname(__file__))
    #analysis_txt = os.path.join('Analysis','analysis.txt')
    #with open(analysis_txt,'w') as outfile:
    #    print(f"Financial Analysis". file=outfile)

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    reader = csv.DictReader(csvfile)

    #header = next(csvreader)
    date = []
    pl = []
    # Loop through the data
    date_col = {'Date': []}
    num_col = {'Profit/Losses': []}
    for record in reader:
        date.append(record['Date'])
        pl.append(int(record['Profit/Losses']))
    
    financial_analysis(record)
    