from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Seção DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_field)
        )
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_field)
        )
        self.driver.find_element(*self.to_field).send_keys(to_text)
