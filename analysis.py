import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("inventory_turnover_2024.csv")

# Drop 'Average' row
df_clean = df[df["Quarter"] != "Average"]

# Compute average turnover
average_turnover = df_clean["Turnover"].mean()

print("Cleaned Data:")
print(df_clean)
print("\nCalculated Average Turnover:", round(average_turnover, 2))

# --- Visualization ---
plt.figure(figsize=(8, 5))

# Bar chart
plt.bar(df_clean["Quarter"], df_clean["Turnover"], color="skyblue", label="Turnover")

# Line chart overlay
plt.plot(df_clean["Quarter"], df_clean["Turnover"], color="blue", marker="o", linestyle="-", label="Trend")

# Add average line
plt.axhline(average_turnover, color="red", linestyle="--", linewidth=1.5, label=f"Average = {round(average_turnover,2)}")

# Titles and labels
plt.title("Inventory Turnover by Quarter (2024)", fontsize=14, fontweight="bold")
plt.xlabel("Quarter")
plt.ylabel("Turnover")
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("inventory_turnover.png", dpi=300)
plt.show()
# is this change ok