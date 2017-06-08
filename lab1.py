#include import for std
from numpy import *

#Open the file, read the lines, close the file
f = open("cbpss.txt")
lines = f.readlines()
f.close()

#Title
print ("China Border Protection Agency Satisfaction Survey v1.0\n")

#Create a list of ratings
ratings = []

#Initialize count variables
count1 = 0
count2 = 0
count3 = 0
count4 = 0

#Iterate through the file, save the first column as an integer into rates
for line in lines:
    cols = line
    rates = int(cols[0])
    
#Append rates to ratings list only if condition is true
    if rates >= 1 and rates < 5:        
        ratings.append(rates)          
    if rates == 1:
        count1 = count1 + 1
    elif rates == 2:
        count2 = count2 + 1
    elif rates == 3:
        count3 = count3 + 1
    elif rates == 4:
        count4 = count4 + 1   
        
#Compute Min, Max and Average   
avgRating = sum(ratings) / len(lines)   
maxRating = max(ratings)
minRating = min(ratings)

#Print the file as integer values
print (str(ratings)+"\n")

#Report the High, Low, Avg ratings
print ("Highest Rating:" + str(maxRating))
print ("Lowest Rating:" + str(minRating))
print ("Average Rating:" + str(int(avgRating)))

#Report amount of each rating
print ("# of 1 ratings:" + str(count1))
print ("# of 2 ratings:" + str(count2))
print ("# of 3 ratings:" + str(count3))
print ("# of 4 ratings:" + str(count4))

#Report the standar deviation of the ratings
print ("Standard Deviation: " + str(std(ratings)))



