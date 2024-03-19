from RetailSalesAnalyzer import RetailSalesAnalyzer

analizer = RetailSalesAnalyzer()
analizer.clean_data()

print('Total Sales by Product: ', analizer.total_sales_by_product())
print('Best Selling Products: ', analizer.best_selling_product())
print('Average Daily Sales: ', analizer.average_daily_sales())
analizer.plot_sales_trend()
analizer.plot_sales_by_product()
analizer.plot_sales_per_product()