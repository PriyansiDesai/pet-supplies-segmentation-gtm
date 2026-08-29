import pandas as pd

df = pd.read_csv('amazon_pet_supplies_dataset_sample.csv')

# Price: strip commas, convert to numeric
df['price_clean'] = df['price'].astype(str).str.replace(',', '', regex=False)
df['price_clean'] = pd.to_numeric(df['price_clean'], errors='coerce')

# Brand: strip "Brand: " prefix
df['brand'] = df['brand'].astype(str).str.replace('Brand: ', '', regex=False)

# Breadcrumbs -> animal_type, product_type
crumbs = df['breadcrumbs'].astype(str).str.split(' | ', regex=False, expand=True)
df['animal_type'] = crumbs[1]
df['product_type'] = crumbs[2]

# Keep only the columns we finalized for EDA
keep_cols = ['title', 'price_clean', 'brand', 'animal_type', 'product_type', 'availability']
df = df[keep_cols].copy()

# Save cleaned version so you don't have to redo this step later
df.to_csv('pet_supplies_eda_ready.csv', index=False)


print("=" * 50)
print("SHAPE & NULLS")
print("=" * 50)
print("Shape:", df.shape)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("ANIMAL TYPE DISTRIBUTION")
print("=" * 50)
print(df['animal_type'].value_counts())
print((df['animal_type'].value_counts(normalize=True).round(3) * 100).astype(str) + " %")

print("\n" + "=" * 50)
print("PRODUCT TYPE DISTRIBUTION (top 10)")
print("=" * 50)
print(df['product_type'].value_counts().head(10))

print("\n" + "=" * 50)
print("PRICE DISTRIBUTION (INR)")
print("=" * 50)
print(df['price_clean'].describe().round(1))

print("\n" + "=" * 50)
print("TOP 10 BRANDS BY PRODUCT COUNT")
print("=" * 50)
print(df['brand'].value_counts().head(10))

print("\n" + "=" * 50)
print("AVG PRICE BY ANIMAL TYPE")
print("=" * 50)
print(df.groupby('animal_type')['price_clean'].agg(['mean', 'median', 'count']).round(1))

print("\n" + "=" * 50)
print("AVAILABILITY (non-null values only)")
print("=" * 50)
print(df['availability'].value_counts().head(10))