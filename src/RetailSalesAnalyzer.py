import pandas as pd
import matplotlib.pyplot as plt


class RetailSalesAnalyzer():
    def __init__(self):
        self.data = pd.read_csv(
            './retail_sales.csv')
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def clean_data(self):
        self.data.dropna(inplace=True)

    def total_sales_by_product(self):
        return self.data.groupby('Product')['Sales'].sum()

    def best_selling_product(self):
        return self.total_sales_by_product().sort_values(ascending=False).index[0]

    def average_daily_sales(self):
        return self.data['Sales'].mean()

    def plot_sales_trend(self):
        self.data.groupby('Date')['Sales'].sum().plot(kind='line')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.legend()
        plt.show()

    def plot_sales_by_product(self):
        self.total_sales_by_product().plot(kind='bar')
        plt.title('Sales By Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.legend()
        plt.show()
    
    def plot_sales_per_product(self):
        products = self.data['Product'].unique()
        sales=self.total_sales_by_product()
        fig, ax = plt.subplots()
        bar_container = ax.bar(products, sales)
        ax.set(ylabel='Sales', title='Sales By Product')
        ax.bar_label(bar_container, fmt='{:,.0f}')
        plt.show()
