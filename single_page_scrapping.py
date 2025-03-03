# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

# REQUEST THE JUMIA APPLIANCES WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("https://www.jumia.com.ng/mlp-appliances/")

# USE BEAUTIFULSOUP TO PARSE THE HTML CONTENT OF THE JUMIA WEBPAGE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# FIND ALL THE APPLIANCE NAMES ON THE PAGE WITH A CLASS ATTRIBUTE OF 'name'
appliances = soup.findAll("div", attrs={"class": "name"})

# FIND ALL THE APPLIANCE PRICES ON THE PAGE WITH A CLASS ATTRIBUTE OF 'prc'
prices = soup.findAll("div", attrs={"class": "prc"})

# LOOP THROUGH BOTH APPLIANCES AND PRICES USING THE 'ZIP' FUNCTION
# THEN PRINT AND FORMAT THE RESULTS
for appliances, prices in zip(appliances, prices):
    print(f"{appliances.text.strip()} - {prices.text.strip()}")
