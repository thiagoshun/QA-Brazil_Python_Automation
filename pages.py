from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from  helpers import retrieve_phone_code
import time
def wait_a_bit():
    time.sleep(2)

class UrbanRoutesPage:
    # Seção DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

 #selecionar tarifa e chamar o taxi
taxi_option_locator = (By.XPATH,'')
comfort_icon_locator = (By.XPATH,'')
comfort_active = (By.XPATH,'')

#numero de telefone
number_text_locator = (By.CSS_SELECTOR,'')
number_enter = (By.ID,'')
number_confirm = (By.CSS_SELECTOR,'')
number_code = (By.XPATH,'')
code_confirm = (By.XPATH,'')
number_finish = (By.CSS_SELECTOR,'')

#metodo de pagamento
add_metodo_pagamento = (By. CSS_SELECTOR,'')
add_card = (By.CSS_SELECTOR,'')
number_card = (By.ID,'')
code_card = (By.CSS_SELECTOR,'')
add_finish_card = (By.XPATH,'')

#adicionar comentario
add_comment = (By.ID, 'comment')
switch_blanker = (By.CSS_SELECTOR, '')
switch_blanker_active = (By.CSS_SELECTOR, '')
add_icecream = (By. CSS_SELECTOR, '')
qnt_icecream = (By. CSS_SELECTOR, '')
call_taxi_button = (By. CSS_SELECTOR, '')
pop_up = (By.CSS_SELECTOR, '')

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

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver,3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver,3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')
