from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import requests
from PIL import Image, ImageDraw, ImageChops
from io import BytesIO
import easyocr


# region Functions
def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


channel_listing = {'http://play.polbox.tv/#/live/1762': 'Fokus TV',
                   'http://play.polbox.tv/#/live/1786': 'Canal+ Kuchnia',
                   'http://play.polbox.tv/#/live/1585': 'Polsat',
                   'http://play.polbox.tv/#/live/1495': 'Polsat 2',
                   'http://play.polbox.tv/#/live/1555': 'TVP 1',
                   'http://play.polbox.tv/#/live/1558': 'TVP 2',
                   'http://play.polbox.tv/#/live/1642': 'TVP Kultura',
                   'http://play.polbox.tv/#/live/1666': 'TVP Polonia',
                   'http://play.polbox.tv/#/live/1630': 'TV 4',
                   'http://play.polbox.tv/#/live/1867': 'TTV',
                   'http://play.polbox.tv/#/live/1567': 'TVN',
                   'http://play.polbox.tv/#/live/1573': 'TV Siedem',
                   'http://play.polbox.tv/#/live/1636': 'TVS',
                   'http://play.polbox.tv/#/live/1516': 'TV Plus',
                   'http://play.polbox.tv/#/live/1732': 'TVP3 Warszawa',
                   'http://play.polbox.tv/#/live/1921': 'Nowa TV',
                   'http://play.polbox.tv/#/live/1948': 'SuperPolsat',
                   'http://play.polbox.tv/#/live/1561': 'Ale Kino+',
                   'http://play.polbox.tv/#/live/1777': 'Ale Kino! HD',
                   'http://play.polbox.tv/#/live/1597': 'AXN',
                   'http://play.polbox.tv/#/live/1498': 'AXN Black',
                   'http://play.polbox.tv/#/live/1501': 'AXN White',
                   'http://play.polbox.tv/#/live/1552': 'Canal+ Premium',
                   'http://play.polbox.tv/#/live/1678': 'CANAL+ Seriale',
                   'http://play.polbox.tv/#/live/1783': 'CANAL+ Seriale HD',
                   'http://play.polbox.tv/#/live/1675': 'CANAL+Family',
                   'http://play.polbox.tv/#/live/1591': 'Comedy Central',
                   'http://play.polbox.tv/#/live/1831': 'HBO',
                   'http://play.polbox.tv/#/live/1834': 'HBO 2',
                   'http://play.polbox.tv/#/live/1837': 'HBO 3',
                   'http://play.polbox.tv/#/live/1840': '13 ulica',
                   'http://play.polbox.tv/#/live/1543': 'Filmbox Extra',
                   'http://play.polbox.tv/#/live/1810': 'Filmbox Premium',
                   'http://play.polbox.tv/#/live/1600': 'FOX Comedy',
                   'http://play.polbox.tv/#/live/1888': 'Polsat Film',
                   'http://play.polbox.tv/#/live/1510': 'Kino Polska',
                   'http://play.polbox.tv/#/live/1702': 'Scifi',
                   'http://play.polbox.tv/#/live/1771': 'Warner TV',
                   'http://play.polbox.tv/#/live/1645': 'TVP Seriale',
                   'http://play.polbox.tv/#/live/1723': 'VOD 1',
                   'http://play.polbox.tv/#/live/1726': 'VOD 2',
                   'http://play.polbox.tv/#/live/1795': 'VOD 3',
                   'http://play.polbox.tv/#/live/1798': 'VOD 4',
                   'http://play.polbox.tv/#/live/1801': 'VOD 5',
                   'http://play.polbox.tv/#/live/1927': 'CBS Reality',
                   'http://play.polbox.tv/#/live/1906': 'Cinemax',
                   'http://play.polbox.tv/#/live/1918': 'Epic Drama',
                   'http://play.polbox.tv/#/live/1966': 'Paramount Channel',
                   'http://play.polbox.tv/#/live/1969': 'Polsat Seriale',
                   'http://play.polbox.tv/#/live/1960': 'Romance TV',
                   'http://play.polbox.tv/#/live/2125': 'TVN Fabula',
                   'http://play.polbox.tv/#/live/1603': 'Polsat News',
                   'http://play.polbox.tv/#/live/1891': 'Polsat News 2',
                   'http://play.polbox.tv/#/live/1684': 'TVP Info',
                   'http://play.polbox.tv/#/live/1570': 'TVN 24',
                   'http://play.polbox.tv/#/live/1849': 'TVN 24 BiS',
                   'http://play.polbox.tv/#/live/1741': 'TV Republika',
                   'http://play.polbox.tv/#/live/1972': 'Wydarzenia 24',
                   'http://play.polbox.tv/#/live/1897': 'Polsat Sport Premium 1',
                   'http://play.polbox.tv/#/live/1900': 'Polsat Sport Premium 2',
                   'http://play.polbox.tv/#/live/1903': 'Polsat Sport',
                   'http://play.polbox.tv/#/live/1894': 'CANAL+ Sport 2',
                   'http://play.polbox.tv/#/live/1549': 'CANAL+ SPORT',
                   'http://play.polbox.tv/#/live/1855': 'Eleven Sports 1',
                   'http://play.polbox.tv/#/live/1858': 'Eleven Sports 2',
                   'http://play.polbox.tv/#/live/1861': 'Eleven Sports 3',
                   'http://play.polbox.tv/#/live/1696': 'FightBox',
                   'http://play.polbox.tv/#/live/1705': 'Motowizja',
                   'http://play.polbox.tv/#/live/1681': 'Canal+ Sport 5',
                   'http://play.polbox.tv/#/live/1708': 'SportKlub',
                   'http://play.polbox.tv/#/live/1594': 'Eurosport 1',
                   'http://play.polbox.tv/#/live/1564': 'TVP Sport',
                   'http://play.polbox.tv/#/live/1765': 'Adventure',
                   'http://play.polbox.tv/#/live/1492': 'Discovery Channel',
                   'http://play.polbox.tv/#/live/1738': 'Da Vinci',
                   'http://play.polbox.tv/#/live/1528': 'Science Channel',
                   'http://play.polbox.tv/#/live/1654': 'Discovery Life',
                   'http://play.polbox.tv/#/live/1534': 'National Geo',
                   'http://play.polbox.tv/#/live/1852': 'ID',
                   'http://play.polbox.tv/#/live/1789': 'Canal+ Domo',
                   'http://play.polbox.tv/#/live/1780': 'History Channel HD',
                   'http://play.polbox.tv/#/live/1672': 'History Channel',
                   'http://play.polbox.tv/#/live/1750': 'H2',
                   'http://play.polbox.tv/#/live/1489': 'Nat Geo Wild',
                   'http://play.polbox.tv/#/live/1663': 'Planete+',
                   'http://play.polbox.tv/#/live/1774': 'Travel Channel',
                   'http://play.polbox.tv/#/live/1522': 'TVP Historia',
                   'http://play.polbox.tv/#/live/1936': 'Animal Planet',
                   'http://play.polbox.tv/#/live/1939': 'BBC Earth',
                   'http://play.polbox.tv/#/live/1981': 'Crime Investigation',
                   'http://play.polbox.tv/#/live/1987': 'Nat Geo People',
                   'http://play.polbox.tv/#/live/1978': 'Viasat History',
                   'http://play.polbox.tv/#/live/1993': 'Viasat Nature',
                   'http://play.polbox.tv/#/live/1735': '4Fun.TV',
                   'http://play.polbox.tv/#/live/1747': 'BBC First',
                   'http://play.polbox.tv/#/live/1699': 'Disco Polo Music',
                   'http://play.polbox.tv/#/live/1690': 'Eska',
                   'http://play.polbox.tv/#/live/1588': 'MTV Polska',
                   'http://play.polbox.tv/#/live/1693': 'Polo TV',
                   'http://play.polbox.tv/#/live/1846': 'Polsat Café',
                   'http://play.polbox.tv/#/live/1720': 'TVP Rozrywka',
                   'http://play.polbox.tv/#/live/1582': 'TVN Style',
                   'http://play.polbox.tv/#/live/1579': 'TVN TURBO',
                   'http://play.polbox.tv/#/live/1519': 'TV6',
                   'http://play.polbox.tv/#/live/1759': 'MTV00s',
                   'http://play.polbox.tv/#/live/1915': '4Fun Dance',
                   'http://play.polbox.tv/#/live/1990': 'CBS Europa',
                   'http://play.polbox.tv/#/live/1957': 'DTX',
                   'http://play.polbox.tv/#/live/1930': 'Eska Rock TV',
                   'http://play.polbox.tv/#/live/1963': 'Food Network',
                   'http://play.polbox.tv/#/live/1954': 'HGTV',
                   'http://play.polbox.tv/#/live/1933': 'Kino Polska Muzyka',
                   'http://play.polbox.tv/#/live/1909': 'Stars TV',
                   'http://play.polbox.tv/#/live/1942': 'TLC',
                   'http://play.polbox.tv/#/live/1975': 'Viasat Explore',
                   'http://play.polbox.tv/#/live/1924': 'Vox Music TV',
                   'http://play.polbox.tv/#/live/1504': 'CBeebies',
                   'http://play.polbox.tv/#/live/1870': 'Boomerang',
                   'http://play.polbox.tv/#/live/1873': 'Polsat JimJam',
                   'http://play.polbox.tv/#/live/1687': 'Disney XD',
                   'http://play.polbox.tv/#/live/1531': 'Disney Channel',
                   'http://play.polbox.tv/#/live/1768': 'Disney Junior',
                   'http://play.polbox.tv/#/live/1525': 'MiniMini',
                   'http://play.polbox.tv/#/live/1513': 'Nick Jr.',
                   'http://play.polbox.tv/#/live/1756': 'Nickelodeon',
                   'http://play.polbox.tv/#/live/1729': 'Puls 2',
                   'http://play.polbox.tv/#/live/1792': 'teleTOON+',
                   'http://play.polbox.tv/#/live/1744': 'TVP-ABC',
                   'http://play.polbox.tv/#/live/1912': '4fun Kids',
                   'http://play.polbox.tv/#/live/1984': 'Cartoon Network'}

