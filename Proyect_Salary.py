gross = int(input("Please enter the gross salary: "))
children = int(input("Please enter the number of children: "))

if gross <= 1000:
    tax = gross * 0.1
elif gross <= 2000:
    tax = gross * 0.12 - (children * 0.01 * gross)
elif gross <= 4000:
    tax = gross * 0.14 - (children * 0.01 * gross)
else:
    tax = gross * 0.18 - (children * 0.005 * gross)

net = gross - tax

print("The net salary is:", net)