from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Draggable").click()

driver.implicitly_wait(5)

dragBox = driver.find_element_by_id('draggable')

ActionChains(driver).click_and_hold(dragBox).move_by_offset(50,50).release().perform()

driver.close()