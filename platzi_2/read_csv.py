import csv

# read a file
# with open('platzi/products.csv', mode="r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)

# show information by column name
with open('platzi/products.csv', mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Product: {row['name']}, Price: {row['price']}")