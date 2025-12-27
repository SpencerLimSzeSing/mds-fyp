# region Load libraries
# %%
import pandas as pd

pd.set_option("display.max_rows", None)  # show all rows
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# endregion

# region import 5 dataset
# %%
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
# endregion

# region data compilation
# %%
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
# endregion

# region import combined dataset
# %%
combined_df = pd.read_csv("../data/raw/combined_df.csv")
# format
combined_df.nunique()
combined_df.describe(include="object")  # Summary Statistics for Categorical Variables
combined_df["Year"].unique()

combined_df["Item"].unique()
combined_df["Item"] = combined_df["Item"].replace("Rice, paddy", "Rice")

combined_df.isnull().sum()  # no missing value

# duplicate
combined_df.duplicated().sum()  # 2310
duplicates = combined_df[combined_df.duplicated()]
print(duplicates)
combined_df = combined_df.drop_duplicates()  # drop the duplicate
combined_df.duplicated().sum()  # check for duplicate ->zero

# missing
combined_df.isnull().sum()

# Summary Statistics for Numerical Variables¶
combined_df.describe().round(2).T

# data distribution (histogram)
combined_df1 = combined_df.drop(columns=["Year"])
combined_df1.hist(bins=25, figsize=(10, 10))
# data distribution (boxplot)
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
sns.boxplot(data=combined_df1["pesticides_used_in_ton"], orient="h")
plt.title("pesticides")
plt.subplot(2, 2, 2)
sns.boxplot(data=combined_df1["average_rain_fall_mm_per_year"], orient="h")
plt.title("average_rain_fall")
plt.subplot(2, 2, 3)
sns.boxplot(data=combined_df1["avg_temp"], orient="h")
plt.title("avg_temp")
plt.subplot(2, 2, 4)
sns.boxplot(data=combined_df1["yield_in_hg_per_ha"], orient="h")
plt.title("yield")
plt.show()


combined_df.describe(include="object")  # Summary Statistics for Categorical
country_counts = combined_df["Area"].value_counts()

# Data pruning,remove countries with less than 100 record
country_todrop = country_counts[country_counts < 100].index.tolist()
combined_df_filtered = combined_df[~combined_df["Area"].isin(country_todrop)]
print(combined_df_filtered)

combined_df_filtered.describe(include="object")

# log transformation on pesticides and yield
combined_df_filtered["pesticides_used_in_log"] = np.log1p(
    combined_df_filtered["pesticides_used_in_ton"]
)  # log(1 + x) ,avoids negatives
combined_df_filtered.hist(column="pesticides_used_in_log", bins=25, figsize=(5, 5))

combined_df_filtered["yield_in_log"] = np.log1p(
    combined_df_filtered["yield_in_hg_per_ha"]
)  # log(1 + x) ,avoids negatives
combined_df_filtered.hist(column="yield_in_log", bins=25, figsize=(5, 5))

combined_df_filtered[
    [
        "pesticides_used_in_ton",
        "yield_in_hg_per_ha",
        "pesticide_used_in_log",
        "yield_in_log",
    ]
].describe().round(2)
combined_df_filtered = combined_df_filtered.drop(
    columns=["pesticides_used_in_ton", "yield_in_hg_per_ha"]
)

combined_df_filtered.info()

# data distribution (boxplot)
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
sns.boxplot(data=combined_df_filtered["pesticide_used_in_log"], orient="h")
plt.title("pesticides")
plt.subplot(2, 2, 2)
sns.boxplot(data=combined_df_filtered["average_rain_fall_mm_per_year"], orient="h")
plt.title("average_rain_fall")
plt.subplot(2, 2, 3)
sns.boxplot(data=combined_df_filtered["avg_temp"], orient="h")
plt.title("avg_temp")
plt.subplot(2, 2, 4)
sns.boxplot(data=combined_df_filtered["yield_in_log"], orient="h")
plt.title("yield")
plt.show()

country = combined_df_filtered["Area"].unique().tolist()
print(country)
# endregion
# %%
