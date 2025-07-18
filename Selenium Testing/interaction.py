from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

elements = driver.find_elements(By.CSS_SELECTOR, '#articlecount a')
total_articles = elements[1]
# print(total_articles.text)
# total_articles.click()

# find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the "Search" <input> element by name
search = driver.find_element(By.NAME, value="search")

# sending text to the search input
search.send_keys("Python", Keys.ENTER)

driver.quit()
