import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

def load_and_clean_data(file_path):
    """Responsibility: Load data and fix column types for better plotting."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing {file_path}! Please ensure it is named 'dataset.csv'.")
    
    df = pd.read_csv(file_path)
    df['Hour'] = pd.to_datetime(df['Time']).dt.hour
    df.columns = df.columns.str.strip()
    # Keeping your original subset list exactly as requested
    df = df.dropna(subset=['Total', 'Rating', 'Product lin', 'Customer', 'Payment'])
    
    return df

def analytics_graphs(df):
    """Responsibility: Create 5 professional, non-redundant visualizations."""
    
    sns.set_theme(style="whitegrid")
    if not os.path.exists('output'):
        os.makedirs('output')
    
    print("🎨 Creating your diverse business dashboard...")

    # --- GRAPH 1: Peak Hour Line Chart ---
    plt.figure(figsize=(10, 5))
    hourly_sales = df.groupby('Hour')['Total'].sum().reset_index()
    sns.lineplot(x='Hour', y='Total', data=hourly_sales, marker='o', color='#FF5733', linewidth=2.5)
    plt.fill_between(hourly_sales['Hour'], hourly_sales['Total'], color='#FF5733', alpha=0.1)
    plt.title('1. Store Traffic: Peak Sales Hours', fontsize=14, fontweight='bold')
    plt.xticks(range(10, 21))
    plt.savefig('output/1_peak_hours.png', dpi=300, bbox_inches='tight')
    plt.close() # Added to free memory

    # --- GRAPH 2: Category King (Horizontal Bar) ---
    plt.figure(figsize=(10, 6))
    category_sales = df.groupby('Product lin')['Total'].sum().sort_values(ascending=False).reset_index()
    sns.barplot(x='Total', y='Product lin', data=category_sales, hue='Product lin', palette='mako', legend=False)
    plt.title('2. Revenue by Product Category', fontsize=14, fontweight='bold')
    sns.despine(left=True, bottom=True)
    plt.savefig('output/2_product_performance.png', dpi=300, bbox_inches='tight')
    plt.close()

    # --- GRAPH 3: Member vs. Normal (Grouped Bar) ---
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Branch', y='Total', hue='Customer', data=df, estimator=sum, errorbar=None, palette='pastel')
    plt.title('3. Member vs. Normal Spending by Branch', fontsize=14, fontweight='bold')
    plt.legend(title='Customer Status', frameon=True)
    plt.savefig('output/3_customer_loyalty.png', dpi=300, bbox_inches='tight')
    plt.close()

    # --- NEW GRAPH 4: Payment Method ---
    plt.figure(figsize=(8, 8))
    payment_counts = df['Payment'].value_counts()
    colors = sns.color_palette('Set3')[0:len(payment_counts)]
    plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', 
            startangle=140, colors=colors, pctdistance=0.85, explode=[0.03]*len(payment_counts))
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    plt.gca().add_artist(centre_circle)
    plt.title('4. Most Popular Payment Methods', fontsize=14, fontweight='bold', pad=15)
    plt.savefig('output/4_payment_donut.png', dpi=300, bbox_inches='tight')
    plt.close()

    # --- GRAPH 5: City Rivalry (KDE Density Plot) ---
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x="Total", hue="City", fill=True, common_norm=False, palette="viridis", alpha=.5, linewidth=0)
    plt.title('5. Sales Density Distribution by City', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Sale Amount (Total)')
    plt.ylabel('Density of Sales')
    plt.savefig('output/5_city_sales_density.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Success! Your 5 unique business insights are ready.")

    # --- DOCKER PROOF SECTION (Added for your terminal screenshot) ---
    print("\n--- DOCKER CONTAINER IMAGE CHECK ---")
    if os.path.exists('output'):
        files = os.listdir('output')
        print(f"Verified: {len(files)} images found in the output directory:")
        for i, file in enumerate(sorted(files), 1):
            print(f" [{i}] {file}")
    print("--------------------------------------\n")

if __name__ == "__main__":
    try:
        supermarket_data = load_and_clean_data('dataset.csv')
        analytics_graphs(supermarket_data)
    except Exception as e:
        print(f"❌ Error: {e}")