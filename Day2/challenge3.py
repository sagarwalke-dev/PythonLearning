#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.

#Where x, y and z are replaced with the actual calculated numbers.


currentAge=int(input("Enter Your Current Age: "))
LAST_AGE=90
remainingYears=LAST_AGE-currentAge
remainingMonths=remainingYears*12
remainingWeeks=remainingMonths*4
remainingDays=remainingYears*365
#fString
print(f"You have {remainingDays} days, {remainingWeeks} weeks, {remainingMonths} months and {remainingYears} years left.")

