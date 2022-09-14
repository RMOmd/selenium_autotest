import time
import requests
from PIL import ImageFile
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import lxml
import re
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains


def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

def login_play_polbox(login, password, driver):
    subscription_field = wait_of_element(xpath='//*[@id="username"]', driver=driver)  # Находим поле логина
    subscription_field.send_keys(login)  # Вводим логин
    subscription_pass = wait_of_element(xpath='//*[@id="password"]', driver=driver)  # Находим поле пароля
    subscription_pass.send_keys(password)  # Вводим пароль
    login_button = wait_of_element(xpath='//*[@id="root"]//form//div[3]/button', driver=driver)  # Находим кнопку войти
    login_button.click()  # Нажимаем
    return

def logout_play_polbox(driver):
    to_cabinet = wait_of_element(xpath='//*[@id="root"]//header/div/div/div[2]/button',
                                 driver=driver)  # в личном кабинете
    to_cabinet.click()

    account_check = wait_of_element(xpath='//*[@id="root"]//div[2]/div/div/div[1]//div/div[2]', driver=driver)
    print("\nAccount type is - " + account_check.text)  # Проверка типа аккаунта

    logout_button = wait_of_element(xpath='//*[@id="root"]//div[1]/button[3]/div',
                                    driver=driver)  # Находим кнопку выйти
    logout_button.click()  # Нажимаем
    print("Exit from account OK")
    yes_button2 = wait_of_element(xpath='/html/body/div[2]/div[3]/div/div[2]/button[2]',
                                  driver=driver)  # Находим кнопку да
    yes_button2.click()  # Нажимаем
    return


options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument(f"--user-data-dir=C:/Users/RMO/AppData/Local/Google/Chrome/User Data")
options.add_argument("javascript.enabled")
#options.headless = True
driver = webdriver.Chrome(options=options, executable_path=r'D:/Selenium/chromedriver.exe')
URL = "http://play.polbox.tv/#/genre/15?title=Animowany"
driver.get(URL)

#login_play_polbox('12437121', '472790', driver=driver)

iBrokenImageCount = 0
time.sleep(4)
image_list = driver.find_elements(By.TAG_NAME, "img") # image_list = driver.find_elements(By.TAG_NAME, "img")
print('Total number of images are ' + str(len(image_list)))
for img in image_list:
    try:
        response = requests.get(img.get_attribute('src'), stream=True)
        if (response.status_code ==200):# != 200):
            #print(img.get_attribute('outerHTML') + " is broken.")
            #iBrokenImageCount = (iBrokenImageCount + 1)
            image_address = img.get_attribute("src")
            web_address = image_address.split('/')
            last_part = web_address.pop(-1)[5:]
            print(last_part)
            second_part = web_address.pop(-1)
            print(second_part)
            begin_address = 'http://online.polbox.tv/v10/'
            full_address = begin_address + second_part + '/' + last_part
            print(full_address)

    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")

