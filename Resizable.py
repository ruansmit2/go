from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Resizable").click()

initialWidth = driver.find_element_by_css_selector('#resizable').value_of_css_property('width')
initialHeight = driver.find_element_by_css_selector('#resizable').value_of_css_property('height')

yAxis = driver.find_element_by_css_selector('#resizable > div.ui-resizable-handle.ui-resizable-e')
xAxis = driver.find_element_by_css_selector('#resizable > div.ui-resizable-handle.ui-resizable-s')

ActionChains(driver).click_and_hold(yAxis).move_by_offset(50,50).release().perform()
ActionChains(driver).click_and_hold(xAxis).move_by_offset(50,50).release().perform()

newWidth = driver.find_element_by_css_selector('#resizable').value_of_css_property('width')
newHeight = driver.find_element_by_css_selector('#resizable').value_of_css_property('height')

try:
    assert initialWidth != newWidth
    assert initialHeight != newHeight
except Exception as e:
    print(e)

driver.close()
