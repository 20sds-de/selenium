from selenium import webdriver
from selenium.webdriver.common.print_page_options import PrintOptions
import base64
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
print_options = PrintOptions()
print_options.orientation = "landscape" ## landscape or portrait
pdf_data = driver.print_page(print_options)

# Save PDF to a file
with open("selenium_page.pdf", "wb") as f:
    f.write(base64.b64decode(pdf_data))
print("script scuccess")

driver.quit()