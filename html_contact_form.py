from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.demoqa.com/")
driver.maximize_window()

driver.find_element_by_link_text("HTML contact form").click()

firstName = driver.find_element_by_class_name('firstname')
lastName = driver.find_element_by_id('lname')
country = driver.find_element_by_name('country')
googleLink = driver.find_elements_by_partial_link_text('Google')
subject = driver.find_element_by_css_selector('#subject').clear()
driver.find_element_by_css_selector('#subject').send_keys("Test Text")
submit = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/form/input[4]')

firstName.send_keys('Ruan')
lastName.send_keys('Smit')
country.send_keys('South Africa')

ActionChains(driver).key_down(Keys.CONTROL).click(googleLink[0]).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(googleLink[1]).perform()

submit.click()
driver.implicitly_wait(5)

try:
    assert 'onsubmitform' in driver.current_url, "Page did not redirect"
except Exception as e:
    print(e)
try:
    assert len(driver.window_handles) == 4, "More or less tabs are open"
except Exception as f:
    print(f)

driver.quit()