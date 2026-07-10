import pandas as pd

# ----------------------------
# Load Dataset
# ----------------------------
file_path = "../data/Dataset for Data Analytics.xlsx"

df = pd.read_excel(file_path)

print("="*50)
print("Original Dataset Shape:", df.shape)

# ----------------------------
# Missing Values
# ----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill numerical columns with median
num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill text columns with Unknown
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# ----------------------------
# Remove Duplicates
# ----------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# ----------------------------
# Convert Date Column
# ----------------------------
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# ----------------------------
# Remove Invalid Dates
# ----------------------------
invalid_dates = df["Date"].isna().sum()

print("Invalid Dates:", invalid_dates)

# ----------------------------
# Remove Duplicate Order IDs
# ----------------------------
if "OrderID" in df.columns:
    duplicate_ids = df["OrderID"].duplicated().sum()
    print("Duplicate Order IDs:", duplicate_ids)

    df = df.drop_duplicates(subset=["OrderID"])

# ----------------------------
# Strip Spaces
# ----------------------------
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# ----------------------------
# Save Cleaned Dataset
# ----------------------------
output_file = "../data/cleaned_data.csv"

df.to_csv(output_file, index=False)

print("="*50)
print("Cleaned Dataset Shape:", df.shape)
print("Cleaned dataset saved as:", output_file)
