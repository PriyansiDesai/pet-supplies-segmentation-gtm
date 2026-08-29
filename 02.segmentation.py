import pandas as pd

df = pd.read_csv('pet_supplies_eda_ready.csv')

priced = df[df['price_clean'].notnull()].copy()

# Percentile-based cutoffs (33rd / 66th) — creates roughly equal-sized tiers
q33, q66 = priced['price_clean'].quantile([0.33, 0.66])
print(f"Tier cutoffs -> Budget: <₹{q33:.0f} | Mid: ₹{q33:.0f}-₹{q66:.0f} | Premium: >₹{q66:.0f}")

def assign_tier(price):
    if price < q33:
        return 'Budget'
    elif price < q66:
        return 'Mid'
    else:
        return 'Premium'

priced['price_tier'] = priced['price_clean'].apply(assign_tier)

print("\nOverall tier counts:")
print(priced['price_tier'].value_counts())

print("\nTier distribution by animal type (crosstab):")
print(pd.crosstab(priced['animal_type'], priced['price_tier']))

print("\nTier distribution by animal type (% within each animal, easier to compare):")
print(pd.crosstab(priced['animal_type'], priced['price_tier'], normalize='index').round(2) * 100)

priced.to_csv('pet_supplies_segmented.csv', index=False)