urlList = [
    'http://play.polbox.tv/#/live/1762',
    'http://play.polbox.tv/#/live/1786',
    'http://play.polbox.tv/#/live/1585',
    'http://play.polbox.tv/#/live/1495',
    'http://play.polbox.tv/#/live/1555',
    'http://play.polbox.tv/#/live/1558',
    'http://play.polbox.tv/#/live/1642',
    'http://play.polbox.tv/#/live/1666',
    'http://play.polbox.tv/#/live/1630',
    'http://play.polbox.tv/#/live/1867',
    'http://play.polbox.tv/#/live/1567',
    'http://play.polbox.tv/#/live/1573',
    'http://play.polbox.tv/#/live/1636',
    'http://play.polbox.tv/#/live/1516',
    'http://play.polbox.tv/#/live/1732',
    'http://play.polbox.tv/#/live/1921',
    'http://play.polbox.tv/#/live/1948',
    'http://play.polbox.tv/#/live/1561',
    'http://play.polbox.tv/#/live/1777',
    'http://play.polbox.tv/#/live/1597',
    'http://play.polbox.tv/#/live/1498',
    'http://play.polbox.tv/#/live/1501',
    'http://play.polbox.tv/#/live/1552',
    'http://play.polbox.tv/#/live/1678',
    'http://play.polbox.tv/#/live/1783',
    'http://play.polbox.tv/#/live/1675',
    'http://play.polbox.tv/#/live/1591',
    'http://play.polbox.tv/#/live/1831',
    'http://play.polbox.tv/#/live/1834',
    'http://play.polbox.tv/#/live/1837',
    'http://play.polbox.tv/#/live/1840',
    'http://play.polbox.tv/#/live/1810',
    'http://play.polbox.tv/#/live/1600',
    'http://play.polbox.tv/#/live/1888',
    'http://play.polbox.tv/#/live/1510',
    'http://play.polbox.tv/#/live/1702',
    'http://play.polbox.tv/#/live/1771',
    'http://play.polbox.tv/#/live/1645',
    'http://play.polbox.tv/#/live/1723',
    'http://play.polbox.tv/#/live/1726',
    'http://play.polbox.tv/#/live/1795',
    'http://play.polbox.tv/#/live/1798',
    'http://play.polbox.tv/#/live/1801',
    'http://play.polbox.tv/#/live/1927',
    'http://play.polbox.tv/#/live/1906',
    'http://play.polbox.tv/#/live/1918',
    'http://play.polbox.tv/#/live/1966',
    'http://play.polbox.tv/#/live/1969',
    'http://play.polbox.tv/#/live/1960',
    'http://play.polbox.tv/#/live/2125',
    'http://play.polbox.tv/#/live/1603',
    'http://play.polbox.tv/#/live/1891',
    'http://play.polbox.tv/#/live/1684',
    'http://play.polbox.tv/#/live/1570',
    'http://play.polbox.tv/#/live/1849',
    'http://play.polbox.tv/#/live/1741',
    'http://play.polbox.tv/#/live/1972',
    'http://play.polbox.tv/#/live/1897',
    'http://play.polbox.tv/#/live/1900',
    'http://play.polbox.tv/#/live/1903',
    'http://play.polbox.tv/#/live/1894',
    'http://play.polbox.tv/#/live/1549',
    'http://play.polbox.tv/#/live/1855',
    'http://play.polbox.tv/#/live/1858',
    'http://play.polbox.tv/#/live/1861',
    'http://play.polbox.tv/#/live/1696',
    'http://play.polbox.tv/#/live/1705',
    'http://play.polbox.tv/#/live/1681',
    'http://play.polbox.tv/#/live/1708',
    'http://play.polbox.tv/#/live/1594',
    'http://play.polbox.tv/#/live/1564',
    'http://play.polbox.tv/#/live/1765',
    'http://play.polbox.tv/#/live/1492',
    'http://play.polbox.tv/#/live/1738',
    'http://play.polbox.tv/#/live/1528',
    'http://play.polbox.tv/#/live/1654',
    'http://play.polbox.tv/#/live/1534',
    'http://play.polbox.tv/#/live/1852',
    'http://play.polbox.tv/#/live/1789',
    'http://play.polbox.tv/#/live/1780',
    'http://play.polbox.tv/#/live/1672',
    'http://play.polbox.tv/#/live/1750',
    'http://play.polbox.tv/#/live/1489',
    'http://play.polbox.tv/#/live/1663',
    'http://play.polbox.tv/#/live/1774',
    'http://play.polbox.tv/#/live/1522',
    'http://play.polbox.tv/#/live/1936',
    'http://play.polbox.tv/#/live/1939',
    'http://play.polbox.tv/#/live/1981',
    'http://play.polbox.tv/#/live/1987',
    'http://play.polbox.tv/#/live/1978',
    'http://play.polbox.tv/#/live/1993',
    'http://play.polbox.tv/#/live/1735',
    'http://play.polbox.tv/#/live/1747',
    'http://play.polbox.tv/#/live/1699',
    'http://play.polbox.tv/#/live/1690',
    'http://play.polbox.tv/#/live/1588',
    'http://play.polbox.tv/#/live/1693',
    'http://play.polbox.tv/#/live/1846',
    'http://play.polbox.tv/#/live/1720',
    'http://play.polbox.tv/#/live/1582',
    'http://play.polbox.tv/#/live/1582',
    'http://play.polbox.tv/#/live/1579',
    'http://play.polbox.tv/#/live/1519',
    'http://play.polbox.tv/#/live/1759',
    'http://play.polbox.tv/#/live/1915',
    'http://play.polbox.tv/#/live/1990',
    'http://play.polbox.tv/#/live/1957',
    'http://play.polbox.tv/#/live/1930',
    'http://play.polbox.tv/#/live/1963',
    'http://play.polbox.tv/#/live/1954',
    'http://play.polbox.tv/#/live/1933',
    'http://play.polbox.tv/#/live/1909',
    'http://play.polbox.tv/#/live/1942',
    'http://play.polbox.tv/#/live/1975',
    'http://play.polbox.tv/#/live/1924',
    'http://play.polbox.tv/#/live/1504',
    'http://play.polbox.tv/#/live/1870',
    'http://play.polbox.tv/#/live/1873',
    'http://play.polbox.tv/#/live/1687',
    'http://play.polbox.tv/#/live/1531',
    'http://play.polbox.tv/#/live/1768',
    'http://play.polbox.tv/#/live/1525',
    'http://play.polbox.tv/#/live/1513',
    'http://play.polbox.tv/#/live/1756',
    'http://play.polbox.tv/#/live/1729',
    'http://play.polbox.tv/#/live/1792',
    'http://play.polbox.tv/#/live/1744',
    'http://play.polbox.tv/#/live/1912',
    'http://play.polbox.tv/#/live/1984'
]


