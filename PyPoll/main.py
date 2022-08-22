import os
import csv

#Path
os.chdir(os.path.dirname(__file__))
election_data_csv = os.path.join('Resources','election_data.csv')

#Define
def election_results(record):

    #Total votes
    total = len(ballot_id)

    #Count the total votes for each candidate
    counter1 = candidate.count('Charles Casper Stockham')
    counter2 = candidate.count('Diana DeGette')
    counter3 = candidate.count('Raymon Anthony Doane')

    #Count the percent for each candidate
    percent1 = counter1 / total * 100
    percent2 = counter2 / total * 100
    percent3 = counter3 / total * 100

    #Format results to 3 decimal places
    format_percent1 = "{:.3f}".format(percent1)
    format_percent2 = "{:.3f}".format(percent2)
    format_percent3 = "{:.3f}".format(percent3)

    #Print results to terminal
    print(f"Election Results")
    print(f"----------------------------------------")
    print(f"Total Votes: {str(total)}")
    print(f"----------------------------------------")
    print(f"Charles Casper Stockham: {str(format_percent1)}% ({str(counter1)})")
    print(f"Diana DeGette: {str(format_percent2)}% ({str(counter2)})")
    print(f"Raymon Anthony Doane: {str(format_percent3)}% ({str(counter3)})")
    print(f"----------------------------------------")
    if counter1 > counter2 and counter3:
        print(f"Winner: Charles Casper Stockham")
    elif counter2 > counter1 and counter3:
        print(f"Winner: Diana DeGette")
    elif counter3 > counter1 and counter2:
        print(f"Winner: Raymon Anthony Doane")
    print(f"----------------------------------------")

    #Export output to txt file
    os.chdir(os.path.dirname(__file__))
    analysis_txt = os.path.join('Analysis','analysis.txt')

    #Write into txt file
    file = open(analysis_txt,'w')
    file.write('Election Results\n')
    file.write('----------------------------------------\n')
    file.write("Total Votes: " + str(total) + "\n")
    file.write('----------------------------------------\n')
    file.write("Charles Casper Stockham: " + str(format_percent1) + "%" + " (" + str(counter1) + ")" + "\n")
    file.write("Diana DeGette: " + str(format_percent2) + "%" + " (" + str(counter2) + ")" + "\n")
    file.write("Raymon Anthony Doane: " + str(format_percent3) + "%" + " (" + str(counter3) + ")" + "\n")
    file.write('----------------------------------------\n')
    if counter1 > counter2 and counter3:
        file.write("Winner: Charles Casper Stockham" + "\n")
    elif counter2 > counter1 and counter3:
        file.write("Winner: Diana DeGette" + "\n")
    elif counter3 > counter1 and counter2:
        file.write("Winner: Raymon Anthony Doane" + "\n")
    file.write('----------------------------------------\n')

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    reader = csv.DictReader(csvfile)

    #Create lists for each column
    ballot_id = []
    candidate = []

    # Loop through the data
    for record in reader:
        ballot_id.append(int(record['Ballot ID']))
        candidate.append(record['Candidate'])

    election_results(record)