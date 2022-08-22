# python-challenge

In this challenge, we are tasked with applying our knowledge by creating 2 Python scripts, 1 of which analyses the financial records of a company and the other to analyse the votes in an election for a small, rural U.S. town.

# PyBank-Challenge
The main script for this analysis is located in /python-challenge/PyBank/main.py

The script analyses the financial dataset provided as a csv type file, located in the subfolder /PyBank/Resources/budget_data.csv
    * The script loops through each row of the csv file and saves the data from each column (Date & Profit/Losses) into their respective lists. 
    * The script then analyses the financial data as required by the challenge.
    * The script then outputs the result onto the terminal and exports the output into a txt file, located in the subfolder /PyBank/Analysis/analysis.txt

# PyPoll-Challenge
The main script for this analysis is located in /python-challenge/PyPoll/main.py

The script analyses the election vote dataset provided as a csv type file, located in the subfolder /PyPoll/Resources/election_data.csv
    * The script loops through each row of the csv file and saves the data from 2 columns (Ballot ID & Candidate) into their respective lists. The County column was ignored as it did not provide any value data for analysis. 
    * The script then analyses the data in the list and finds the winner of the election as required by the challenge.
    * The script then outputs the result onto the terminal and exports the output into a txt file, located in the subfolder /PyPoll/Analysis/analysis.txt