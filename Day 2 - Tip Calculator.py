
# calculating total bill amount each person would pay including tip

print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? '))
tip_percent = int(input('what percentage tip would you like to give? 10, 12 or 15? '))
no_of_people = int(input('How many people to split the bill? '))

total_bill = round(total_bill, 2)
tip_amount = total_bill * tip_percent / 100
total_amount_for_each = (total_bill + tip_amount) / no_of_people
print(round(total_amount_for_each, 2))



