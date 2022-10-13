import time
import unittest
import random
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE, TimeoutException


# from ANNA import Locator as LC
# from ANNA import my_key as KEY


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test_" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        # API testing from Selenium
        print("Google Url has", requests.get(driver.current_url).status_code, "as status Code")
        code = requests.get(driver.current_url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        if "Google" not in driver.title:
            raise Exception("Google page has wrong Title!")

        # Delay all actions from 1 to 3 sec
        delay()

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "q")))
            print("Google Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        # Checking page title for "Google" (partial presence for assertIn method) then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        # driver.find_element_by_name("q").clear()
        # driver.find_element_by_name("q").send_keys("wikipedia")
        # driver.find_element_by_name("q").send_keys(Keys.RETURN)

        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait(driver, 3)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia").click()
        self.assertIn("Wikipedia", driver.title)  # partial Page title assertion
        print("Page has", driver.title + ", as Page title")
        print("Wikipedia Url has", requests.get(driver.current_url).status_code, "as status Code")

        delay()
        if "Wikipedia" not in driver.title:
            raise Exception("Unable to load Wikipedia page!")

        # assert "No results found." not in driver.page_source, True or False
        assert "No results found." not in driver.page_source
        delay()
        # API response Status code check
        codeWiki = requests.get(driver.current_url).status_code
        if codeWiki == 200:
            print("Wikipedia Url has correct", requests.get(driver.current_url).status_code, " as status Code")
        else:
            print("Wikipedia Url has incorrect", requests.get(driver.current_url).status_code, "as status Code")

        wait = WebDriverWait(driver, 2)
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='p-logo']")))
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-wiki-logo")))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="central-featured"]')))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem2 = driver.find_element(By.ID, "searchInput")
        elem2.send_keys("Dead Sea")
        # driver.find_element(By.NAME, "go").click()
        driver.find_element(By.XPATH, "//i[contains(text(),'Search')]").click()

        delay()
        # elem2.send_keys(Keys.RETURN)
        # driver.find_element_by_partial_link_text("Dead sea").click()
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))

        # use time.sleep(1) or delay() function

        self.assertIn("Dead Sea - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if "Dead Sea" not in driver.title:
            raise Exception("Wikipedia Dead Sea page Title is wrong!")

        driver.find_element(By.XPATH, "//*[@alt='Extended-protected article']")
        driver.find_element(By.XPATH, "//*[@id='siteSub']")
        driver.find_element(By.XPATH, "//*[@class='mw-page-title-main']")
        driver.find_element(By.XPATH, "//*[@alt='Dead Sea by David Shankbone.jpg']").click()
        driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").click()
        # creating variable "delay" with 3 seconds time
        delay = 3
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((
                    By.XPATH, "//*[@src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Dead_Sea_by_"
                              "David_Shankbone.jpg/800px-Dead_Sea_by_David_Shankbone.jpg']")))
            print("Dead Sea is beautifull!")
            driver.get_screenshot_as_file('ScreenshotDeadSea_page.png')
        except TimeoutException:
            print("Can't find Element by src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Dead_Sea_by_"
                  "David_Shankbone.jpg/800px-Dead_Sea_by_David_Shankbone.jpg'")

            driver.get_screenshot_as_file('Dead_Sea_page_loading_error.png')
        driver.implicitly_wait(3)

        # assert "Dead Sea - Wikpedia" in driver.title
        # print(driver.title)
        assert "Dead Sea - Wikipedia" in driver.title
        print("Page has", driver.title + " as Page title")
        print("I'd like to go there!")
        driver.get_screenshot_as_file('dSea.png')
        # driver.save_screenshot('./UnitTests/gold1.png')

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.com")

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")
        # check API response code
        print("Google Url has ", requests.get("https://www.google.com").status_code, " as status Code")
        code = requests.get("https://www.google.com").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")

        if "Google" not in driver.title:
            raise Exception("Unable to load Google page!")

        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source
        driver.implicitly_wait(5)

        # Delay all actions from 1 to 3 sec
        delay()

        elem2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
        elem2.click()
        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        if "Wikipedia" not in driver.title:
            raise Exception("Unable to load Wikipedia page!")

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-wiki-logo")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem3 = driver.find_element(By.ID, "searchInput")
        elem3.send_keys("Dead Sea")
        time.sleep(1)
        # driver.find_element(By.ID, "searchButton").click()
        elem3.send_keys(Keys.RETURN)  # this command doesn't work in FF
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        print("Page has", driver.title + " as Page title")

        if "Dead Sea" not in driver.title:
            raise Exception("Title is different in Wikipedia Dead Sea page!")

        # API response Status code check
        code = requests.get("https://www.wikipedia.org").status_code
        if code == 200:
            print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, "status Code")
        else:
            print("Wikipedia Url has", requests.get("https://www.wikipedia.org").status_code, "as status Code")

        driver.find_element(By.XPATH, "//*[@alt='Extended-protected article']")
        driver.find_element(By.XPATH, "//*[@id='siteSub']")
        driver.find_element(By.XPATH, "//*[@class='mw-page-title-main']")
        driver.find_element(By.XPATH, "//*[@alt='Dead Sea by David Shankbone.jpg']").click()
        driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").click()

        # Delay all actions from 1 to 3 sec
        delay(1, 3)

        # This waits up to 5 seconds before throwing a
        # TimeoutException unless it finds the element to return within 5 seconds.
        try:
            WebDriverWait(driver, 5) \
                .until(EC.presence_of_element_located((By.XPATH, "//img[@class='shrinkToFit']")))
            print("First Firefox Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//img[@class='overflowingVertical']")))
            print("Second Firefox Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            # self.assertIn("Gold-crystals.jpg (JPEG Image, 4788 × 3102 pixels)", driver.title)
            print("Page has", driver.title + " as Page title")

        print("Dead Sea is healthy!")

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        print("Google Url has ", requests.get("https://www.google.com").status_code, " as status Code")
        code = requests.get("https://www.google.com").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")
        if "Google" not in driver.title:
            raise Exception("Google page has wrong Title!")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "q")))
            print("First Google Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        # driver.find_element_by_name("q").clear()
        # driver.find_element_by_name("q").send_keys("wikipedia")
        # driver.find_element_by_name("q").send_keys(Keys.RETURN)

        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)  # wait max 5 sec

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia").click()
        # self.assertIn("Wikipedia", driver.title)  # partial Page title assertion
        print("Page has", driver.title + ", as Page title")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")

        # if "Wikipedia" not in driver.title:
        #     raise Exception("Unable to load Wikipedia page!")

        # assert "No results found." not in driver.page_source, True or False
        assert "No results found." not in driver.page_source

        # API response Status code check
        codeWiki = requests.get("https://www.wikipedia.org").status_code
        if codeWiki == 200:
            print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, " as status Code")
        else:
            print("Wikipedia Url has", requests.get("https://www.wikipedia.org").status_code, "as status Code")

        wait = WebDriverWait(driver, 2)
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='p-logo']")))
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-wiki-logo")))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="central-featured"]')))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem2 = driver.find_element(By.ID, "searchInput")
        elem2.send_keys("Dead Sea")
        # driver.find_element(By.NAME, "go").click()
        driver.find_element(By.XPATH, "//i[contains(text(),'Search')]").click()
        # elem2.send_keys(Keys.RETURN)
        # driver.find_element_by_partial_link_text("Gold").click()
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))

        # time.sleep(1)
        # Delay all actions from 1 to 3 sec
        delay()
        self.assertIn("Dead Sea - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if "Dead Sea" not in driver.title:
            raise Exception("Wikipedia Dead Sea page Title is wrong!")

        driver.find_element(By.XPATH, "//*[@alt='Extended-protected article']")
        driver.find_element(By.XPATH, "//*[@id='siteSub']")
        driver.find_element(By.XPATH, "//*[@class='mw-page-title-main']")
        driver.find_element(By.XPATH, "//*[@alt='Dead Sea by David Shankbone.jpg']").click()
        driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((
                    By.XPATH, "//*[@src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Dead_Sea_by_"
                              "David_Shankbone.jpg/800px-Dead_Sea_by_David_Shankbone.jpg']")))
            print("Dead Sea is there!")
            driver.get_screenshot_as_file('ScreenshotDeadSea_page.png')
        except TimeoutException:
            print("Can't find Element by src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Dead_Sea_by_"
                  "David_Shankbone.jpg/800px-Dead_Sea_by_David_Shankbone.jpg'")

            # assert "Dead Sea - Wikpedia" in driver.title
            # print(driver.title)
            assert "Dead Sea - Wikipedia" in driver.title
            print("Page has", driver.title + " as Page title")
            print("I'd like to go there!")
            driver.get_screenshot_as_file('dSea.png')
            # driver.save_screenshot('./UnitTests/gold1.png')

    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/annasour/PycharmProjects/Python/seleniumPy'
#                                                         '/HtmlReports'))
