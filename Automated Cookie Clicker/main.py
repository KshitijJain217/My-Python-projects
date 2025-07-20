from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.get("http://ozh.github.io/cookieclicker/")

try:
    choose_language = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
    choose_language.click()
except NoSuchElementException:
    print("Language selection not found, continuing...")

sleep(2)
cookie = driver.find_element(by=By.ID, value="bigCookie")

# Get all store items (products 0-17)
item_ids = [f"product{i}" for i in range(18)]

# Set timers
wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

while True:
    cookie.click()

    # Every 5 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            # Extract number from text like "123 cookies"
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # Stop after 5 minutes
    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break


