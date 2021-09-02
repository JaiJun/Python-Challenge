import selenium
from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("http://www.google.com")
# 定位搜尋框
element = driver.find_element_by_class_name("gLFyf.gsfi")
# 傳入字串
element.send_keys("Selenium Python")

#點擊搜尋按鈕
button = driver.find_element_by_class_name("gNO89b")
button.click()