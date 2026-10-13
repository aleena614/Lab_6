
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a messy 15-day weather dataset
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-04", "2026-09-05", "2026-09-06",
        "2026-09-07", "2026-09-08", "2026-09-09",
        "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15",
        "2026-09-01"
    ],
    "City": [
        " kamra", "KAMRA ", "Kamra", " attock ",
        "ATTOCK", "Attock ", " kamra ", "KAMRA",
        "Attock", " attock", "KAMRA ", "Kamra",
        "ATTOCK ", "kamra", " Attock ", " kamra"
    ],
    "Temperature": [
        "34C", "33C", "32C", "31C", "30C",
        "29C", "28C", "35C", "36C", "32C",
        "31C", "30C", "29C", "33C", "34C",
        "34C"
    ],
    "Humidity": [
        42, 48, 50, None, 55,
        58, None, 60, 62, 65,
        None, 70, 58, None, 52,
        42
    ],
    "Condition": [
        "sunny", " CLOUDY ", "Rainy", " sunny ",
        "CLOUDY", "rainy ", " Sunny", "cloudy",
        "SUNNY ", " Rainy", "cloudy ", "SUNNY",
        "Cloudy", " sunny", "CLOUDY ", " SUNNY "
    ]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)

# 3. Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# 4. Remove the temperature unit and convert to numbers
df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
)
df["Temperature"] = pd.to_numeric(df["Temperature"])

# 5. Convert Date text to datetime
df["Date"] = pd.to_datetime(df["Date"])

# 6. Drop duplicate rows
df = df.drop_duplicates().copy()

print("Rows after dropping duplicates:", len(df))

# 7. Fill missing humidity using the median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print(
    "Missing Humidity filled with median:",
    humidity_median
)

# 8. One-hot encode the Condition column
encoded_conditions = pd.get_dummies(
    df["Condition"],
    prefix="Condition",
    dtype=int
)

print("\nEncoded Condition columns:")
print(encoded_conditions.to_string(index=False))

# 9. Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print(
    "\nCorrelation (Temperature, Humidity):",
    round(correlation, 2)
)

# 10. Print condition counts
condition_counts = df["Condition"].value_counts()

print("\nCondition counts:")
print(condition_counts)

# 11. Create a 2 x 2 visualization dashboard
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Plot 1: Temperature over Date
axes[0, 0].plot(
    df["Date"],
    df["Temperature"],
    marker="o"
)
axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# Plot 2: Temperature vs Humidity
axes[0, 1].scatter(
    df["Temperature"],
    df["Humidity"]
)
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity")

# Plot 3: Number of Days by Condition
axes[1, 0].pie(
    condition_counts,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Days by Weather Condition")

# Plot 4: Temperature Histogram
axes[1, 1].hist(
    df["Temperature"],
    bins=6,
    edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

# Overall dashboard title
fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# 12. Save the complete dashboard
plt.savefig(
    "weather_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nSaved weather_dashboard.png")

plt.show()
