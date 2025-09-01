from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import time

def wait_a_bit():
    time.sleep(2)

class UrbanRoutesPage:
    # Seção DE e PARA
    # Localizador do campo de origem (ID = 'from')
    from_field = (By.ID, 'from')
    # Localizador do campo de destino (ID = 'to')
    to_field = (By.ID, 'to')

    # Selecionar tarifa e chamar o taxi
    # Localiza o botão "Chamar" pelo texto
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"Chamar")]') #verificar
    # Localiza o ícone de conforto (imagem kids)
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    # Localiza quando o conforto está ativo
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    # Número de telefone
    # Localiza texto/label do telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-text')
    # Localiza campo de digitar número (ID = 'phone')
    number_enter = (By.ID, 'phone')
    # Botão confirmar número
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    # Campo para inserir código SMS
    number_code = (By.ID, 'code')
    # Botão confirmar código
    code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    # Finalizar número (possível erro no seletor)
    number_finish = (By.CSS_SELECTOR, 'phone')

    # Botão para adicionar metodo de pagamento
    add_metodo_pagamento_locator = (By.CSS_SELECTOR, '.pp-button.filled')
    # Botão adicionar cartão
    add_card_locator = (By.CSS_SELECTOR, '.pp-plus')
    # Campo número do cartão
    number_card_locator = (By.ID, 'number')
    # Campo código do cartão (CVC)
    code_card_locator = (By.CSS_SELECTOR, '#code.card-input')
    # Botão finalizar adição do cartão
    add_finish_card_locator = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button.section-close')
    # Botão fechar janela de cartão
    close_button_card_locator = (By.CSS_SELECTOR, '.close-button section-close')
    # Texto de confirmação do cartão
    confirm_card_locator = (By.CSS_SELECTOR, '.pp-value-text')

    # Adicionar comentário
    # Campo de adicionar comentário
    add_comment = (By.ID, 'comment')
    # Interruptor de opção extra
    switch_blanker = (By.CSS_SELECTOR, '.switch')
    # Localizador do switch ativo
    switch_blanker_active = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div')
    # Botão de adicionar sorvete
    add_icecream = (By.CSS_SELECTOR, '.counter-plus')  # Corrigido '<.counter-plus' para '.counter-plus'
    # Mostra a quantidade de sorvete
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')
    # Botão para chamar o táxi
    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    # Pop-up de confirmação
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

#confirmar o taxi
    chamar_taxi_locator = (By.CSS_SELECTOR, '.smart-button')
    show_order = (By.CSS_SELECTOR, '.order')


    # Construtor da classe que recebe o driver do Selenium
    def __init__(self, driver):
        self.driver = driver

    # Preenche o campo "De" com o texto informado
    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_field)
        )
        self.driver.find_element(*self.from_field).send_keys(from_text)

    # Preenche o campo "Para" com o texto informado
    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_field)
        )
        self.driver.find_element(*self.to_field).send_keys(to_text)

    # Preenche origem e destino de uma vez
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    # Retorna o valor digitado no campo "De"
    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    # Retorna o valor digitado no campo "Para"
    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    # Clica no botão de chamar táxi
    def click_taxi_option(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.taxi_option_locator)
        ).click()

    # Clica no ícone de conforto
    def click_comfort_icon(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_icon_locator)
        ).click()

    # Verifica se o conforto está ativo (retorna True/False)
    def click_comfort_active(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.comfort_active)
        ).is_displayed()

    # Clica no botão de telefone
    def click_button_tel(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.number_text_locator)
        ).click()

    # Preenche o campo número de telefone
    def preencher_numero_telefone(self):
        phone_input = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_enter)
        )
        phone_input.send_keys('+1 123 123 12 12')

    # Clica para confirmar o número de telefone
    def confirmar_numero(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_confirm)
        ).click()

    # Preenche o código SMS recebido
    def preencher_code(self, code): #recebendo como parametro
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_code)
        )
        # Corrigido: adiciona o código no campo
        self.driver.find_element(*self.number_code).send_keys(code)

    # Confirma o código enviado
    def code_confirmado(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.code_confirm)
        ).click()

#validar o cod no assert
    def code_confirmado_active(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.comfort_active)
        ).is_displayed()


#click metodo de pagamento
    def add_metodo_pagamento(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.add_metodo_pagamento_locator)
        ).click()

#add card more number and code
    def add_card(self, card_number, card_code):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.add_card_locator)
        ).click()
        # Preenche o número do cartão
        self.driver.find_element(*self.number_card_locator).send_keys(card_number)
        # Preenche o código de segurança
        self.driver.find_element(*self.code_card_locator).send_keys(card_code)
        # Clica no botão de adicionar
        self.driver.find_element(*self.add_finish_card_locator).click()

        # Confirma se cartão foi adicionado com sucesso
    def confirm_card(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.confirm_card_locator)
        ).text

    # Preenche o campo de comentário
    def add_comentario(self, mensagem):
        # Espera o campo de comentário estar visível
        comment_input = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.add_comment)
        )
        comment_input.clear()  # Limpa caso já tenha texto
        comment_input.send_keys(mensagem)

    # Retorna o texto do comentário para validação
    def coment_confirm(self):
        # Espera o campo que mostra o comentário preenchido
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.add_comment)
        ).get_attribute("value")  # "value" porque é um input

    def switch_cobertor_active(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.switch_blanker_active)
        ).is_displayed()

    def add_ice(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.add_icecream)
        ).click()

    # Retorna a quantidade de sorvete como string, depois convertida para int no teste
    def qnt_sorvete(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.qnt_icecream)
        ).text

    def click_pedir_taxi(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.chamar_taxi_locator)
        ).click()

    def click_pedir_taxi_active(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.show_order)
        ).is_displayed()

