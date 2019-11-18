from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Selectable").click()

resultSet = driver.find_element_by_xpath('//*[@id="selectable"]')
options = resultSet.find_elements_by_tag_name("li")

options[1].click()

try:
    assert options[1] == driver.find_element_by_css_selector('#selectable > li.ui-widget-content.ui-selectee.ui-selected'), "Item 2 was not selected"
except Exception as e:
    print(e)

ActionChains(driver).key_down(Keys.CONTROL).click(options[3]).key_up(Keys.CONTROL).perform()

try:
    assert driver.find_element_by_css_selector('#selectable > li:nth-child(2)').value_of_css_property('background-color') == '#F39814'
    assert driver.find_element_by_css_selector('#selectable > li:nth-child(4)').value_of_css_property('background-color') == '#F39814'
except Exception as e:
    print(e)

driver.close()


