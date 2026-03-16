import pandas as pd 
import matlotlib.pyplot as plt

# 1. Load the macroeconomic and emissions dataset
# This script analyzes the relationship between GDP growth and CO2 emissions.
try:
  df = pd.read_csv('data.csv')
  print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: data.csv file not found.")
    exit()
  # 2. Basic Data Cleaning
df.dropna(inplace=True) # Remove missing values to ensure accurate modeling

# 3. Statistical Analysis: Correlation
correlation = df['GDP_Growth_Rate'].corr(df['CO2_Emissions_Mt'])
print(f"Pearson Correlation between GDP Growth and CO2 Emissions: {correlation:.2f}")

# 4. Data Visualization (Trend Analysis)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot GDP Growth
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP Growth Rate (%)', color=color)
ax1.plot(df['Year'], df['GDP_Growth_Rate'], color=color, marker='o', label='GDP Growth')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for Emissions
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('CO2 Emissions (Mt)', color=color)
ax2.plot(df['Year'], df['CO2_Emissions_Mt'], color=color, marker='s', linestyle='--', label='CO2 Emissions')
ax2.tick_params(axis='y', labelcolor=color)

# Formatting and saving the plot
plt.title('Macroeconomic Trend: Turkey GDP Growth vs. CO2 Emissions')
fig.tight_layout()
plt.grid(True, alpha=0.3)
plt.savefig('gdp_vs_emissions_plot.png')
print("Analysis complete. Visualization saved as 'gdp_vs_emissions_plot.png'.")
