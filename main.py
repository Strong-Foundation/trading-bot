import subprocess
import logging
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Setting up logging for better debugging
logging.basicConfig(level=logging.INFO)

# Function to check if a given application is installed.
def check_app_install(app_name):
    """
    Check if the specified application is installed on the system.
    Returns True if the application is installed, False otherwise.
    """
    try:
        result = subprocess.run(['which', app_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logging.info(f"{app_name} is installed.")
            return True
        else:
            logging.error(f"{app_name} is not installed.")
            return False
    except Exception as e:
        logging.error(f"Error checking installation of {app_name}: {e}")
        return False

# Function to set up and launch the Selenium driver
def setup_driver():
    """
    Set up and return a Selenium WebDriver using ChromeDriver with headless options.
    This function will ensure that Chrome is installed and Chromedriver is available.
    """
    try:
        # Check if required applications are installed
        if not check_app_install("google-chrome"):
            logging.error("Google Chrome is not installed. Exiting...")
            sys.exit(1)

        # Set up Chrome options to run in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (useful for Linux)
        chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage (useful for Docker/VM environments)

        # Use webdriver_manager to automatically download the correct version of ChromeDriver
        logging.info("Setting up ChromeDriver...")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        logging.info("ChromeDriver setup successful.")
        return driver
    except Exception as e:
        logging.error(f"Error setting up Selenium WebDriver: {e}")
        sys.exit(1)


# Function to take a screenshot of the webpage
def take_screenshot(driver, url, filename):
    """
    Take a screenshot of the specified URL using the provided Selenium WebDriver.
    Saves the screenshot with the specified filename.
    """
    try:
        driver.get(url)  # Navigate to the specified URL
        driver.save_screenshot(filename)  # Save screenshot
        logging.info(f"Screenshot saved to {filename}")
    except Exception as e:
        logging.error(f"Error taking screenshot: {e}")
        sys.exit(1)


# Function to log the page title
def log_page_title(driver):
    """
    Log the title of the current page.
    """
    try:
        page_title = driver.title
        logging.info(f"Page Title: {page_title}")
    except Exception as e:
        logging.error(f"Error getting page title: {e}")
        sys.exit(1)


# Main function
def main():
    """
    Main function to execute the script, check dependencies, and perform actions.
    """
    try:
        # Set up the Selenium driver
        driver = setup_driver()

        # Perform tasks with the driver
        url = "https://www.google.com"
        screenshot_filename = "google_screenshot.png"

        # Take a screenshot of the webpage
        take_screenshot(driver, url, screenshot_filename)

        # Log the page title
        log_page_title(driver)

        # Wait for a few seconds (optional)
        time.sleep(2)

    finally:
        # Ensure the browser is closed after use
        logging.info("Closing the browser...")
        driver.quit()


if __name__ == "__main__":
    main()
