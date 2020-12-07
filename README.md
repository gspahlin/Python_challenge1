# Python_challenge1

This repository contains two python scripts that are designed to read and analyze data from a .csv file. The scripts are housed in two different folders.

pypoll folder:
Pypolls_challenge.py - this is the finished script used to analyze the data. The script is written using lists and for loops to determine who got votes, so that it can
be re-run on additional .csv outputs without changing any internals for subsequent elections. The candidate names are not hard coded, but are generated from the .csv by 
the algorythm. The script is designed to print each candidate's name in alphabetical order along with the vote totals and percentage of the vote obtained by each 
candidate. It also prints the overall total vote and the winning candidate. 

Election_Results.txt - is an example output file for the poll challenge. 

election_data.csv - is the .csv that the script was designed to read. Note: this is a large file, and will not open correctly on excel. 


pybank folder:
Bankpy_Challenge_Final.py - this is a final draft of my bank analysis spreadsheet. The script uses one large for loop to do calculations without importing any data into 
lists. The script calculates the following quantities: Total Profit (or loss), Total months analyzed, Average change in revenue, Greatest increase and decrease in revenue.
The script can handle a case where multiple maxima or minima are present. 

Financial_Analysis.txt - this is an example output file from the script

budget_data.csv - this is the .csv the script was designed to read. 
