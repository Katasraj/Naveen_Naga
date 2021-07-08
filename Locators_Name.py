from WebdriverManager import Driver_Load
from selenium.webdriver.common.by import By
import time

l =  Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://classic.crmpro.com/")

print("Title of the Page: ",driver.title)

username = driver.find_element(By.NAME,"username")
passwd = driver.find_element(By.NAME,"password")
login_btn = driver.find_element(By.XPATH,"//input[@type='submit']")

username.send_keys("batcautomation")
passwd.send_keys("Test@12345")
login_btn.click()

time.sleep(5)
driver.quit()