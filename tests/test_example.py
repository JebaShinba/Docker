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
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Initialize WebDriver with options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("https://example.com")

    def test_page_title(self):
        # Verifying that the page title is correct
        self.assertIn("Example Domain", self.driver.title)

    def test_click_element(self):
        # Click the link and check that we land on the expected redirected page
        element = self.driver.find_element(By.CSS_SELECTOR, "a")
        element.click()
        
        # Adjusted to check for the expected redirect URL
        self.assertIn("iana.org", self.driver.current_url)  # Adjusted to match the redirected domain

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


