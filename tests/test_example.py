from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
chrome_options.add_argument("--window-size=1280x1024")  # Set window size
chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging port
chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

# Initialize WebDriver
driver = webdriver.Chrome()

# Test
driver.get("https://www.google.com")
print("Title: ", driver.title)
driver.quit()
