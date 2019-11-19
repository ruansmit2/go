from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Automation Practice Switch Windows").click()

driver.implicitly_wait(5)

driver.find_element_by_id('button1').click()

nbwHandles = driver.window_handles
driver.switch_to.window(nbwHandles[1])

try:
    assert 'https://www.toolsqa.com/' == driver.current_url, "Page did not redirect"
except Exception as f:
    print(f)

driver.close()

driver.switch_to.window(nbwHandles[0])

driver.close()

