from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Droppable").click()

dragItem = driver.find_element_by_id('draggable')
dropItem = driver.find_element_by_id('droppable')

try:
    assert driver.find_element_by_css_selector('#droppable').text == 'Drop here'
except Exception as e:
    print(e)

ActionChains(driver).click_and_hold(dragItem).move_to_element(dropItem).move_by_offset(0,10).release().perform()

try:
    assert driver.find_element_by_css_selector('#droppable').text == "Dropped!"
    assert driver.find_element_by_css_selector('#droppable').value_of_css_property('background') == '#fffa90'
except Exception as e:
    print(e)


driver.close()