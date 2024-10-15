#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input(f"What was the total bill? $"))
tip_percentage = float(
    input(f"How much tip would you like to give? 10, 12, or 15?"))
people_split = int(input(f"How many people to split the bill?"))
person_bill = (total_bill * (1 + tip_percentage / 100)) / people_split
print(f'Each person should pay: {"{:.2f}".format(person_bill)}$')
