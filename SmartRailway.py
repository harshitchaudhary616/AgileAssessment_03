trains = [
    {
        "number": 12001,
        "route": "Delhi-Mumbai",
        "total_seats": 500,
        "booked": 480,
        "waiting": 35,
        "fare": 1500,
        "cancel": 20,
        "distance": 1400
    },
    {
        "number": 12002,
        "route": "Chennai-Bangalore",
        "total_seats": 400,
        "booked": 250,
        "waiting": 5,
        "fare": 800,
        "cancel": 15,
        "distance": 360
    },
    {
        "number": 12003,
        "route": "Kolkata-Patna",
        "total_seats": 300,
        "booked": 290,
        "waiting": 40,
        "fare": 700,
        "cancel": 10,
        "distance": 600
    },
    {
        "number": 12004,
        "route": "Hyderabad-Goa",
        "total_seats": 350,
        "booked": 120,
        "waiting": 0,
        "fare": 1200,
        "cancel": 5,
        "distance": 700
    },
    {
        "number": 12005,
        "route": "Jaipur-Ahmedabad",
        "total_seats": 450,
        "booked": 430,
        "waiting": 25,
        "fare": 1000,
        "cancel": 12,
        "distance": 650
    }
]

for t in trains:
    t["occupancy"] = round((t["booked"] / t["total_seats"]) * 100, 2)
    t["revenue"] = (t["booked"] - t["cancel"]) * t["fare"]
    t["revenue_per_km"] = round(t["revenue"] / t["distance"], 2)

print("Occupancy Ratio")

for t in trains:
    print(t["route"], ":", str(t["occupancy"]) + "%")

print()

print("Actual Revenue")

for t in trains:
    print(t["route"], ":", t["revenue"])

print()

print("High Demand / Overbooked Trains")

for t in trains:
    if t["waiting"] > 20 or t["booked"] > t["total_seats"]:
        print(t["route"])

print()

print("Revenue Per Kilometer")

for t in trains:
    print(t["route"], ":", t["revenue_per_km"])

best = max(trains, key=lambda x: x["revenue"])

print()
print("Route With Maximum Revenue")
print(best["route"], best["revenue"])

print()
print("Occupancy Below 50%")

for t in trains:
    if t["occupancy"] < 50:
        print(t["route"])

trains.sort(key=lambda x: x["revenue"], reverse=True)

print()
print("Sorted By Revenue")

for t in trains:
    print(t["route"], t["revenue"])

file = open("reservation_report.txt", "w")

file.write("Railway Reservation Analytics Report\n\n")

for t in trains:
    file.write(
        t["route"] +
        " Revenue: " + str(t["revenue"]) +
        " Occupancy: " + str(t["occupancy"]) + "%\n"
    )

file.close()

print()
print("Report Saved Successfully")

print()
print("Reading Report")

file = open("reservation_report.txt", "r")

print(file.read())

file.close()

print("Top Three Revenue Generating Trains")

for t in trains[:3]:
    print(t["route"], t["revenue"])
