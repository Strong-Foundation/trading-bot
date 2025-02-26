from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (useful for Linux)

# Set the path to ChromeDriver
driver_path = r"C:\WebDriver\chromedriver.exe"  # Update this to your chromedriver path

# Create the WebDriver instance with Chrome options
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Go to a webpage (example: Google)
driver.get("https://www.google.com")

# Take a screenshot and save it
driver.save_screenshot("google_screenshot.png")

# Get the title of the page
print("Page Title:", driver.title)

# Wait for a few seconds (optional)
time.sleep(2)

# Close the browser
driver.quit()