def name_compare(i):
    channel_name = str(i)
    return print(channel_listing.get(channel_name))


def check_url(urlList, driver):
    for i in urlList:
        print('\n' + i)
        name_compare(i)
        driver.get(i)
        driver.implicitly_wait(2)

        iBrokenImageCount = 0
        image_list = driver.find_elements(By.XPATH, '//*[@class="archiveCarBlock"]/div')
        res_total = print('\nTotal number of images are ' + str(len(image_list)))

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('background'), stream=True)
                if (response.status_code != 200):
                    res_broken = print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount = (iBrokenImageCount + 1)

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
                iBrokenImageCount = (iBrokenImageCount + 1)
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")
        print('The page has ' + str(iBrokenImageCount) + ' broken images')
        driver.refresh()
    # driver.quit()
    return res_total


def login_play_polbox(login, password, driver):
    subscription_field = wait_of_element(xpath='//*[@id="username"]', driver=driver)  # Находим поле логина
    subscription_field.send_keys(login)  # Вводим логин
    subscription_pass = wait_of_element(xpath='//*[@id="password"]', driver=driver)  # Находим поле пароля
    subscription_pass.send_keys(password)  # Вводим пароль
    login_button = wait_of_element(xpath="//button[text()='Log In']", driver=driver)  # Находим кнопку войти
    login_button.click()  # Нажимаем
    return


