from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

try:
    # Open website
    driver.get("https://tichi-app-webapp-stage.web.app/")

    driver.save_screenshot("screenshots/01_HomePage.png")

    # Click Sign In
    sign_in = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Sign In')]")
        )
    )

    sign_in.click()

    # Wait for Email field
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    driver.save_screenshot("screenshots/02_LoginPage.png")

    # Enter Email
    email.clear()
    email.send_keys("717823i227@kce.ac.in")

    driver.save_screenshot("screenshots/03_EmailEntered.png")

    # Find Continue button
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    # Click using JavaScript (more reliable)
    driver.execute_script("arguments[0].click();", continue_btn)

    print("Continue button clicked")

    time.sleep(5)

    driver.save_screenshot("screenshots/04_AfterContinue.png")

    print("Current URL :", driver.current_url)

    # Wait for Password
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    driver.save_screenshot("screenshots/05_PasswordPage.png")

    # Enter Password
    password.send_keys("Monika@01")

    driver.save_screenshot("screenshots/06_PasswordEntered.png")

    # Login button
    login_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    driver.execute_script("arguments[0].click();", login_btn)

    time.sleep(5)

    driver.save_screenshot("screenshots/07_LoginSuccess.png")

    print("Login Successful")

except Exception as e:
    print("ERROR :", e)
    driver.save_screenshot("screenshots/Error.png")

input("Press Enter to close browser...")

driver.quit()