from WebdriverManager import Driver_Load
from selenium.webdriver.common.by import By
import time

l =  Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.freshworks.com/")

print("Title of the Page: ",driver.title)

header_element = driver.find_element(By.TAG_NAME,"h1")
print(header_element.text)