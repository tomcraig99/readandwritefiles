import csv

# reader object
customers = open("customers.csv", "r")
customer_file = csv.reader(customers, delimiter=",")
# writer object
countries = open("customer_country.csv", "w", newline="")
country_file = csv.writer(countries, delimiter=",")
# skip header
next(customer_file)
# create lists
header = ["First Name", "Last name", "Country"]
country_file.writerow(header)
# loop to write to new csv
i = 0
for record in customer_file:
    first = record[1]
    last = record[2]
    country = record[4]
    # temp list and write to file
    country_list = [first, last, country]
    country_file.writerow(country_list)
    i += 1
# total and close files
print("Customers:", i)
customers.close()
countries.close()
