import pandas as pd

# import 5 dataset
pesticides = pd.read_csv("../data/raw/pesticides.csv")
rainfall = pd.read_csv("../data/raw/rainfall.csv")
temp = pd.read_csv("../data/raw/temp.csv")
yieldd = pd.read_csv("../data/raw/yield.csv")
# retrive dataset overview
pesticides.info()
pesticides.head()

rainfall.info()
rainfall.head()

temp.info()
temp.head()

yieldd.info()
yieldd.head()

# data compilation
# 1.pesticides
pesticides.nunique()
# rename column
pesticides = pesticides.rename(columns={"Value": "pesticides_used_in_ton"})
# remove irrelavant columns
pesticides = pesticides.drop(columns=["Domain", "Element", "Item", "Unit"])

# 2.rainfall
# convert object to numeric
rainfall["average_rain_fall_mm_per_year"] = pd.to_numeric(
    rainfall["average_rain_fall_mm_per_year"], errors="coerce"
)
# strip spaces from all column names
rainfall.columns = rainfall.columns.str.strip()

# 3.temp
# rename
temp = temp.rename(columns={"year": "Year", "country": "Area"})

# 5.yieldd
yieldd.nunique()
# rename column
yieldd = yieldd.rename(columns={"Value": "yield_in_hg_per_ha"})
# remove irrelavant columns
yieldd = yieldd.drop(
    columns=[
        "Area Code",
        "Item Code",
        "Year Code",
        "Domain Code",
        "Domain",
        "Element",
        "Element Code",
        "Unit",
    ]
)

# compile
combined_df = pd.merge(pesticides, rainfall, how="inner", on=["Area", "Year"])
combined_df = combined_df.merge(temp, how="inner", on=["Area", "Year"])
combined_df = combined_df.merge(yieldd, how="inner", on=["Area", "Year"])


combined_df.isnull().sum()
combined_df[combined_df.isnull().any(axis=1)]
combined_df = combined_df.dropna()

# Save combined_df to CSV in the given path
combined_df.to_csv(path_or_buf="../data/raw/combined_df.csv", index=False)
