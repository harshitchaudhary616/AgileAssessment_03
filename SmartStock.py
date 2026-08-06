portfolio = [
    {
        "investor_id": 101,
        "symbol": "TCS",
        "quantity": 50,
        "buy_price": 3200,
        "current_price": 3650,
        "sector": "IT",
        "dividend": 3000
    },
    {
        "investor_id": 102,
        "symbol": "INFY",
        "quantity": 80,
        "buy_price": 1450,
        "current_price": 1620,
        "sector": "IT",
        "dividend": 2500
    },
    {
        "investor_id": 103,
        "symbol": "HDFCBANK",
        "quantity": 60,
        "buy_price": 1550,
        "current_price": 1700,
        "sector": "Banking",
        "dividend": 1800
    },
    {
        "investor_id": 104,
        "symbol": "RELIANCE",
        "quantity": 40,
        "buy_price": 2500,
        "current_price": 2750,
        "sector": "Energy",
        "dividend": 2200
    },
    {
        "investor_id": 105,
        "symbol": "SBIN",
        "quantity": 100,
        "buy_price": 650,
        "current_price": 610,
        "sector": "Banking",
        "dividend": 1200
    }
]

sector = {}
investors = []

for p in portfolio:
    p["investment"] = p["quantity"] * p["buy_price"]
    p["current"] = p["quantity"] * p["current_price"]
    p["profit"] = p["current"] - p["investment"] + p["dividend"]
    p["return"] = round((p["profit"] / p["investment"]) * 100, 2)

    if p["sector"] not in sector:
        sector[p["sector"]] = 0

    sector[p["sector"]] += p["current"]

    investors.append({
        "id": p["investor_id"],
        "return": p["return"]
    })

print("Investment Value")

for p in portfolio:
    print(p["symbol"], ":", p["investment"])

print()

print("Current Value")

for p in portfolio:
    print(p["symbol"], ":", p["current"])

print()

print("Profit / Loss")

for p in portfolio:
    print(p["symbol"], ":", p["profit"])

print()

print("Percentage Return")

for p in portfolio:
    print(p["symbol"], ":", str(p["return"]) + "%")

best = max(portfolio, key=lambda x: x["return"])
worst = min(portfolio, key=lambda x: x["return"])

print()
print("Best Performing Stock")
print(best["symbol"], best["return"])

print()
print("Worst Performing Stock")
print(worst["symbol"], worst["return"])

print()
print("Sector Wise Exposure")

for k, v in sector.items():
    print(k, ":", v)

investors.sort(key=lambda x: x["return"], reverse=True)

print()
print("Investor Ranking")

for i in investors:
    print(i["id"], i["return"])

file = open("portfolio_report.txt", "w")

file.write("Portfolio Report\n\n")

for p in portfolio:
    file.write(
        str(p["investor_id"]) + " " +
        p["symbol"] + " " +
        str(p["investment"]) + " " +
        str(p["current"]) + " " +
        str(p["profit"]) + " " +
        str(p["return"]) + "%\n"
    )

file.close()

print()
print("Portfolio Report Saved")

print()

file = open("portfolio_report.txt", "r")

print(file.read())

file.close()
