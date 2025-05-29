import pandas as pd
import numpy as np

# Define 15 sectors with 2–3 industries each
sector_industry_map = {
    'Technology': ['Software', 'Hardware', 'Semiconductors'],
    'Healthcare': ['Pharmaceuticals', 'Medical Devices', 'Biotech'],
    'Finance': ['Banking', 'Insurance', 'Asset Management'],
    'Consumer': ['Retail', 'Food & Beverage', 'Apparel'],
    'Energy': ['Oil & Gas', 'Renewables', 'Utilities'],
    'Industrials': ['Aerospace', 'Machinery', 'Construction'],
    'Materials': ['Metals & Mining', 'Chemicals', 'Packaging'],
    'Real Estate': ['Commercial RE', 'Residential RE'],
    'Telecommunications': ['Wireless Services', 'Broadband'],
    'Transportation': ['Airlines', 'Logistics', 'Rail'],
    'Media': ['Publishing', 'Broadcasting', 'Streaming'],
    'Education': ['EdTech', 'Tutoring', 'Institutions'],
    'Hospitality': ['Hotels', 'Restaurants', 'Travel'],
    'Agriculture': ['Farming', 'Agribusiness', 'AgTech'],
    'Automotive': ['OEMs', 'Parts Suppliers', 'EV Manufacturers']
}

# Reverse map from industry to sector
industry_to_sector = {industry: sector for sector, industries in sector_industry_map.items() for industry in industries}

# Sample sizes and buckets
sizes = ['Micro', 'Small', 'Mid', 'Large']
buckets = [1,2,3,4]
countries = ["USA", "FRA", "JPN", "ITA"]

# Expanded reasons list (32 reasons)
reasons = [
    'High Growth', 'Low Leverage', 'Sector Tailwinds', 'Strong Management',
    'Undervalued', 'Improving Margins', 'New Product Launch', 'Market Leader',
    'Cost Efficiency', 'Diversified Revenue', 'Positive Guidance', 'Low Capex',
    'Regulatory Approval', 'Patent Portfolio', 'Recurring Revenue',
    'Technological Edge', 'M&A Potential', 'Global Expansion', 'Turnaround Plan',
    'High Free Cash Flow', 'Share Buyback', 'Dividend Growth', 'Experienced Team',
    'Strong Brand', 'Low Competition', 'Growing TAM', 'Sticky Customers',
    'Rising Demand', 'Operational Leverage', 'Favorable FX Trends',
    'Low Customer Churn', 'Capital Light Model'
]

# Number of rows
n = 1000  # Can be changed as needed

# Set seed and generate base data
np.random.seed(1)
industries = np.random.choice(list(industry_to_sector.keys()), size=n)
df = pd.DataFrame({
    'ID': [f'C{i:03d}' for i in range(1, n+1)],
    'Size': np.random.choice(sizes, size=n),
    'Industry': industries,
})
df['Country'] = np.random.choice(countries, size=n)
df['Sector'] = df['Industry'].map(industry_to_sector)
df['Propensity'] = np.random.choice(buckets, size=n)

# Assign unique reasons to each row
def get_unique_reasons():
    return np.random.choice(reasons, size=3, replace=False)

df[['Reason1', 'Reason2', 'Reason3']] = [get_unique_reasons() for _ in range(n)]

df.to_csv(f"sample_output.csv", index = False)