from WebdriverManager import Driver_Load
from selenium.webdriver.common.by import By
import time

l =  Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://app.hubspot.com/login")

print("Title of the Page: ",driver.title)

driver.find_element(By.CSS_SELECTOR,"#username").send_keys("naga45@gmail.com")


# time.sleep(10)
# driver.quit()