import csv

file_path = 'platzi/products.csv'
updated_file_path = 'platzi/products_updated.csv'

with open(file_path, mode="r") as f:
    reader = csv.DictReader(f)
    field_names = reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        for row in reader:
            row['total_value']= int(row['price']) * int(row['quantity'])
            writer.writerow(row)