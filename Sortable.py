from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Sortable").click()

driver.implicitly_wait(5)

#Move item 1 to where item 2 is located
item1 = driver.find_element_by_xpath('//*[@id="sortable"]/li[1]')
item2 = driver.find_element_by_xpath('//*[@id="sortable"]/li[2]')
ActionChains(driver).click_and_hold(item1).move_to_element(item2).move_by_offset(0,10).release().perform()

#Move item 7 to where item 6 is located
item7 = driver.find_element_by_xpath('//*[@id="sortable"]/li[7]')
item6 = driver.find_element_by_xpath('//*[@id="sortable"]/li[6]')
ActionChains(driver).click_and_hold(item7).move_to_element(item6).move_by_offset(0,10).release().perform()

resultSet = driver.find_element_by_xpath('//*[@id="sortable"]')
options = resultSet.find_elements_by_tag_name("li")

try:
    assert "Item 2" == options[0].text, "List did not sort correctly"
    assert "Item 6" == options[-1].text,  "List did not sort correctly"
except Exception as e:
    print(e)

driver.close()



