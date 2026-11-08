import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

# Find highest and lowest sales
highest = max(sales)
lowest = min(sales)

highest_month = months[sales.index(highest)]
lowest_month = months[sales.index(lowest)]

print("Highest Sales:")
print(highest_month, "=", highest)

print("Lowest Sales:")
print(lowest_month, "=", lowest)

# Line chart

plt.subplot(2,1,1)
plt.plot(months, sales, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales Revenue (₹)")
plt.title("Monthly Sales Revenue - Line Chart")
plt.grid(True)


# Bar chart
plt.subplot(2,1,2)
plt.bar(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales Revenue (₹)")
plt.title("Monthly Sales Revenue - Bar Chart")
plt.grid(True)

plt.tight_layout()
plt.show()