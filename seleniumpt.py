from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Shalini/PycharmProjects/Selenium/form.html")

#radio button select
title = driver.find_element(By.ID, "title").text
title = "Selenium Practice html file"

hindi_radio = driver.find_element(By.ID, "hindi")
hindi_radio.click()

assert hindi_radio.is_selected()

#dropdown select by text
country_dropdown = Select(driver.find_element(By.ID, "country"))
#select by text
country_dropdown.select_by_visible_text("United States")

#assert
option1 = country_dropdown.first_selected_option.text
assert option1 == "United States"
print("country assertion passed")

print("assertion passed")

#dropdown select by value
country_dropdown.select_by_value("IN")
option2 = country_dropdown.first_selected_option.text
assert option2 == "India"

#dropdown multi select in country

country_dropdown.select_by_visible_text("United Kingdon")
country_dropdown.select_by_visible_text("Canada")

selected = [option.text for option in country_dropdown.all_selected_options]

assert "United Kingdom" in selected
assert "canada" in selected

assert "India" not in selected

print("value country assertion passed")