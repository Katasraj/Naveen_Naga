from WebdriverManager import Driver_Load
from selenium.webdriver.common.by import By
import time

l =  Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")

print("Title of the Page: ",driver.title)

linkslist = driver.find_elements(By.TAG_NAME,'a')
print("Total Links: ",len(linkslist))

for ele in linkslist:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))

imglist = driver.find_elements(By.TAG_NAME,'img')
print("Total No Of Images: ",len(imglist))

for img in imglist:
    print(img.get_attribute('src'))