def logout_play_polbox(driver):
    to_cabinet = wait_of_element(xpath='//*[@id="root"]//header/div/div/div[2]/button',
                                 driver=driver)  # в личном кабинете
    to_cabinet.click()

    account_check = wait_of_element(xpath='//*[@id="root"]//div[2]/div/div/div[1]//div/div[2]', driver=driver)
    print("\nAccount type is - " + account_check.text)  # Проверка типа аккаунта

    logout_button = wait_of_element(xpath="//div[text()='Log Out']",
                                    driver=driver)  # Находим кнопку выйти
    logout_button.click()  # Нажимаем
    print("Exit from account OK")
    yes_button2 = wait_of_element(xpath='/html/body/div[2]/div[3]/div/div[2]/button[2]',
                                  driver=driver)  # Находим кнопку да
    yes_button2.click()  # Нажимаем
    return


def text_recognition(file_path):
    reader = easyocr.Reader(["ru"], ["en"])
    result = reader.readtext(file_path, detail=0)
    return result


def remove_movie(driver):
    wait = WebDriverWait(driver, 10)
    remove_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]//div/div/div/div/div[3]/button')))  # Жмем удалить кино
    ActionChains(driver).move_to_element(remove_button).click().perform()
    yes_button = wait_of_element(xpath='/html/body//div[3]//div[2]/button[1]', driver=driver)  # Жмем да
    yes_button.click()
    return


