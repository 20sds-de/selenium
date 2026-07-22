from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Shalini/PycharmProjects/Selenium/form.html")


title = driver.find_element(By.ID, "title").text
title = "Selenium Practice html file"

hindi_radio = driver.find_element(By.ID, "hindi")
hindi_radio.click()

assert hindi_radio.is_selected()

print("assertion passed")