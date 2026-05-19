import pandas as pd
import matplotlib

# Use a non-GUI backend so the script works even if Tk/Tcl isn't installed.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('compact.csv')

# Show Columns
print("Columns in Dataset:\n")
print(df.columns)

# Filter Pakistan Data
pakistan = df.loc[df['country'] == 'Pakistan'].copy()

# Convert date column
pakistan['date'] = pd.to_datetime(pakistan['date'])
pakistan = pakistan.sort_values('date')

# Column name compatibility (some datasets use different names)
cases_col = 'cumulative_confirmed' if 'cumulative_confirmed' in pakistan.columns else 'total_cases'
deaths_col = 'cumulative_deceased' if 'cumulative_deceased' in pakistan.columns else 'total_deaths'

# Plot Graph
plt.figure(figsize=(12,6))

plt.plot(
    pakistan['date'],
    pakistan[cases_col]
)

plt.title('COVID-19 Cases in Pakistan')

plt.xlabel('Date')
plt.ylabel('Total Cases')

plt.grid(True)

# Save Graph
plt.savefig('graph.png')

print("\nSaved plot as graph.png")

# Calculate Death Rate
pakistan['death_rate'] = (
    pakistan[deaths_col]
    /
    pakistan[cases_col]
) * 100

# Latest Death Rate
latest = (
    pakistan.loc[(pakistan[cases_col] > 0), ['date', 'death_rate']]
    .dropna()
    .tail(1)
)

print("\nLatest Death Rate:\n")
print(latest)

# Insights
print("\nINSIGHTS")
print("1. COVID cases increased rapidly during waves.")
print("2. Death rate stayed lower than total cases.")
print("3. Cases decreased after vaccination.")
