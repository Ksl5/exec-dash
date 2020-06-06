# dashboard_generator.py
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from operator import itemgetter
import itertools

def to_usd(my_price):
   return f"${my_price:,.2f}" #> $12,000.71

#selected_report = csv_filename
#CSV_FILENAME = input("Please enter date of monthly sales report (sales-YYYYMM.csv): ")

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data/monthly-sales", CSV_FILENAME)
total_sale = 0
rows = []

with open(csv_filepath, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        
        total_sale = total_sale + float(row["sales price"])
    
        rows.append(dict(row)) 

product_sales = []

sorted_rows = sorted(rows, key=itemgetter("product"))
rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product")) 

for product, product_rows in rows_by_product:
    monthly_sales = sum([float(row["sales price"]) for row in product_rows])
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:3] # first three items in a list  
top_sellers.reverse()        
parsed_date = datetime.strptime(row["date"], "%Y-%m-%d")        
 
print("-----------------------")
month = parsed_date.strftime("%B")
year = parsed_date.year
print(f"SALES REPORT!")
print(f"MONTH: {month} {year}")
print("-----------------------")
print("CRUNCHING THE DATA...")
print("-----------------------")

print("Total Monthly Sales: " + to_usd(total_sale))

print("-----------------------")
print("TOP SELLING PRODUCTS:")
rows = []
cols = []
counter = 0
for top_seller in top_sellers:
    counter = counter + 1
    product_name = top_seller["name"]
    sales_usd = to_usd(top_seller["monthly_sales"])
    print(f"  {counter}. {product_name} {sales_usd}")
    rows.append(product_name)
    cols.append(top_seller["monthly_sales"])
print("-----------------------")
print("VISUALIZING THE DATA...")
#TODO bar chart
#TODO error message
#plt.style.use('ggplot')





#bar_value = [gen[product_name] for gen in product_name]
#bar_labels = [gen[sales_usd] for gen in sales_usd]


#bar_labels = [product_name] 
#bar_value = [sales_usd] 
#
#plt.barh(bar_labels, bar_value, align='center')
#plt.show()

#bar_data = sorted_product_sales[0:10]
#bar_data = {product_name, sales_usd}
#bar_data = f"  {counter}. {product_name} {sales_usd}"


#x = [dat[sales_usd]for dat in bar_data]
#product = [dat[product_name]for dat in bar_data]
#x = top_sellers
#x = [p [product_name] for p in product_name]
#y = [s [sales_usd] for s in sales_usd]



plt.barh(rows, cols, color='blue')

plt.xlabel("Sales USD")
plt.ylabel("Product")
plt.title("Top-selling Products This Month")
numbers = [1000, 2000, 3000]
labels =  [to_usd(x) for x in numbers]
plt.xticks(numbers, labels)
#plt.xticks([1000,2000], ["one thousand", "two thousand"])
a = [1]
plt.show()

#bar_data = top_sellers
#x = [dat["product"]for dat in bar_data]
#Salesprice = [dat["sales price"]for dat in bar_data]

#bar_value = [gen["product"] for gen in bar_data]
#bar_labels = [gen["sales price"] for gen in bar_data]
#plt.barh(bar_labels, bar_value, align='center')
#plt.show()