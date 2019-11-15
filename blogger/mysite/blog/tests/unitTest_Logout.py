import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "vravi"
        pwd = "Sampath@3"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        try:
            # attempt to find the plus button - if found, logged in

            time.sleep(3)

            elem = driver.find_element_by_xpath('//*[@id="user-tools"]/a[3]')
            elem.click()

            elem = driver.find_element_by_xpath('//*[@id="content"]/h1').text

            if(elem == 'Logged out'):
                assert True
            else:
                raise NoSuchElementException
        except (NoSuchElementException, AssertionError):
            self.fail("User logout test failed")
            assert False

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()