from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # This will handle the ChromeDriver installation
import time

# Set up Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (useful for Linux)
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage (useful for Docker/VM environments)

# Use webdriver_manager to automatically download the correct version of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

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
