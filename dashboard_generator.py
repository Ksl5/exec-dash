# dashboard_generator.py
import csv
import os

def to_usd(my_price):
   return f"${my_price:,.2f}" #> $12,000.71

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data/monthly-sales", CSV_FILENAME)
#csv_filepath = "data/monthly-sales/sales-201803.csv"
total_sale = 0

with open(csv_filepath, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        #print(row["sales price"])
        total_sale = total_sale + float(row["sales price"])
        



print("-----------------------")
month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values
print(f"SALES REPORT!")
print(f"MONTH: {month} {year}")

print("MONTH: March 2018")

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