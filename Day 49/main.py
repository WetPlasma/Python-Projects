from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Path to chromedriver
path = r"driverpath"

# Start Chrome service
service = Service(path)
driver = webdriver.Chrome(service=service)

# Open LinkedIn Jobs page
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=4094083431&f_AL=true&geoId=92000000&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
)

while True:
    try:
        sign_in_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button',
                )
            )
        )
        sign_in_button.click()
        time.sleep(1)  # Allow time for sign in modal to
        email_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
            )
        )
        email_input.send_keys("mymail.gmail.com")
        password_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
            )
        )
        password_input.send_keys("pass")
        sign_in_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button',
                )
            )
        )
        sign_in_button.click()
    except:
        print("Sign in button not found.")
        break

# Wait for 3 seconds
time.sleep(3)


while True:
    try:
        apply_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="ember55"]',
                )
            )
        )
        apply_button.click()

        phone_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4094083431-7183000321-phoneNumber-nationalNumber"]',
                )
            )
        )
        phone_input.send_keys("phone no")
        time.sleep(1)
        div_to_scroll = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[4]/div/div/div[2]")
            )
        )
        div_to_scroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button",
                )
            )
        )
        next_button.click()
        break
    except:
        print("Phone input not found.")
        break
while True:
    pass

# Close browser
driver.close()
