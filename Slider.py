from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Slider").click()

driver.implicitly_wait(5)

slider = driver.find_element_by_css_selector('#slider > span')

ActionChains(driver).click_and_hold(slider).move_by_offset(50,0).release().perform()

try:
    assert driver.find_element_by_css_selector('#slider > span').value_of_css_property('left') == "48.6563px", "Slider did not move or is not in the correct possition"
except Exception as f:
    print(f)

driver.close()
