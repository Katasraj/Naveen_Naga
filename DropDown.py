from WebdriverManager import Driver_Load
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

l =  Driver_Load("chrome")
driver = l.Driver_Definition()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print("Title of the Page: ",driver.title)

def select_values(element,value):
    select = Select(element)
    select.select_by_visible_text(value)

elm_industry = driver.find_element(By.ID,"Form_submitForm_Industry")
elm_country = driver.find_element(By.ID,"Form_submitForm_Country")

select_values(elm_industry,'Education')
select_values(elm_country,'India')
#select = Select(elm_industry)

#select.select_by_visible_text('Education')
#select.select_by_index(4)


#select_contry = Select(elm_country)
#select_contry.select_by_visible_text('India')

select = Select(elm_industry)
Industry_List = select.options

Industry_Options = []
for elm in Industry_List:
    Industry_Options.append(elm.text)
print(Industry_Options)

#Without Using Select
indus_options = driver.find_elements(By.XPATH,"//select[@id='Form_submitForm_Industry']/option")
print("Total Industrial Options: ",len(indus_options))
for elm_opt in indus_options:
    print(elm_opt.text)