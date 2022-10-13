# Two browsers test for Google and Wikipedia with Waiting functionality, screenshots and HTML Reports
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import AllureReports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search_1(self):
        driver = self.driver
        driver.get("http://www.google.com")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.NAME, "q")))
            print("First Chrome Page is ready!")
            driver.get_screenshot_as_file('GooglePage.png')
        except TimeoutException:
            print("Loading took too much time!")
            # driver.get_screenshot_as_file('google_page_loading_error.png')
            # driver.save_screenshot('UnitTests/Screenshots/google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        assert "No results found." not in driver.page_source

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
        elem.click()
        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 2)
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem = driver.find_element(By.ID, "searchInput")
        elem.send_keys("gold")
        elem.send_keys(Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        self.assertIn("Gold - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        driver.find_element(By.XPATH, "//img[@alt='Gold nugget (Australia) 4 (16848647509).jpg']").click()
        driver.find_element(By.XPATH, "//img[@class='mw-mmv-final-image jpg']").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((
                    By.XPATH, "//*[@src='https://upload.wikimedia.org/wikipedia/commons/6/69/Gold_nugget_%28Australia"
                              "%29_4_%2816848647509%29.jpg']")))
            print("Google Browser Page is ready!")
            driver.get_screenshot_as_file('ScreenshotGold_page.png')
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('gold_page_loading_error.png')
        driver.implicitly_wait(10)

        # assert "Gold-crystals.jp  g (4788�3102)" in driver.title
        print("Page has", driver.title + " as Page title")
        print("Test for Chrome is Done! Gold forever!")
        driver.get_screenshot_as_file('gold.png')

    def test_search_2(self):
        driver = self.driver
        driver.get("http://www.google.com")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.NAME, "q")))
            print("First Chrome Page is ready!")
            driver.get_screenshot_as_file('GooglePage.png')
        except TimeoutException:
            print("Loading took too much time!")
            # driver.get_screenshot_as_file('google_page_loading_error.png')
            # driver.save_screenshot('UnitTests/Screenshots/google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        assert "No results found." not in driver.page_source

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
        elem.click()
        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 2)
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem = driver.find_element(By.ID, "searchInput")
        elem.send_keys("gold")
        elem.send_keys(Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        self.assertIn("Gold - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        driver.find_element(By.XPATH, "//img[@alt='Gold nugget (Australia) 4 (16848647509).jpgggg']").click()
        driver.find_element(By.XPATH, "//img[@class='mw-mmv-final-image jpg']").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((
                    By.XPATH, "//*[@src='https://upload.wikimedia.org/wikipedia/commons/6/69/Gold_nugget_%28Australia"
                              "%29_4_%2816848647509%29.jpg']")))
            print("Google Browser Page is ready!")
            driver.get_screenshot_as_file('ScreenshotGold_page.png')
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('gold_page_loading_error.png')
        driver.implicitly_wait(10)

        # assert "Gold-crystals.jp  g (4788�3102)" in driver.title
        print("Page has", driver.title + " as Page title")
        print("Test for Chrome is Done! Gold forever!")
        driver.get_screenshot_as_file('gold.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)