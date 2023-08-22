#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome To Tip Calculater.")
a=int(input("What was the total bill?:\n"))
b=int(input("What percentage of tip you want to give?10,12 or 15\n"))
c=int(input("How many people to split the bill?\n"))
h=a/c+(a/b)
print("Each person should pay:",round(h,2))