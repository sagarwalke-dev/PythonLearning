#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 1.Take input from user
weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))

#2.Calcualte BIM 
bim=weight/(height*height)

print(str(round(bim)))
