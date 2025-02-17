import csv

new_product = {
    'name': 'Wireless Charger',
    'price': 80,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-02-11'
}

with open('platzi/products.csv', mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=new_product.keys())
    writer.writerow(new_product)
    file.write("\n")