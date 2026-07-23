from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expectcond

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Shalini/PycharmProjects/Selenium/xpath.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

user = wait.until(Expectcond.visibility_of_element_located((By.XPATH, "//input[@id='user']")))
user.send_keys("Shalini")

password = driver.find_element(By.XPATH, "//input[@id='pass']")
password.send_keys("mypassword")

login_btn = driver.find_element(By.XPATH, "//button[@id='loginBtn']")
login_btn.click()

product = driver.find_element(By.XPATH, "//li[@data-id = '103']").text
print("product:", product)

assert "T-Shirt" in product

driver.quit()