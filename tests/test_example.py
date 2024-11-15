import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
        chrome_options.add_argument("--window-size=1280x1024")  # Set a specific window size
        
        # Initialize WebDriver once for all tests
        cls.driver = webdriver.Chrome()

    def test_open_google(self):
        # Open Google and verify the title
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title, "Google homepage did not load correctly.")
        print("Test: Open Google homepage - Passed.")

    def test_google_search(self):
        # Perform a Google search and verify the input is accepted
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_query = "Selenium WebDriver"
        search_box.send_keys(search_query + Keys.RETURN)
        self.assertIn(search_query, self.driver.title, "Search results page did not include the search query.")
        print(f"Test: Google search for '{search_query}' - Passed.")

    def test_search_autocomplete(self):
        # Test the autocomplete suggestions in the search box
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        self.driver.implicitly_wait(2)
        suggestions = self.driver.find_elements(By.CSS_SELECTOR, "li span")
        self.assertGreater(len(suggestions), 0, "No autocomplete suggestions were found.")
        print(f"Test: Autocomplete suggestions for 'Selenium' - Found {len(suggestions)} suggestions.")

    def test_extract_results(self):
        # Extract and print search results
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_query = "Selenium WebDriver"
        search_box.send_keys(search_query + Keys.RETURN)
        self.driver.implicitly_wait(3)
        
        results = self.driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(results), 0, "No search results found.")
        print(f"Test: Extract search results for '{search_query}' - Passed.")
        for result in results[:5]:  # Display the first 5 results
            title = result.text
            link = result.find_element(By.XPATH, "..").get_attribute("href")
            print(f"Title: {title}, Link: {link}")

    def test_search_navigation(self):
        
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_query = "Selenium WebDriver"
        search_box.send_keys(search_query + Keys.RETURN)
        self.driver.implicitly_wait(3)
        
        next_button = self.driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        self.assertIn("start=10", self.driver.current_url, "Navigation to the second page of results failed.")
        print("Test: Search navigation to the second page - Passed.")

    def test_take_screenshot(self):
        # Take a screenshot of the search results page
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_query = "Selenium WebDriver"
        search_box.send_keys(search_query + Keys.RETURN)
        self.driver.implicitly_wait(3)
        screenshot_path = "google_search_results.png"
        self.driver.save_screenshot(screenshot_path)
        print(f"Test: Screenshot of search results saved at '{screenshot_path}' - Passed.")

    def test_links_are_clickable(self):
        # Verify that the search result links are clickable
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_query = "Selenium WebDriver"
        search_box.send_keys(search_query + Keys.RETURN)
        self.driver.implicitly_wait(3)
        
        results = self.driver.find_elements(By.CSS_SELECTOR, "h3")
        first_result = results[0]
        first_result.find_element(By.XPATH, "..").click()
        self.assertNotEqual(self.driver.current_url, "https://www.google.com", "Clicking the first result did not navigate to a new page.")
        print("Test: Links in search results are clickable - Passed.")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    unittest.main()

