# DAY 48

from selenium import webdriver
from selenium.webdriver.common.by import By

# to keep chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# # there was no direct way to access link so go for the "div" class name to get hold of "a" tag
# print(documentation_link.text)
# # in such cases use XPATH
# logo_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[4]/ul/li[8]/a')
# print(logo_link)


event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# upcoming_events = {}
# for n in range(len(event_dates)):
#     # upcoming_events[event_dates[n].text] = event_names[n].text
#     upcoming_events[n]= {
#         "time": event_dates[n].text,
#         "name": event_names[n].text
#     }

# Dictionary comprehension to create a dictionary of upcoming events
upcoming_events = {
    n: {
        "time": event_dates[n].text,
        "name": event_names[n].text
    }
    for n in range(len(event_dates))
}
print(upcoming_events)

# driver.close()  # This will close the browser window
driver.quit()   # This will close the browser session
# Note: The above close and quit methods are not necessary if you want to keep the browser open.
