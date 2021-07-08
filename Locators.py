from WebdriverManager import Driver_Load
from selenium.webdriver.common.by import By
import time

l =  Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)
username_url = driver.find_element(By.ID,"Form_submitForm_subdomain")
first_name = driver.find_element(By.ID,"Form_submitForm_FirstName")
last_name = driver.find_element(By.ID,"Form_submitForm_LastName")
email = driver.find_element(By.ID,"Form_submitForm_Email")
platform_link = driver.find_element(By.LINK_TEXT,"Platform")

username_url.send_keys("naveenautomationlabs")
first_name.send_keys("Naveen")
last_name.send_keys("automationlabs")
email.send_keys("naveen@gmail.com")
platform_link.click()
