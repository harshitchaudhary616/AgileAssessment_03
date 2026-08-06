import csv

products = [
    {
        "id": 101,
        "name": "Laptop",
        "category": "Electronics",
        "opening_stock": 100,
        "sold": 70,
        "returned": 5,
        "lead_time": 7,
        "cost": 500,
        "price": 700
    },
    {
        "id": 102,
        "name": "Mobile",
        "category": "Electronics",
        "opening_stock": 150,
        "sold": 120,
        "returned": 8,
        "lead_time": 5,
        "cost": 300,
        "price": 450
    },
    {
        "id": 103,
        "name": "Chair",
        "category": "Furniture",
        "opening_stock": 80,
        "sold": 50,
        "returned": 2,
        "lead_time": 10,
        "cost": 40,
        "price": 70
    },
    {
        "id": 104,
        "name": "Table",
        "category": "Furniture",
        "opening_stock": 60,
        "sold": 35,
        "returned": 1,
        "lead_time": 12,
        "cost": 80,
        "price": 130
    },
    {
        "id": 105,
        "name": "Shoes",
        "category": "Fashion",
        "opening_stock": 200,
        "sold": 160,
        "returned": 10,
        "lead_time": 6,
        "cost": 20,
        "price": 45
    }
]

category_profit = {}

for p in products:
    p["current_stock"] = p["opening_stock"] - p["sold"] + p["returned"]
    p["profit"] = (p["price"] - p["cost"]) * (p["sold"] - p["returned"])
    p["turnover"] = round(p["sold"] / p["opening_stock"], 2)
    p["forecast"] = int((p["sold"] + (p["sold"] - 10) + (p["sold"] - 20)) / 3)

    if p["category"] not in category_profit:
        category_profit[p["category"]] = 0

    category_profit[p["category"]] += p["profit"]

print("Current Stock")

for p in products:
    print(p["name"], ":", p["current_stock"])

print()

print("Profit")

for p in products:
    print(p["name"], ":", p["profit"])

print()

print("Products Requiring Reorder")

for p in products:
    if p["current_stock"] < 30:
        print(p["name"])

print()

print("Inventory Turnover Ratio")

for p in products:
    print(p["name"], ":", p["turnover"])

highest = max(products, key=lambda x: x["profit"])

print()
print("Highest Profit Product")
print(highest["name"], highest["profit"])

print()
print("Category Wise Profit")

for k, v in category_profit.items():
    print(k, ":", v)

print()
print("Predicted Next Month Demand")

for p in products:
    print(p["name"], ":", p["forecast"])

products.sort(key=lambda x: x["profit"], reverse=True)

print()
print("Products Sorted By Profit")

for p in products:
    print(p["name"], p["profit"])

with open("inventory_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "ID",
        "Name",
        "Category",
        "CurrentStock",
        "Profit",
        "Turnover",
        "Forecast"
    ])

    for p in products:
        writer.writerow([
            p["id"],
            p["name"],
            p["category"],
            p["current_stock"],
            p["profit"],
            p["turnover"],
            p["forecast"]
        ])

print()
print("CSV Exported Successfully")

data = []

with open("inventory_report.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Profit"] = int(row["Profit"])
        data.append(row)

data.sort(key=lambda x: x["Profit"], reverse=True)

print()
print("Top Five Profitable Products")

for p in data[:5]:
    print(p["Name"], p["Profit"])
