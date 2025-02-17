import json

# read the json file
with open("platzi/products.json") as file:
    data = json.load(file)

# # show the data
# for product in data:
#     # print(product)
#     print(f"Product: {product["name"]}, Price: {product["price"]}")


# write a new product to the json file
new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

with open("platzi/products.json", "w") as file:
    data.append(new_product)
    json.dump(data, file, indent=4)