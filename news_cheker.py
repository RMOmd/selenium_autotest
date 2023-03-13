import pytest
import allure
from allure_commons.types import AttachmentType

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as BS
import requests


def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

@allure.epic('Testing PolBox')
@allure.feature('Test broken images')
@allure.story('Тестирование на битые картинки')
@allure.severity('critical')
def test_broken_img():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--user-data-dir=C:/Users/RMO/AppData/Local/Google/Chrome/User Data")
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=r'D:/Selenium/chromedriver.exe')
    # driver = webdriver.Chrome(options=options, executable_path=r'E:/selenium/chromedriver.exe')
    URL = "https://polbox.tv/en/about/news/"
    driver.get(URL)

    we_in_news_page = wait_of_element(xpath='/html/body/div[6]/div/div/div/h1', driver=driver) # Проверка, что мы на странице новостей
    if we_in_news_page.text == "NEWS POLBOX.TV":
        print("\nPage loading Succesful")
    else:
        print("\nPage loading Failed")


        # Проверка картинок на наличие поломанных, т.е. у кого статус код не 200
    iBrokenImageCount = 0
    image_list = driver.find_elements(By.TAG_NAME, "img")
    print('Total number of images are ' + str(len(image_list)))

    for img in image_list:
        try:
            response = requests.get(img.get_attribute('src'), stream=True)
            if (response.status_code != 200):
                print(img.get_attribute('outerHTML') + " is broken.")
                iBrokenImageCount = (iBrokenImageCount + 1)

        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")
        except:
            print("Encountered Some other Exception")

    driver.quit()


    print('The page has ' + str(iBrokenImageCount) + ' broken images')
if __name__ == '__main__':
    test_broken_img()

@allure.epic('Testing PolBox')
@allure.feature('Test images names')
@allure.story('Тестирование картинок на русские символы')
@allure.severity('critical')
def test_image_names():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--user-data-dir=C:/Users/RMO/AppData/Local/Google/Chrome/User Data")
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=r'D:/Selenium/chromedriver.exe')
    URL = "https://polbox.tv/en/about/news/"
    driver.get(URL)


# Проверка, что мы на странице новостей
    we_in_news_page = wait_of_element(xpath='/html/body/div[6]/div/div/div/h1', driver=driver)
    if we_in_news_page.text == "NEWS POLBOX.TV":
        print("\nPage loading Succesful")
    else:
        print("\nPage loading Failed")

# Парсинг и проверка имен картинок на наличие русских символов
    response = requests.get(URL)
    soup = BS(response.content, 'html.parser')  # Получаем контент страницы
    for link in soup.find_all('img'):  # Выбираем по тегу картинки
        results = link.get('src')[16:-4]  # Обрезаем адрес картинки для получения имени
        #res = re.findall(r'[^а-я0-9_.+-]', results)
        res = re.findall(r'[^0-9a-zA-Z_./]', results)  # Проверяем, что все символы английские
        # Цикл проверки на наличие невошедших символов
        if len(res) > 0:
            print('Russian detected')
    print("\nImages names are OK")

    driver.quit()
if __name__ == '__test_news_checker__':
    test_image_names()

    
 *************************************   считает и проверяет картинки
    
        urlList = []


    with open('list.txt', 'r') as f:
        for i in f:
            urlList.append(i)

    # navigate to URL
    for i in urlList:
        print(i)
        driver.get(i)
        driver.implicitly_wait(2)

    #driver.get("http://play.polbox.tv/#/live/1555")

        print("\nОткрыта страница Successful")


        iBrokenImageCount = 0
        image_list = driver.find_elements(By.XPATH, '//*[@class="archiveCarBlock"]/div')
        print('Total number of images are ' + str(len(image_list)))

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('background'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount = (iBrokenImageCount + 1)

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")
        print('The page has ' + str(iBrokenImageCount) + ' broken images')

    driver.quit()

    
    ======================================================================== egghunter
    
driver = webdriver.Chrome(options=options, executable_path=r'h:/Selenium/chromedriver.exe')
driver.get("https://develop:develop2016@dev.polbox.tv/en/customers/signin/")

cockie_accept = driver.find_element(By.ID, "cookiesAgreement").click()


enter_login = driver.find_element(By.ID, 'email')
enter_login.clear()
enter_login.send_keys('polboxcustomer@gmail.com')
enter_pass = driver.find_element(By.ID, 'pass')
enter_pass.clear()
enter_pass.send_keys('polQ12345')
sign_button = driver.find_element(By.CLASS_NAME, "button").click()

i = 0
while i <= 10:
    i = i + 1
    try:
        driver.implicitly_wait(30) # seconds
        eggs = driver.find_element(By.XPATH, "//*[contains(@src, 'img/eggs')]").click()

    except:
        time.sleep(3)
        driver.refresh()
        continue


time.sleep(5)
driver.quit()

    
    
