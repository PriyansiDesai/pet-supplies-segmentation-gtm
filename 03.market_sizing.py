import pandas as pd

df = pd.read_csv('pet_supplies_segmented.csv')

# Sourced inputs
CAT_OWNING_HOUSEHOLDS_INDIA = 1_900_000   # Euromonitor, 2025
ECOMMERCE_ATTACH_RATE = 0.25              # TraceData Research, 2024
BASE_FREQUENCY_PER_YEAR = 4               # global pet e-commerce CLV benchmark, not India-specific
PREMIUM_FREQUENCY_PER_YEAR = 2            # assumption, not sourced

cats = df[df['animal_type'] == 'Cats']
cats_premium = df[(df['animal_type'] == 'Cats') & (df['price_tier'] == 'Premium')]

avg_price_cats_all = cats['price_clean'].median()
avg_price_cats_premium = cats_premium['price_clean'].median()
premium_share_cats = len(cats_premium) / cats['price_clean'].notnull().sum()

print(f"Cats — median price (all tiers): Rs{avg_price_cats_all:.0f}")
print(f"Cats — median price (Premium only): Rs{avg_price_cats_premium:.0f}")
print(f"Cats — Premium tier share: {premium_share_cats:.0%}")

# TAM
tam_population = CAT_OWNING_HOUSEHOLDS_INDIA
tam_revenue_per_customer = avg_price_cats_all * BASE_FREQUENCY_PER_YEAR
tam_value = tam_population * tam_revenue_per_customer

# SAM
sam_population = tam_population * ECOMMERCE_ATTACH_RATE
sam_revenue_per_customer = avg_price_cats_all * BASE_FREQUENCY_PER_YEAR
sam_value = sam_population * sam_revenue_per_customer

# SOM
som_population = sam_population * premium_share_cats
som_revenue_per_customer = avg_price_cats_premium * PREMIUM_FREQUENCY_PER_YEAR
som_value = som_population * som_revenue_per_customer

print("\n" + "=" * 50)
print("TAM-SAM-SOM (bottoms-up, INR)")
print("=" * 50)
print(f"TAM: {tam_population:,.0f} households x Rs{tam_revenue_per_customer:,.0f}/yr = Rs{tam_value/1e7:,.0f} Cr")
print(f"SAM: {sam_population:,.0f} households x Rs{sam_revenue_per_customer:,.0f}/yr = Rs{sam_value/1e7:,.0f} Cr")
print(f"SOM: {som_population:,.0f} households x Rs{som_revenue_per_customer:,.0f}/yr = Rs{som_value/1e7:,.0f} Cr")