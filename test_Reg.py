from WebdriverManager import Driver_Load
import pytest
l = Driver_Load("chrome")
driver = l.Driver_Definition()

@pytest.mark.skip
def test_registration_form():

    driver.maximize_window()
    driver.get("http://www.tutorialsninja.com/demo/")

    # driver.find_element_by_link_text("My Account").click()
    # driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()

    driver.find_element_by_xpath("//*[@title='My Account']").click()
    driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()
    driver.find_element_by_id("input-firstname").send_keys("TestSTET2")
    driver.find_element_by_id("input-lastname").send_keys("LastSTET2")
    driver.find_element_by_id("input-email").send_keys("LastSTET2@gmail.com")
    driver.find_element_by_id("input-telephone").send_keys("9600124695")
    driver.find_element_by_id("input-password").send_keys("Test2@123")
    driver.find_element_by_id("input-confirm").send_keys("Test2@123")
    driver.find_element_by_name("agree").click()
    driver.find_element_by_xpath("//input[@value='Continue']").click()

    msg = driver.find_element_by_xpath("//div[@id='content']/h1").text
    print(msg)
    assert msg=="Your Account Has Been Created!"


#test_registration_form()