
#Bankpy challenge
import os       #so it has modules to find the file
import csv      #so it can read a .csv

#this is supposed to tell the program where to find the csv and what its name is
#if you have it in the same folder you can just give it file name
csvpath = os.path.join('budget_data.csv') 

#the stuff after with tells it to open the csv at the path, and that a space leads to a new line
# then it defines a csv reader object "csvreader" and it tells the reader module that its a csv, and that values are 
# delimited with commas

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #variable section
    
    mnth_ct = 0        # number of months of data
    tot_prof = 0       # this will hold the sum of the profits/losses
    dp_max = 0         # this will hold the max change in profits
    dp_min = 0         # this will hold the min change in profits
    dp_sum = 0         #this will hold the sum of the changes in profit
    last_p = 867884    # last month's profit initiallized with first month profit
    dp = 0             # change in profit between last month and this month
    
    #next a for loop is used to extract information for the above variables
    
    for row in csvreader:
        if row[1] != "Profit/Losses":            #an if to throw away the heading
            mnth_ct = mnth_ct + 1                #add 1 to month count ever time loop runs
            dp = int(row[1]) - last_p            #calculate change in profit, make that dp
            dp_sum = dp_sum + dp                 #add the change to the sum of the changes
            tot_prof = tot_prof + int(row[1])    #add profit to the total
            last_p = int(row[1])
        
            if dp > dp_max:                      #if the change is bigger than dp_max record month and value
                dpmxm = str(row[0])
                dp_max = dp
            
            elif dp == dp_max:                    #sets exception if multiple values exist
                dpmxm = ("multiple months")
        
            elif dp < dp_min:                     #same as first if but for min change
                dpmnm = str(row[0])
                dp_min = dp
            
            elif dp == dp_min:
                dpmnm = ("multiple months")
    
    ave_dp = round(dp_sum/(mnth_ct - 1), 2)      #calculate average change once loop is finished, round to 2 places
    
#output section
    
line1 = ("\n Financial Analysis \n")
line2 = ("----------------------- \n")
line3 = ("Total Months = " + str(mnth_ct) + "\n")
line4 = ("Total Revenue = $" + str(tot_prof) + "\n")
line5 = ("Ave. Monthly Change in Profit = $" + str(ave_dp) + "\n")
line6 = ("Largest Increase in Profit was $" + str(dp_max) + " this happened in " + dpmxm + "\n")
line7 = ("Largest Decrease in Profit was $" + str(dp_min) + " this happened in " + dpmnm + "\n") 

#print lines into the terminal
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7) 

#write lines 1 - 7 into a new txtfile

f= open("Financial_Analysis.txt", "w+")

f.write(line1)  
f.write(line2)
f.write(line3)
f.write(line4)
f.write(line5)
f.write(line6)
f.write(line7)

f.close()
    


