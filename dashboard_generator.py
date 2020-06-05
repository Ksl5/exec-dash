# dashboard_generator.py
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from operator import itemgetter



def to_usd(my_price):
   return f"${my_price:,.2f}" #> $12,000.71

#selected_report = csv_filename
CSV_FILENAME = input("Please enter date of monthly sales report (sales-YYYYMM.csv): ")

#CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data/monthly-sales", CSV_FILENAME)
#csv_filepath = "data/monthly-sales/sales-201803.csv"
total_sale = 0

with open(csv_filepath, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        
        total_sale = total_sale + float(row["sales price"])
        #print(row["product"][2], row["sales price"][2])
        #print(row["date"])
        
        #top_product = row["product"]
        #unique_products = set(top_product)
        #print (unique_products)
        #print(top_product)    
        #bar_data = [
#plt.style.use('ggplot')
#print(row["date"])
#2018-03-06
parsed_date = datetime.strptime(row["date"], "%Y-%m-%d")


#print(str(report_month).strftime("%Y-%m"))
#print(date)

#x = [dat["product"]for dat in bar_data]
#Viewers = [dat["sales price"]for dat in bar_data]
#
#bar_value = [gen["viewers"] for gen in bar_data]
#bar_labels = [gen["genre"] for gen in bar_data]
#plt.barh(bar_labels, bar_value, align='center')
#plt.show()



print("-----------------------")
month = parsed_date.strftime("%B")
year = parsed_date.year
print(f"SALES REPORT!")
print(f"MONTH: {month} {year}")


print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")

print("Total Monthly Sales: " + to_usd(total_sale))
#print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

