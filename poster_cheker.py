import time
import allure
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image, ImageDraw, ImageChops
import httplib2
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from play_polbox import wait_of_element, login_play_polbox, logout_play_polbox, check_url, channel_listing, name_compare, text_recognition, remove_movie, remove_tv, url_categories


def posters_url_checker(driver):
    iBrokenImageCount = 0
    posters_url = []
    time.sleep(5)
    image_list = driver.find_elements(By.TAG_NAME, "img")
    print('Total number of images are ' + str(len(image_list)))
    for img in image_list:
        try:
            response = requests.get(img.get_attribute('src'), stream=True)
            if (response.status_code == 200):  # != 200):
                image_address = img.get_attribute("src")
                web_address = image_address.split('/')
                last_part = web_address.pop(-1)[5:]
                second_part = web_address.pop(-1)
                server_name = web_address.pop(-2)
                begin_address = 'http://online.polbox.tv/'
                full_address = begin_address + server_name + '/' + second_part + '/' + last_part
                posters_url.append(full_address)
        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
    posters_url.pop(0)
    return posters_url


def categori_movie(xpath_id, driver):
    movie_button = wait_of_element(xpath='//*[@id="root"]/div/header/div/div/div[1]/button[2]', driver=driver).click()
    catalog_items_more = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath_id)))
    webdriver.ActionChains(driver).move_to_element(catalog_items_more).perform()
    animation_movie = wait_of_element(xpath=xpath_id, driver=driver).click()
    return


def scroll_page(driver):
    i = 20  # листает страницу вниз  working
    while i < 2100:
        try:
            xpath_id = '//*[@id="root"]//div[' + str(i) + ']/div/h6'
            catalog_items_more = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_id)))
            webdriver.ActionChains(driver).move_to_element(catalog_items_more).perform()
            i = i + 10
            time.sleep(1)
        except TimeoutException:
            break
    return


def poster_size(driver):
    for i in posters_url_checker(driver=driver): # проверка постеров на размер менее 500
        #small_size = i
        try:
            response = requests.get(i)
            if (response.status_code == 200):
                h = httplib2.Http('.cache')
                response, content = h.request(i)
                out = open('img.png', 'wb')
                out.write(content)
                out.close()
                im = Image.open('img.png')
                w, h = im.size
                if w < 500:
                    print(i)
            else:
                continue
        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
    return



@allure.epic('Testing Play.PolBox.TV')
@allure.feature('Test movie posters size')
@allure.story('Тестирование постеров кинофильмов на маленькое разрешение')
@allure.severity('critical')
def test_posters_size_checker():
    #region Browser settings
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--user-data-dir=C:/Users/RMO/AppData/Local/Google/Chrome/User Data")
    options.add_argument("javascript.enabled")
    #options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=r'D:/Selenium/chromedriver.exe')
    #endregion
    URL = "http://play.polbox.tv/#/"
    driver.get(URL)
    login_play_polbox('12452341', '242195', driver=driver)
    for i in url_categories:
        categori_movie(i, driver=driver)
        scroll_page(driver=driver)
        poster_size(driver=driver)
    logout_play_polbox(driver=driver)
    driver.quit()
if __name__ == '__main__':
    test_posters_size_checker()


