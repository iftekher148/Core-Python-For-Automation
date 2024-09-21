from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Close the browser
driver.quit()
