from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'E:\other\java_selenium\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element(by=By.XPATH, value="//*[@id=\"user-name\"]")
    input_password = driver.find_element(by=By.XPATH, value="//*[@id=\"password\"]")
    login_button = driver.find_element(by=By.XPATH, value="//*[@id=\"login-button\"]")

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element(by=By.XPATH, value="//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text == "PRODUCTS":
        print("Мы попали на главную страницу")
    else:
        print("Ошибка поиска элемента")

    # Поиск товара и проверка попадания на страницу
    result_find_item = driver.find_element(by=By.ID, value="item_5_title_link")
    result_find_item.click()
    title_item = driver.find_element(by=By.XPATH, value="//*[@id=\"inventory_item_container\"]//div[2]/div[1]")
    if title_item.text == "Sauce Labs Fleece Jacket":
        print("Мы попали на страницу товара")
    else:
        print("Ошибка поиска элемента")

    # Добавление товара в корзину и проверка
    add_to_basket_button = driver.find_element(by=By.XPATH, value="//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]")
    add_to_basket_button.click()

    find_basket = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
    find_basket.click()

    item_in_basket = driver.find_element(by=By.CLASS_NAME, value="inventory_item_name")
    if item_in_basket.text == "Sauce Labs Fleece Jacket":
        print("Товар в корзине")
    else:
        print("Ошибка поиска элемента")

    time.sleep(5)


if __name__ == '__main__':
    first_test()