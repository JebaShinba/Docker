import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ExampleSeleniumTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver using webdriver_manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
