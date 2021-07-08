#https://www.youtube.com/watch?v=--eR5HdhTxY&list=WL&index=4&t=304s
#https://github.com/rahulrsr/STET1-PytestAutomation/blob/master/xpath.json

from WebdriverManager import Driver_Load
import time

l = Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.get("http://www.tutorialsninja.com/demo/")

# driver.find_element_by_link_text("My Account").click()
# driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()

driver.find_element_by_xpath("//*[@title='My Account']").click()
driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()
driver.find_element_by_id("input-firstname").send_keys("TestSTET1")
driver.find_element_by_id("input-lastname").send_keys("LastSTET1")
driver.find_element_by_id("input-email").send_keys("LastSTET1@gmail.com")
driver.find_element_by_id("input-telephone").send_keys("9600124694")
driver.find_element_by_id("input-password").send_keys("Test1@123")
driver.find_element_by_id("input-confirm").send_keys("Test1@123")
driver.find_element_by_name("agree").click()
driver.find_element_by_xpath("//input[@value='Continue']").click()

msg = driver.find_element_by_xpath("//div[@id='content']/h1").text
print(msg)
assert msg=="Your Account Has Been Created!"

# time.sleep(5)
# driver.quit()