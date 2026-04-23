import pandas as pd

data = {
    'Car': [
        'Nissan GT-R R33',
        'Mercedes Maybach GLS 600',
        'Porsche Carrera GT',
        'Ferrari 296 GTB',
        'McLaren 750S',
        'BAC Mono R',
        'Lamborghini Revuelto',
        'BMW M3 Competition',
        'Lotus Emira',
        'Lamborghini Murcielago SV',
        'McLaren P1',
        'Lexus LFA',
        'Ferrari 812 Superfast',
        'Bugatti Chiron Pur Sport',
        'Pagani Huayra Roadster',
        'Ferrari 488 Pista',
        'Mercedes G63 AMG',
        'Apollo IE',
        'Pininfarina Battista',
        'Hennessey Venom F5'
    ],
    'Price': [
        55000, 180000, 2200000, 370000,
        400000, 300000, 700000, 125000,
        100000, 900000, 2200000, 850000,
        450000, 5000000, 3900000, 800000,
        265000, 3500000, 3500000, 3200000
    ]
}

df = pd.DataFrame(data)
print(df.to_string())
print("\nTotal Dream Garage Cost: $", df['Price'].sum())
print("Most Expensive:", df.loc[df['Price'].idxmax(), 'Car'])
print("Cheapest:", df.loc[df['Price'].idxmin(), 'Car'])
# Add savings tracker
monthly_savings = 500  # in dollars (change this later)
total_cost = df['Price'].sum()
months_needed = total_cost / monthly_savings
years_needed = months_needed / 12

print("\n--- GARAGE SAVINGS TRACKER ---")
print(f"Total Cost: ${total_cost:,}")
print(f"Monthly Savings: ${monthly_savings:,}")
print(f"Years to garage: {years_needed:.1f} years")

# Affordable first
print("\n--- BUY ORDER (cheapest first) ---")
print(df.sort_values('Price')[['Car','Price']].to_string())