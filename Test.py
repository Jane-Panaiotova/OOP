from selenium import webdriver
import time
import unittest
import names


class Login(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-dev-shm-using")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-info")
        self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path=r'/Users/anapanaitova/Driver/chromedriver')
        self.driver.set_window_size(1920, 1080)

    def test_tophat_registration(self):
        driver = self.driver
        url = 'https://tophat.com.ua/'
        driver.get(url)
        time.sleep(2)
        user_email = names.get_last_name() + names.get_first_name() + '@test.com'
        user_fname = names.get_first_name() + '@test.com' + names.get_last_name()
        account_button = driver.find_element_by_class_name('button-title')
        account_button.click()
        time.sleep(1)
        registration_form = driver.find_element_by_id('show-registration-popup')
        registration_form.click()
        time.sleep(2)
        email_field = driver.find_element_by_xpath('//*[@id="registration-popup"]/div/div/div[2]/form/div[3]/input')
        email_field.send_keys(user_email)
        name_field = driver.find_element_by_xpath('//*[@id="registration-popup"]/div/div/div[2]/form/div[4]/input')
        name_field.send_keys(user_fname)
        password_field1 = driver.find_element_by_xpath('//*[@id="registration-popup"]/div/div/div[2]/form/div[5]/input')
        password_field1.send_keys('1234567')
        password_field2 = driver.find_element_by_xpath('//*[@id="registration-popup"]/div/div/div[2]/form/div[6]/input')
        password_field2.send_keys('1234567')
        submit_button = driver.find_element_by_xpath('//*[@id="registration-popup"]/div/div/div[2]/form/div[7]/button')
        submit_button.click()
        time.sleep(2)
        assert driver.find_element_by_xpath('//*[@id="message-popup"]/div/div')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()