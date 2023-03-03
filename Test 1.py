from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.livescore.com/en/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.quit()
#livescore