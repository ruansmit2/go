from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("Automation Practice Switch Windows").click()

driver.implicitly_wait(5)
driver.find_element_by_id('alert').click()
alert = driver.switch_to.alert

try:
    assert 'Knowledge' in alert.text, "Page did not give alert"
    alert.accept()
except Exception as f:
    print(f)

driver.close()


