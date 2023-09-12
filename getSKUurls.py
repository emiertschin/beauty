from bs4 import BeautifulSoup
import csv

# Your HTML code here
html_code = """
#insert here for manual pull
"""

# Parse the HTML code using Beautiful Soup
soup = BeautifulSoup(html_code, 'html.parser')

# Find all product elements
class_x = soup.find_all("div", class_="ProductCard")

# Locate the containers with class Y
#class_y = soup.find_all("div", class_="css-1qe8tjm")

# Combine the containers from both class X and class Y
product_elements = class_x

# Initialize a list to store product data
product_data = []

# Extract information for each product element
for order_number, product_element in enumerate(product_elements):
    product_name = product_element.find('a', class_='ProductCard__Title').text.strip()
    brand = product_element.find('div', class_='ProductCard__Brand').text.strip()
    price = product_element.find('div', class_='ProductCard__Price')
    if price:
        product_price = price.text.strip()
    else:
        product_price = "N/A"  # Or any other placeholder
    
    # Store data in a dictionary
    product_dict = {
        'Order #': order_number + 1,  # Adding 1 to start order numbers from 1
        'Product Name': product_name,
        'Brand': brand,
        'Price': product_price
    }
    
    product_data.append(product_dict)

# Sort product data by order number
sorted_product_data = sorted(product_data, key=lambda x: x['Order #'])

# Print the sorted data (you can format it as a table or export as needed)
for item in sorted_product_data:
    print(item)

# Define the CSV file's name
#csv_file = "product_data.csv"

#with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
#    writer = csv.writer(file)
#    writer.writerows(brand)

#print("Data has been saved to", csv_file)


