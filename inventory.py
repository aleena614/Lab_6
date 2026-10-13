
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a messy product inventory dataset
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Yogurt", "Cookies", "Water", "Cheese", "Soda"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks", "beverages",
        "DAIRY ", " snacks ", "Beverages", "dairy", " BEVERAGES "
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800",
        "Rs. 200", "Rs. 150", "Rs. 50", "Rs. 600", "Rs. 950"
    ],
    "Stock": [40, 120, 60, 100, 30, 80, 90, 150, 45, 55]
}

# 2. Create a DataFrame
df = pd.DataFrame(data)

# 3. Clean the Category column
# Remove extra spaces and standardize capitalization
df["Category"] = df["Category"].str.strip().str.title()

# 4. Convert Price from text to numeric values
# Remove the "Rs. " prefix and commas
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "", regex=False)

# Convert the cleaned price strings into numbers
df["Price"] = pd.to_numeric(df["Price"])

# 5. Add label encoding for Category
df["Category_Code"] = df["Category"].astype("category").cat.codes

# 6. Print the cleaned DataFrame
print("Cleaned Product Inventory:")
print(df)

# 7. Calculate average price for each category
avg_price = df.groupby("Category")["Price"].mean()

# Calculate total stock for each category
category_stock = df.groupby("Category")["Stock"].sum()

# 8. Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot: average price per category
avg_price.plot(kind="bar", ax=axes[0])

axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=0)

# Pie chart: each category's share of total stock
axes[1].pie(
    category_stock,
    labels=category_stock.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[1].set_title("Share of Total Stock by Category")

# Adjust spacing between the plots
plt.tight_layout()

# 9. Save the figure
plt.savefig("inventory_plots.png", dpi=300, bbox_inches="tight")

print("\nSaved inventory_plots.png")

# 10. Display the plots
plt.show()
