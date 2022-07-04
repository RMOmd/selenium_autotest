from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

def test_add_item_to_basket():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'E:\other\java_selenium\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = wait_of_element(xpath='//*[@id="user-name"]', driver=driver)
    input_password = wait_of_element(xpath='//*[@id="password"]', driver=driver)
    login_button = wait_of_element(xpath='//*[@id="login-button"]', driver=driver)

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск товара и проверка попадания на страницу
    result_find_item = wait_of_element(xpath='//*[@id="item_5_title_link"]/div', driver=driver)
    result_find_item.click()

    # Добавление товара в корзину и проверка
    add_to_basket_button = wait_of_element(xpath='//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]', driver=driver)
    add_to_basket_button.click()

    find_basket = wait_of_element(xpath='//*[@id=\"shopping_cart_container\"]/a', driver=driver)
    find_basket.click()

    item_in_basket = wait_of_element(xpath='//*[@id=\"item_5_title_link\"]/div', driver=driver)
    if item_in_basket.text == "Sauce Labs Fleece Jacket":
        print("Товар в корзине")
    else:
        print("Ошибка поиска товара в корзине")

    time.sleep(5)


if __name__ == '__main__':
    test_add_item_to_basket()
