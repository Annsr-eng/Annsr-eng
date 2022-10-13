import unittest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get("https://qasvus.wordpress.com/")
# driver.maximize_window()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_house_chrome(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='site-navigation']")))
        time.sleep(1)

        print(driver.find_element(By.XPATH, "//*[@rel = 'home']").get_attribute('href'))
        print(driver.find_element(By.XPATH, '//*[@class = "wp-image-55 size-full"]').get_attribute('src'))

        assert "California Real Estate" in driver.title
        print(driver.title)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[text()= 'Send Us a Message']")
        driver.find_element(By.ID, "g2-name").send_keys("Anna")
        driver.find_element(By.NAME, "g2-email").send_keys("home@gmail.com")
        driver.find_element(By.NAME, "g2-message").send_keys("Hello new home")
        driver.implicitly_wait(4)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        # driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[contains(text(),'go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//*[@class = 'pushbutton-wide']").get_attribute('type'))

    def test_search_house_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='site-navigation']")))
        time.sleep(1)

        print(driver.find_element(By.XPATH, "//*[@rel = 'home']").get_attribute('href'))
        print(driver.find_element(By.XPATH, '//*[@class = "wp-image-55 size-full"]').get_attribute('src'))

        assert "California Real Estate" in driver.title
        print(driver.title)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[text()= 'Send Us a Message']")
        driver.find_element(By.ID, "g2-name").send_keys("Anna")
        driver.find_element(By.NAME, "g2-email").send_keys("home@gmail.com")
        driver.find_element(By.NAME, "g2-message").send_keys("Hello new home")
        driver.implicitly_wait(4)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        # driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[contains(text(),'go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//*[@class = 'pushbutton-wide']").get_attribute('type'))

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def search_home_firefox(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='site-navigation']")))
        time.sleep(1)

        print(driver.find_element(By.XPATH, "//*[@rel = 'home']").get_attribute('href'))
        print(driver.find_element(By.XPATH, '//*[@class = "wp-image-55 size-full"]').get_attribute('src'))

        assert "California Real Estate" in driver.title
        print(driver.title)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[text()= 'Send Us a Message']")
        driver.find_element(By.ID, "g2-name").send_keys("Anna")
        driver.find_element(By.NAME, "g2-email").send_keys("home@gmail.com")
        driver.find_element(By.NAME, "g2-message").send_keys("Hello new home")
        driver.implicitly_wait(4)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        # driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[contains(text(),'go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//*[@class = 'pushbutton-wide']").get_attribute('type'))

    def search_home_firefox_1150x850(self):
        driver = self.driver
        driver.set_window_size(1150, 850)
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='site-navigation']")))
        time.sleep(1)

        print(driver.find_element(By.XPATH, "//*[@rel = 'home']").get_attribute('href'))
        print(driver.find_element(By.XPATH, '//*[@class = "wp-image-55 size-full"]').get_attribute('src'))

        assert "California Real Estate" in driver.title
        print(driver.title)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[text()= 'Send Us a Message']")
        driver.find_element(By.ID, "g2-name").send_keys("Anna")
        driver.find_element(By.NAME, "g2-email").send_keys("home@gmail.com")
        driver.find_element(By.NAME, "g2-message").send_keys("Hello new home")
        driver.implicitly_wait(4)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        # driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[contains(text(),'go back')]").send_keys('\n')
        print(driver.find_element(By.XPATH, "//*[@class = 'pushbutton-wide']").get_attribute('type'))

    def tearDown(self):
        self.driver.quit()


# driver.quit()

if __name__ == "__main__":
    unittest.main()
