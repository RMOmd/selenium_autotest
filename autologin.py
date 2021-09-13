from selenium import webdriver
import time

try: 
    link = "https://www.phptravels.net/"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3) 
    button = browser.find_element_by_xpath("/html/body/header/div[1]/div/div/div[2]/div/div/a[2]").click() #жмем кнопку логин

    login_box = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input').send_keys("user@phptravels.com")#вводим логин
    pass_box = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input').send_keys("demouser")# вводим пароль
    button_login = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/button").click()#логинимся

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.quit()
