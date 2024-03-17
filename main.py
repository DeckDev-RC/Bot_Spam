from playwright.sync_api import sync_playwright
import time
import random


class SpacemanBot:
    def __init__(self):
        with sync_playwright() as p:
            self.navegador = p.chromium.launch(headless=False)
            self.pagina = self.navegador.new_page()
            self.pagina.goto('https://pixbet.com/prejogo/')
            self.entrando()

    def entrando(self):
        self.pagina.locator('xpath=//*[@id="fe_header"]/div[1]/div[1]/div[3]/div[2]/button[1]').click()
        time.sleep(40)
        self.pagina.locator('xpath=//*[@id="fe_login_box_popup"]/form/div[4]/input').click()
        time.sleep(3)
        self.pagina.fill('xpath=//*[@id="fe_login_box_popup"]/form/div[4]/input', "kaykyloco")
        time.sleep(5)
        self.pagina.locator('xpath=/html/body/div[2]/form/div[5]/input"]').click()
        time.sleep(3)
        self.pagina.fill('xpath=/html/body/div[2]/form/div[5]/input"]', "copa2023!")
        time.sleep(4)
        self.pagina.locator('xpath=//*[@id="fe_login_box_popup"]/form/div[6]/div/button').click()
        time.sleep(30)

    @staticmethod
    def digite_como_uma_pessoa(frase, campo_input_unico):
        print("Digitando...")
        for letra in frase:
            campo_input_unico.fill(letra)
            time.sleep(random.randint(1, 5) / 30)


bot = SpacemanBot()
bot.entrando()
