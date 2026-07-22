from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.fifa.com")
        wait = WebDriverWait(driver, 2)

        popup_selectors = [
            (By.CSS_SELECTOR, "button.close"),
            (By.CSS_SELECTOR, "button[aria-label='Close']"),
            (By.CSS_SELECTOR, "button[data-testid='close-button']"),
            (By.XPATH, "//button[contains(@class, 'close') or contains(@aria-label, 'Close') or contains(@data-testid, 'close')]"),
        ]

        for by, value in popup_selectors:
            try:
                close_button = wait.until(EC.element_to_be_clickable((by, value)))
                if close_button.is_displayed():
                    close_button.click()
                    time.sleep(1)
                    print("Signup popup closed")
                    break
            except Exception:
                continue

        time.sleep(2)
        print("Browser launched successfully")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

