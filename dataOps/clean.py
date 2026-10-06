#Goal: read CSV, remove duplicates, fix data types, 
import pandas as pd

df = pd.read_csv('../data/raw/cars.csv')
pd.set_option("display.max_columns", None)

# Handle duplicates
duplicate_count = df.duplicated().sum()
print(f"\nDuplicate rows found: {duplicate_count:,}")

df = df.drop_duplicates().reset_index(drop=True)
print(f"\nNumber of rows after removing duplicates: {len(df)}")

# Handle missing/invalid values
missing_percent = df.isna().mean() * 100
print(missing_percent)

# Remove rows with missing mileage
df = df.dropna(subset=["mileage"]).reset_index(drop=True)

#Handle categorical columns
categorical_columns = [
    "engine",
    "transmission",
    "drivetrain",
    "fuel_type",
    "exterior_color",
    "interior_color",
]
df[categorical_columns] = df[categorical_columns].fillna('unknown')

#drop unnecessary columns
df = df.drop(columns=['seller_name', 'seller_rating', 'driver_rating', 'driver_reviews_num', 'price_drop'])

# Preserve unknown history information as -1
history_columns = [
    "accidents_or_damage",
    "one_owner",
    "personal_use_only"
]

df[history_columns] = df[history_columns].fillna(-1)

# The mpg column stored as a format of "city - highway" mpg. 
# I will split this into two separate columns for city and highway mpg.
# Standardize dashes and remove surrounding whitespace
df["mpg"] = (
    df["mpg"]
    .str.strip()
    .str.replace("–", "-", regex=False)
    .str.replace("—", "-", regex=False)
)

# Split MPG range into two columns
mpg_split = df["mpg"].str.split("-", n=1, expand=True)

mpg_1 = pd.to_numeric(mpg_split[0], errors="coerce")
mpg_2 = pd.to_numeric(mpg_split[1], errors="coerce")

df["average_mpg"] = pd.concat(
    [mpg_1, mpg_2],
    axis=1
).mean(axis=1)

df = df.drop(columns=["mpg"])

#Final data quality check
print("\n===== CLEANED DATA =====")

print(f"Number of rows: {len(df):,}")
print(f"Number of columns: {len(df.columns)}")


#Save the data
output_path = "../data/cleaned/cars_cleaned.csv"

df.to_csv(
    output_path,
    index=False
)

print(
    f"\nCleaned dataset saved to: {output_path}"
)
