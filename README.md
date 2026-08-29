# Premium Pet Accessories — Segmentation & GTM Sizing (India E-Commerce)

## Overview
This project looks at 343 pet product listings scraped from Amazon.in to figure out which pet product segment is worth targeting for an online launch in India. I cleaned and explored the data, segmented products by animal type and price, then built a market size estimate from scratch instead of relying on a single industry report.

## Main finding
The products listed on Amazon.in don't match how pet ownership actually looks in India. Dogs are the most commonly owned pet by a wide margin, but they're only 1% of the listings in this dataset. Food, usually the biggest spending category in pet care, is outnumbered by toys and accessories. So this catalog is really an accessories-and-non-dog market, not a full picture of pet spending in India.

That gap is the reason I focused the rest of the analysis on cats and premium accessories, since that's the segment the data actually has enough evidence for.

## What I did
1. Cleaned the raw data — prices had commas and inconsistent formatting, brand names had extra text, and categories were buried in a single breadcrumb string that needed splitting
2. Ran EDA to see what categories, prices, and brands actually show up and how often
3. Segmented products by animal type and by price tier (Budget, Mid, Premium)
4. Built a bottoms-up TAM-SAM-SOM estimate using real Indian pet ownership numbers and this dataset's pricing
5. Compared that estimate against outside market research as a check
6. Wrote a specific recommendation based on what the data actually supports

## Key findings

**Category mix is skewed**
Dogs: 4 of 343 listings. Toys (82) outnumber Food (36). Prices are right-skewed — a handful of expensive listings pull the average up, so the median (₹969) is more representative than the mean (₹1,885).

**Brands are fragmented**
23% of listings are labeled just "Generic," and no single brand has a meaningful share. That usually points to room for a focused new entrant.

**Cats skew premium**
38% of cat listings fall in the top price tier — the highest of any category with a large enough sample to trust. Small Animals are similar (42%) but there are far fewer of them. Birds lean budget. Dogs had too few listings to draw a real conclusion, so I left that one out rather than force it.

## Market sizing

I built this bottoms-up instead of quoting a single market-size figure, partly because the reports I found disagreed with each other by close to 10x.

| | Definition | Value |
|---|---|---|
| TAM | All cat-owning households in India | ₹758 Cr (~$91M) |
| SAM | Of those, who buy online | ₹189 Cr (~$23M) |
| SOM | Of those, who'd buy premium products | ₹114 Cr (~$13.5M) |

![TAM SAM SOM market sizing funnel](tam_sam_som_chart.png)

This number sits below the broadest top-down industry estimates, which makes sense since cats are just one part of a much larger multi-species market. I'm treating this as a rough consistency check, not proof the number is exactly right.

## Recommendation

**Primary: Target premium cat accessories as the entry point.**
This is the segment the data actually supports — highest premium concentration among categories with a large enough sample (38%), lines up with the "pets as family" trend, and the competition is fragmented enough that a focused brand could stand out. ₹114 Cr SOM is a realistic number to work with.

**Considered but not recommended (yet):**

- **Dog products** — the largest real pet-ownership segment in India, but this dataset only has 4 dog listings, nowhere near enough to size or validate demand. Worth a separate, dedicated data pull before treating it as an opportunity.
- **Budget bird accessories** — the largest *volume* segment in this catalog (147 listings, mostly Budget tier), so it's tempting as a "quick scale" play. Ruled out for a premium/branded entrant specifically, since budget-tier, high-volume categories usually compete on price and logistics, not brand — a weaker fit for a new, differentiated player.

Premium cats is the pick because it's the only segment where the data, the trend research, and a viable competitive gap all point the same direction at once.

## Limitations
- 343 listings is a small sample, so these are directional findings, not a full market picture
- The purchase-frequency numbers used in sizing are partly assumptions, flagged above
- One field (product origin, relevant to the "Made in India" trend) was too inconsistent to use reliably in this timeframe — a good next step if this were extended

## Tools
Python (pandas) for cleaning, EDA, and segmentation. Manual TAM-SAM-SOM modeling, checked against secondary market research.
