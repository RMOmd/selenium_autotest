from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests


def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

### проверка картинок

iBrokenImageCount = 0
image_list = []
image_list = driver.find_element(By.XPATH, '//*[@class="archiveCarBlock"]//img').get_attribute("background")  # //div[@background]')   //*[@class="archiveCarBlock"]//img'
print(image_list)

print (image_list.get_attribute("src"))
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
