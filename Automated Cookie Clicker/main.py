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
cookie = driver.find_element(By.ID, "bigCookie")

item_ids = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 5*60

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            cookies_text = cookies_element.text
            cookie_count = int(cookies_text.split()[0].replace(",", ""))

            products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Clicked on {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Error retrieving cookie count or products, continuing...")

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            print(f"Final cookie count: {cookies_element.text}")
        except NoSuchElementException:
            print("Final cookie count element not found.")
        break


# driver.quit()
