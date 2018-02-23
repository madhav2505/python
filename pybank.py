import os
import csv

totalMonths = 0
totalRevenue = 0
avgRevenueChange = 0
greatestRevIncDate = "Date1"
greatestRevIncAmt = 0
greatestRevDecDate = "Date2"
greatestRevDecAmt = 0
totalRevenueChange = 0


fileList = ["budget_data_1.csv","budget_data_2.csv"]
for file in fileList:
    csvpath = os.path.join("raw_data",file)
    with open(csvpath, newline='') as csvfile:
        csvfile.readline()
        csvreader = csv.reader(csvfile, delimiter=',')
        totalMonths = 0
        totalRevenue = 0
        prevRevenue = 0
        greatestRevIncAmt = 0
        greatestRevDecAmt = 0
        for row in csvreader:
            totalRevenue = totalRevenue + int(row[1])
            totalMonths = totalMonths +1
            revIncrease = int(row[1]) - prevRevenue
            totalRevenueChange = totalRevenueChange + revIncrease
            prevRevenue =  int(row[1])
            if(revIncrease > greatestRevIncAmt):
                greatestRevIncAmt = revIncrease
                greatestRevIncDate = row[0]
            
            if(revIncrease < greatestRevDecAmt):
                greatestRevDecAmt = revIncrease
                greatestRevDecDate = row[0]


    avgRevenueChange = round(totalRevenueChange/totalMonths,2)

   #create and open output file to write resuts to
    outputpath = os.path.join("raw_data",file.split(".")[0] + "_Results.txt")

    lines = []
    
    resultsfile = open(outputpath, "w")
    
    #create the output
    lines.append("Financial Analysis")
    lines.append("----------------------------")
    lines.append("Total Months: "+str(totalMonths))
    lines.append("Total Revenue: $" + str(totalRevenue))
    lines.append("Average Revenue Change: $"+str(avgRevenueChange))
    lines.append("Greatest Increase in Revenue: "+greatestRevIncDate + " ($" + str(greatestRevIncAmt) +")")
    lines.append("Greatest Decrease in Revenue: "+greatestRevDecDate + " ($" + str(greatestRevDecAmt) +")")

     ##Write the output to file and console
    for line in lines:
        print(line)
        print(line,file=resultsfile)
        
    #new line
    print()
    
    #close the file
    resultsfile.close()