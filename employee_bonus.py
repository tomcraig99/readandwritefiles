import csv

# create reader object
customers = open("EmployeePay.csv", "r")
customer_file = csv.reader(customers, delimiter=",")
# skip header
next(customer_file)
# loop to create temp variables and print each cust
for record in customer_file:
    first = record[1]
    last = record[2]
    salary = float(record[3])
    bonus_percent = float(record[4])
    bonus = bonus_percent * salary

    print("Fname:     ", first, sep="")
    print("Lname:     ", last, sep="")
    print("Salary:    ", "$", format(salary, ",.2f"), sep="")
    print("Bonus:     ", "$", format(bonus, ",.2f"), sep="")
    total = (1 + bonus_percent) * salary
    print("Total pay: ", "$", format(total, "<,.2f"), sep="")
    # input to go to next employee
    input()
