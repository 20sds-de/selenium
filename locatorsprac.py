from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Shalini/PycharmProjects/Selenium/locators.html")
driver.maximize_window()

user = driver.find_element(By.ID, "user")
assert user.is_displayed()

input_field = driver.find_element(By.CLASS_NAME, "input_field")
assert input_field.is_enabled()

inputs =driver.find_elements(By.TAG_NAME, "input")
assert len(inputs) == 2

forgot = driver.find_element(By.LINK_TEXT,"Forgot Password")
assert forgot.text == "Forgot Password"
assert forgot.is_displayed

partial= driver.find_element(By.PARTIAL_LINK_TEXT, "Password")
assert "Password" in partial.text

#css selector by id, name, class, attribute, class+tag
driver.find_element(By.CSS_SELECTOR, "#user")
driver.find_element(By.CSS_SELECTOR, ".input_field")
driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Enter password']")
css_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.primary")
assert css_btn.text == "Login"

#xpath by attribute, contains, text, parent->child,sibling

xpath_id = driver.find_element(By.XPATH, "//input[@id = 'user']") 
assert xpath_id.get_attribute("name") == "username"

xpath_contains= driver.find_element(By.XPATH,"//input[contains(@placeholder,'username')]")
assert "username" in xpath_contains.get_attribute("placeholder")
driver.find_element(By.XPATH, "//li[text()='T-Shirt']")
xpath_parent_child = driver.find_element(By.XPATH, "//div[@id='login-box']/input")
assert xpath_parent_child.get_attribute("id") == "user"
driver.find_element(By.XPATH, "//label[text()='Username']/following-sibling::input")

print("all asserions passed")
