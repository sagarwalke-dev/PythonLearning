#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#1. Take input from user
persons=float(input("Enter number of persons to split bill:"))
bill=float(input("Enter the bill amount: "))
tip=float(input("Enter tip percentage(%): "))
totalBill=bill+(tip/100*bill)

eachBill=totalBill/persons
print("Each person should pay "+str(round(eachBill,2)))
