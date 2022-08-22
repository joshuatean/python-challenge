import os
import csv

#Path
os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join('Resources','budget_data.csv')

#Define
def financial_analysis(record):

    #Total
    total = sum(pl)

    #Find the difference between each profit/loss record and save result to a list
    difference = [pl[i+1]-pl[i] for i in range(len(pl)-1)] 
    total_difference = sum(difference)

    #Find the average change
    average_change = total_difference/len(difference)

    #Format result to 2 decimal places
    format_average_change = "{:.2f}".format(average_change)

    #Total months
    total_months = len(date)
    
    #Greatest increase and decrease in profit
    update_date_list = date.pop(0)  #To remove first entry in the date list
    gdifference = dict.fromkeys(date)   #Create a new dictionary, set keys using Date
    gdifference.update(zip(date,difference))    #Update dictionary with entries from the date list and difference list

    max_increase = max(difference)
    max_decrease = min(difference)
    
    max_month = max(gdifference, key=gdifference.get)   #Get greatest increase month by key
    min_month = min(gdifference, key=gdifference.get)   #Get greatest decrease month by key
    
    #Print output to terminal
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total months: {str(total_months)}")
    print(f"Total: ${str(total)}")
    print(f"Average Change: ${str(format_average_change)}")
    print(f"Greatest Increase in Profits: {str(max_month)} (${str(max_increase)})")
    print(f"Greatest Decrease in Profits: {str(min_month)} (${str(max_decrease)})")
    
    #Export output to txt file
    os.chdir(os.path.dirname(__file__))
    analysis_txt = os.path.join('Analysis','analysis.txt')

    #Write output to txt file
    file = open(analysis_txt,'w')
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write("Total months: " + str(total_months) + "\n")
    file.write("Total: $" + str(total) + "\n")
    file.write("Average Change: $" + str(format_average_change) + "\n")
    file.write("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_increase) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(max_decrease) + ")" + "\n")
 
# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    reader = csv.DictReader(csvfile)

    #Create lists for each column
    date = []
    pl = []
    
    # Loop through the data
    for record in reader:
        date.append(record['Date'])
        pl.append(int(record['Profit/Losses']))
    
    financial_analysis(record)