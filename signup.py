from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver,20)

try:

    driver.get("https://tichi-app-webapp-stage.web.app/sign-up")

    driver.save_screenshot("screenshots/01_SignUp_Page.png")

    # First Name
    wait.until(
        EC.visibility_of_element_located((By.ID,"firstName"))
    ).send_keys("John")

    driver.save_screenshot("screenshots/02_FirstName.png")

    # Last Name
    driver.find_element(By.ID,"lastName").send_keys("Doe")

    driver.save_screenshot("screenshots/03_LastName.png")

    # Mobile Number
    driver.find_element(By.ID,"phoneNumber").send_keys("9876543210")

    driver.save_screenshot("screenshots/04_Mobile.png")

    # Password
    driver.find_element(By.ID,"password").send_keys("Password@123")

    driver.save_screenshot("screenshots/05_Password.png")

    # Confirm Password
    driver.find_element(By.ID,"confirmPassword").send_keys("Password@123")

    driver.save_screenshot("screenshots/06_ConfirmPassword.png")

    # Accept Terms
    driver.find_element(By.ID,"remember").click()

    driver.save_screenshot("screenshots/07_TermsAccepted.png")

    # Click Sign Up
    signup = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,"button[type='submit']")
        )
    )

    driver.execute_script("arguments[0].click();", signup)

    time.sleep(5)

    driver.save_screenshot("screenshots/08_SignUpSuccess.png")

    print("Signup Completed Successfully")

except Exception as e:

    print("ERROR :",e)

    driver.save_screenshot("screenshots/Error.png")

input("Press Enter to Close...")

driver.quit()