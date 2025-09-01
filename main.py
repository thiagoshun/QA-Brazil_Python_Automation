import time
from time import sleep

from pages import UrbanRoutesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM,data.ADDRESS_TO)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        assert routes_page.click_comfort_active()
        time.sleep(5)


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_button_tel()
        routes_page.preencher_numero_telefone()
        time.sleep(3)
        routes_page.confirmar_numero()
        code = helpers.retrieve_phone_code(self.driver)#function utilizada para recuperar o cod
        routes_page.preencher_code(code)#receb o cod
        routes_page.code_confirmado()
        assert routes_page.code_confirmado_active() #validar que o numero que inseri apareceu depois


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_metodo_pagamento()
        routes_page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        # Confirma que o cartão foi adicionado com sucesso
        confirmacao = routes_page.confirm_card()
        # Valida se o texto retornado contém a palavra "Cartão"
        assert "Dinheiro" in confirmacao


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_comentario(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in routes_page.coment_confirm()


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        assert routes_page.switch_cobertor_active()


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        for _ in range(2):
            routes_page.add_ice()
        assert int(routes_page.qnt_sorvete()) == 2


    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        #add numero de telefone
        routes_page.click_button_tel()
        routes_page.preencher_numero_telefone()
        routes_page.confirmar_numero()
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.preencher_code(code)
        routes_page.code_confirmado()
        time.sleep(5)
        routes_page.add_metodo_pagamento()
        routes_page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        confirmacao = routes_page.confirm_card()
        routes_page.add_comentario(data.MESSAGE_FOR_DRIVER)
        time.sleep(5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

