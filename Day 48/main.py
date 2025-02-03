from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


path = r"D:\Shreyas\python tutorials\chromedriver-win64\chromedriver.exe"

service = Service(path)
driver = webdriver.Chrome(service=service)


driver.get("https://orteil.dashnet.org/experiments/cookie/")


time.sleep(5)


cookie = driver.find_element(By.ID, "cookie")
cookie_count = driver.find_element(By.ID, "money")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")


store = store[::-1]


def buy_item():
    for item in store:
        if "grayed" not in item.get_attribute("class"):
            item.click()
            break


# Start the game loop
start_time = time.time()

while True:
    cookie.click()  # Click the cookie continuously

    # Check if 5 seconds have passed
    if time.time() - start_time > 5:
        buy_item()  # Try buying an upgrade
        start_time = time.time()  # Reset the timer

    # Print cookie count every loop iteration (optional)
    print(cookie_count.text)
