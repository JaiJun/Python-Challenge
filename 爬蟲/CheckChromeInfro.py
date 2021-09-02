from selenium import webdriver
from selenium.webdriver.common.by import By

# 透過Browser Driver 開啟 Chrome
driver = webdriver.Chrome(r"C:\chromedriver.exe")
# 前往特定網址
default_url = "https://www.google.com.tw"
driver.get(default_url)

# 獲取目前網頁url
url = driver.current_url
print(url)

