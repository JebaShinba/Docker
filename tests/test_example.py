import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class ExampleSeleniumTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver with headless mode enabled
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--no-sandbox")  # Required for running in some CI environments
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-gpu")  # Disable GPU usage for better compatibility
        
        # Initialize WebDriver with options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("https://example.com")

    def test_page_title(self):
        self.assertIn("Example Domain", self.driver.title)

    def test_click_element(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "a")
        element.click()
        self.assertIn("example.com", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

