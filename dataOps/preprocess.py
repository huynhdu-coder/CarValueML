#prepare validated data for modeling through encoding, 
# scaling, feature engineering, and train/test splitting.
import pandas as pd
df = pd.read_csv('../data/raw/cars.csv')

# There are 46% of missing values in the 'price_drop'
# So I created a new column to indicate whether the 'price_drop' value is missing or not.
# Create an indicator before filling missing values
df["price_drop_missing"] = df["price_drop"].isna().astype(int)

# Fill unavailable price-drop amounts with a numeric placeholder
df["price_drop"] = df["price_drop"].fillna(0)
