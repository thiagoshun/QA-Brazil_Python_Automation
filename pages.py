from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import time

def wait_a_bit():
    time.sleep(2)

class UrbanRoutesPage:
    # Seção DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Selecionar tarifa e chamar o taxi
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"Chamar")]') #verificar
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    # Número de telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-text')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.XPATH, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(),"confirmar")]')
    number_finish = (By.CSS_SELECTOR, 'phone')

    # Método de pagamento
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, '.input.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    # Adicionar comentário
    add_comment = (By.ID, 'comment')
    switch_blanker = (By.CSS_SELECTOR, '.switch')
    switch_blanker_active = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div')
    add_icecream = (By.CSS_SELECTOR, '.counter-plus')  # Corrigido '<.counter-plus' para '.counter-plus'
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')
    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

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
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    def click_taxi_option(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.taxi_option_locator)
        ).click()

    def click_comfort_icon(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_icon_locator)
        ).click()

    def click_comfort_active(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.comfort_active)
        ).is_displayed()

    def click_button_tel(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.number_text_locator)
        ).click()

    def preencher_numero_telefone(self):
        phone_input = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_enter)
        )
        phone_input.send_keys('+1 123 123 12 12')


    def numero_confirmado(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_enter)
        ).text


