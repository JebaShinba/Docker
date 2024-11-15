import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver with headless mode enabled
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Initialize WebDriver with the correct ChromeDriver version
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("https://www.google.com")

    def test_google_title(self):
        # Verifying that the page title contains "Google"
        self.assertIn("Google", self.driver.title)

    def test_google_search(self):
        # Search for a term and verify results
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("OpenAI")
        search_box.submit()

        # Check if results page loaded with "OpenAI" term in title
        self.assertIn("OpenAI", self.driver.title)

    def tearDown(self):
        # Quit the WebDriver instance
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