def remove_tv(driver):
    wait = WebDriverWait(driver, 10)
    remove_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]//div[6]/button')))  # Жмем удалить канал
    ActionChains(driver).move_to_element(remove_button).click().perform()
    yes_button = wait_of_element(xpath='/html/body//div[3]//div[2]/button[1]', driver=driver)  # Жмем да
    yes_button.click()
    return

url_categories = [
    '(//*[@id="root"]//div[1]/button)[8]',
    '(//*[@id="root"]//div[1]/button)[9]',
    '(//*[@id="root"]//div[1]/button)[10]',
    '(//*[@id="root"]//div[1]/button)[11]',
    '(//*[@id="root"]//div[1]/button)[12]',
    '(//*[@id="root"]//div[1]/button)[13]',
    '(//*[@id="root"]//div[1]/button)[14]',
    '(//*[@id="root"]//div[1]/button)[15]',
    '(//*[@id="root"]//div[1]/button)[16]',
    '(//*[@id="root"]//div[1]/button)[17]',
    '(//*[@id="root"]//div[1]/button)[18]',
    '(//*[@id="root"]//div[1]/button)[19]',
    '(//*[@id="root"]//div[1]/button)[20]',
    '(//*[@id="root"]//div[1]/button)[21]',
    '(//*[@id="root"]//div[1]/button)[22]',
    '(//*[@id="root"]//div[1]/button)[23]',
    '(//*[@id="root"]//div[1]/button)[24]',
    '(//*[@id="root"]//div[1]/button)[25]',
    '(//*[@id="root"]//div[1]/button)[26]'
]

