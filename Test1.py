from pathlib import Pathgit

from selenium import webdriver
from selenium.webdriver.common.by import By


def check_header_name(expected_name: str) -> None:
    html_path = Path(__file__).resolve().parent / "index.html"

    driver = webdriver.Chrome()
    driver.sleep(10000)
    try:
        driver.get(html_path.resolve().as_uri())
        header_text = driver.find_element(By.TAG_NAME, "h1").text
        print(f"Header found: {header_text}")

        if header_text == expected_name:
            print("Name is correct")
        else:
            print(f"Name is incorrect. Expected: {expected_name}")
    finally:
        driver.quit()


if __name__ == "__main__":
    check_header_name("Shalini Devarasetti")
