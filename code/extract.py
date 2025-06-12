import pandas as pd

# EXTRACT
# Load the CSV
df = pd.read_csv(r"C:\Users\ashis\OneDrive\Desktop\archive\dataset\covid_19_india.csv")

# Show first 5 rows
print(df.head())

# TRANSFORM
# Rename columns for clarity
df.rename(
    columns={"Date": "date", "ConfirmedIndianNational": "confirmed_indian"},
    inplace=True,
)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Drop unused columns
df = df.drop(["Sno", "Time", "ConfirmedForeignNational"], axis=1)

# Show info
print(df.info())

# LOAD
# Save the cleaned file
output_path = (
    r"C:\Users\ashis\OneDrive\Desktop\archive\cleaned_data\cleaned_covid_data.csv"
)
df.to_csv(output_path, index=False)
