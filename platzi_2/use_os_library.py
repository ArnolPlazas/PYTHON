import os

# Get the current working directory
# cwd = os.getcwd()
# print("current working directory: ", cwd)

# list json files in the current working directory
# files = [f for f in os.listdir("platzi") if f.endswith(".json")]
# print("json files in the current working directory: ", files)

# rename files
os.rename("platzi/products.json", "platzi/items.json")
print("Renamed 'products.json' to 'items.json'")