channel_listing = {'http://play.polbox.tv/#/live/1762': 'Fokus TV',
                   'http://play.polbox.tv/#/live/1786': 'Canal+ Kuchnia',
                   'http://play.polbox.tv/#/live/1585': 'Polsat',
                   'http://play.polbox.tv/#/live/1495': 'Polsat 2',
                   'http://play.polbox.tv/#/live/1555': 'TVP 1',
                   'http://play.polbox.tv/#/live/1558': 'TVP 2',
                   'http://play.polbox.tv/#/live/1642': 'TVP Kultura',
                   'http://play.polbox.tv/#/live/1666': 'TVP Polonia',
                   'http://play.polbox.tv/#/live/1630': 'TV 4',
                   'http://play.polbox.tv/#/live/1867': 'TTV',
                   'http://play.polbox.tv/#/live/1567': 'TVN',
                   'http://play.polbox.tv/#/live/1573': 'TV Siedem',
                   'http://play.polbox.tv/#/live/1636': 'TVS',
                   'http://play.polbox.tv/#/live/1516': 'TV Plus',
                   'http://play.polbox.tv/#/live/1732': 'TVP3 Warszawa',
                   'http://play.polbox.tv/#/live/1921': 'Nowa TV',
                   'http://play.polbox.tv/#/live/1948': 'SuperPolsat',
                   'http://play.polbox.tv/#/live/1561': 'Ale Kino+',
                   'http://play.polbox.tv/#/live/1777': 'Ale Kino! HD',
                   'http://play.polbox.tv/#/live/1597': 'AXN',
                   'http://play.polbox.tv/#/live/1498': 'AXN Black',
                   'http://play.polbox.tv/#/live/1501': 'AXN White',
                   'http://play.polbox.tv/#/live/1552': 'Canal+ Premium',
                   'http://play.polbox.tv/#/live/1678': 'CANAL+ Seriale',
                   'http://play.polbox.tv/#/live/1783': 'CANAL+ Seriale HD',
                   'http://play.polbox.tv/#/live/1675': 'CANAL+Family',
                   'http://play.polbox.tv/#/live/1591': 'Comedy Central',
                   'http://play.polbox.tv/#/live/1831': 'HBO',
                   'http://play.polbox.tv/#/live/1834': 'HBO 2',
                   'http://play.polbox.tv/#/live/1837': 'HBO 3',
                   'http://play.polbox.tv/#/live/1840': '13 ulica',
                   'http://play.polbox.tv/#/live/1543': 'Filmbox Extra',
                   'http://play.polbox.tv/#/live/1810': 'Filmbox Premium',
                   'http://play.polbox.tv/#/live/1600': 'FOX Comedy',
                   'http://play.polbox.tv/#/live/1888': 'Polsat Film',
                   'http://play.polbox.tv/#/live/1510': 'Kino Polska',
                   'http://play.polbox.tv/#/live/1702': 'Scifi',
                   'http://play.polbox.tv/#/live/1771': 'Warner TV',
                   'http://play.polbox.tv/#/live/1645': 'TVP Seriale',
                   'http://play.polbox.tv/#/live/1723': 'VOD 1',
                   'http://play.polbox.tv/#/live/1726': 'VOD 2',
                   'http://play.polbox.tv/#/live/1795': 'VOD 3',
                   'http://play.polbox.tv/#/live/1798': 'VOD 4',
                   'http://play.polbox.tv/#/live/1801': 'VOD 5',
                   'http://play.polbox.tv/#/live/1927': 'CBS Reality',
                   'http://play.polbox.tv/#/live/1906': 'Cinemax',
                   'http://play.polbox.tv/#/live/1918': 'Epic Drama',
                   'http://play.polbox.tv/#/live/1966': 'Paramount Channel',
                   'http://play.polbox.tv/#/live/1969': 'Polsat Seriale',
                   'http://play.polbox.tv/#/live/1960': 'Romance TV',
                   'http://play.polbox.tv/#/live/2125': 'TVN Fabula',
                   'http://play.polbox.tv/#/live/1603': 'Polsat News',
                   'http://play.polbox.tv/#/live/1891': 'Polsat News 2',
                   'http://play.polbox.tv/#/live/1684': 'TVP Info',
                   'http://play.polbox.tv/#/live/1570': 'TVN 24',
                   'http://play.polbox.tv/#/live/1849': 'TVN 24 BiS',
                   'http://play.polbox.tv/#/live/1741': 'TV Republika',
                   'http://play.polbox.tv/#/live/1972': 'Wydarzenia 24',
                   'http://play.polbox.tv/#/live/1897': 'Polsat Sport Premium 1',
                   'http://play.polbox.tv/#/live/1900': 'Polsat Sport Premium 2',
                   'http://play.polbox.tv/#/live/1903': 'Polsat Sport',
                   'http://play.polbox.tv/#/live/1894': 'CANAL+ Sport 2',
                   'http://play.polbox.tv/#/live/1549': 'CANAL+ SPORT',
                   'http://play.polbox.tv/#/live/1855': 'Eleven Sports 1',
                   'http://play.polbox.tv/#/live/1858': 'Eleven Sports 2',
                   'http://play.polbox.tv/#/live/1861': 'Eleven Sports 3',
                   'http://play.polbox.tv/#/live/1696': 'FightBox',
                   'http://play.polbox.tv/#/live/1705': 'Motowizja',
                   'http://play.polbox.tv/#/live/1681': 'Canal+ Sport 5',
                   'http://play.polbox.tv/#/live/1708': 'SportKlub',
                   'http://play.polbox.tv/#/live/1594': 'Eurosport 1',
                   'http://play.polbox.tv/#/live/1564': 'TVP Sport',
                   'http://play.polbox.tv/#/live/1765': 'Adventure',
                   'http://play.polbox.tv/#/live/1492': 'Discovery Channel',
                   'http://play.polbox.tv/#/live/1738': 'Da Vinci',
                   'http://play.polbox.tv/#/live/1528': 'Science Channel',
                   'http://play.polbox.tv/#/live/1654': 'Discovery Life',
                   'http://play.polbox.tv/#/live/1534': 'National Geo',
                   'http://play.polbox.tv/#/live/1852': 'ID',
                   'http://play.polbox.tv/#/live/1789': 'Canal+ Domo',
                   'http://play.polbox.tv/#/live/1780': 'History Channel HD',
                   'http://play.polbox.tv/#/live/1672': 'History Channel',
                   'http://play.polbox.tv/#/live/1750': 'H2',
                   'http://play.polbox.tv/#/live/1489': 'Nat Geo Wild',
                   'http://play.polbox.tv/#/live/1663': 'Planete+',
                   'http://play.polbox.tv/#/live/1774': 'Travel Channel',
                   'http://play.polbox.tv/#/live/1522': 'TVP Historia',
                   'http://play.polbox.tv/#/live/1936': 'Animal Planet',
                   'http://play.polbox.tv/#/live/1939': 'BBC Earth',
                   'http://play.polbox.tv/#/live/1981': 'Crime Investigation',
                   'http://play.polbox.tv/#/live/1987': 'Nat Geo People',
                   'http://play.polbox.tv/#/live/1978': 'Viasat History',
                   'http://play.polbox.tv/#/live/1993': 'Viasat Nature',
                   'http://play.polbox.tv/#/live/1735': '4Fun.TV',
                   'http://play.polbox.tv/#/live/1747': 'BBC First',
                   'http://play.polbox.tv/#/live/1699': 'Disco Polo Music',
                   'http://play.polbox.tv/#/live/1690': 'Eska',
                   'http://play.polbox.tv/#/live/1588': 'MTV Polska',
                   'http://play.polbox.tv/#/live/1693': 'Polo TV',
                   'http://play.polbox.tv/#/live/1846': 'Polsat Café',
                   'http://play.polbox.tv/#/live/1720': 'TVP Rozrywka',
                   'http://play.polbox.tv/#/live/1582': 'TVN Style',
                   'http://play.polbox.tv/#/live/1579': 'TVN TURBO',
                   'http://play.polbox.tv/#/live/1519': 'TV6',
                   'http://play.polbox.tv/#/live/1759': 'MTV00s',
                   'http://play.polbox.tv/#/live/1915': '4Fun Dance',
                   'http://play.polbox.tv/#/live/1990': 'CBS Europa',
                   'http://play.polbox.tv/#/live/1957': 'DTX',
                   'http://play.polbox.tv/#/live/1930': 'Eska Rock TV',
                   'http://play.polbox.tv/#/live/1963': 'Food Network',
                   'http://play.polbox.tv/#/live/1954': 'HGTV',
                   'http://play.polbox.tv/#/live/1933': 'Kino Polska Muzyka',
                   'http://play.polbox.tv/#/live/1909': 'Stars TV',
                   'http://play.polbox.tv/#/live/1942': 'TLC',
                   'http://play.polbox.tv/#/live/1975': 'Viasat Explore',
                   'http://play.polbox.tv/#/live/1924': 'Vox Music TV',
                   'http://play.polbox.tv/#/live/1504': 'CBeebies',
                   'http://play.polbox.tv/#/live/1870': 'Boomerang',
                   'http://play.polbox.tv/#/live/1873': 'Polsat JimJam',
                   'http://play.polbox.tv/#/live/1687': 'Disney XD',
                   'http://play.polbox.tv/#/live/1531': 'Disney Channel',
                   'http://play.polbox.tv/#/live/1768': 'Disney Junior',
                   'http://play.polbox.tv/#/live/1525': 'MiniMini',
                   'http://play.polbox.tv/#/live/1513': 'Nick Jr.',
                   'http://play.polbox.tv/#/live/1756': 'Nickelodeon',
                   'http://play.polbox.tv/#/live/1729': 'Puls 2',
                   'http://play.polbox.tv/#/live/1792': 'teleTOON+',
                   'http://play.polbox.tv/#/live/1744': 'TVP-ABC',
                   'http://play.polbox.tv/#/live/1912': '4fun Kids',
                   'http://play.polbox.tv/#/live/1984': 'Cartoon Network'}

# endregion
