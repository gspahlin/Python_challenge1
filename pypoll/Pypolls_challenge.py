#Pypolls challenge
import os       #so it has modules to find the file
import csv      #so it can read a .csv

#this is supposed to tell the program where to find the csv and what its name is
#if you have it in the same folder you can just give it file name
csvpath = os.path.join('election_data.csv') 

#the stuff after with tells it to open the csv at the path, and that a space leads to a new line
# then it defines a csv reader object "csvreader" and it tells the reader module that its a csv, and that values are 
# delimited with commas

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    votes = []                               #this is a list for votes
    
    for row in csvreader:
        if row[2] != "Candidate":            #an if to throw away the heading
            votes.append(str(row[2]))       #this adds all the votes to a huge list in python
    
    votes.sort()                             #this will sort the votes by candidate name
    
    cands = []                               # this is a list for unique candidate names
    
    for name in votes:                       # this loop is for finding unique candidate names cite for method: 
        if name not in cands:                # https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
            cands.append(name)                
    
    totes = []                               #This list is for holding vote counts
    
    for can in cands:                        #this loop loops through candidates and counts the vote list for each name value
        ctot = votes.count(can) 
        totes.append(ctot)
        
    totevotes = sum(totes)                   #this calculates total votes
    
    percnts = []
    
    for tote in totes:                        #this loop uses the totals list to make a percents list
        pc = round((tote/totevotes)*100, 3)
        percnts.append(pc)
    
    windex = percnts.index(max(percnts))     
    
     #Windex is the index of the highest percent value. 
     #all the lists are ordered by candidate so it tells you which candidate won
        
# output section

lines = []
c = 0

#this loop prepares output lines based on the results

for can in cands:
    lines.append(str(cands[c]) + ": " + str(percnts[c]) + "% " + "(" + str(totes[c]) + ")")   
    c = c + 1

#print to terminal

print("\n Election Results")
print("---------------------------")
print("Total Votes:" + str(totevotes))
print("---------------------------")
for line in lines:
    print(line + "\n")
print("---------------------------")
print("Winner:" + str(cands[windex]))
print("---------------------------")
    
#Text output. First we open up a test file, the the above print comments turn to write commands

f= open("Election_Results.txt", "w+")

f.write("\n Election Results \n")
f.write("--------------------------- \n")
f.write("Total Votes:" + str(totevotes)+ "\n")
f.write("--------------------------- \n")
for line in lines:
    f.write(line + "\n")
f.write("--------------------------- \n")
f.write("Winner:" + str(cands[windex])+ "\n")
f.write("--------------------------- \n")

f.close()