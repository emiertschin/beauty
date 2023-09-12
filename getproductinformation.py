from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.read_csv("sephora_body_urlsonly.csv", usecols=['body_URLS']) # can also index sheet by name or fetch all sheets
print(df)

whatitis=[]
concerns=[]
ingrhigh=[]
abt=[]
urls=[]
for url in df['body_URLS']:
    driver.get(url)
    urls.append(url)
    print(url)
    try:
        abt1=driver.find_element(By.XPATH,"//div[@class='css-32uy52 eanm77i0']").text
    except NoSuchElementException:
        abt1 = ''
        print('not found')
    abt.append(abt1)
    
    lines = abt1.splitlines()

    ws=''
    for line in lines:
        if "What it is" in line:
            ws=line
        elif "Skincare Concerns" not in line:
            ws=ws+line
        elif "Skincare Concerns" in line:
            break
    whatitis.append(ws)

    conc=''
    for line in lines:
        if "Skincare Concerns" in line:
            conc=line
        elif "Highlighted Ingredients" not in line:
            conc=conc+line
        elif "Highlighted Ingredients" in line:
            break
    concerns.append(conc)

    ih=''
    for line in lines:
        if "Highlighted Ingredients" in line:
            ih=line
        elif "Show more" not in line:
            ih=ih+line
        elif "Show more" in line:
            break
    ingrhigh.append(ih)

print(len(urls),len(abt),len(whatitis),len(concerns),len(ingrhigh))

data = {'url':urls,
        'about':abt,
        'What it is':whatitis,
        'Skincare concerns':concerns,
        'Highlighted ingredients':ingrhigh}

df_ingr = pd.DataFrame(data)
df_ingr.to_csv('sephora_body.csv',index=False)