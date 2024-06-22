from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GuiTestWithSelenium(TestCase):
    # Important: it uses real database

    def test_home_page_firefox(self):
        selenium_webdriver = webdriver.Firefox()
        selenium_webdriver.get('http://127.0.0.1:8000/')
        assert 'Welcome to HollyMovie' in selenium_webdriver.page_source

    def test_home_page_chrome(self):
        selenium_webdriver = webdriver.Chrome()
        selenium_webdriver.get('http://127.0.0.1:8000/')
        assert 'Welcome to HollyMovie' in selenium_webdriver.page_source

    def test_sign_up_page(self):
        selenium_webdriver = webdriver.Firefox()
        selenium_webdriver.get('http://127.0.0.1:8000/')
        sign_up_button = selenium_webdriver.find_element(By.LINK_TEXT, 'Sign-up')
        sign_up_button.send_keys(Keys.RETURN)
        username_id = selenium_webdriver.find_element(By.ID, 'id_username')
        username_id.send_keys('TestUser1')

        assert 'test' in selenium_webdriver.page_source