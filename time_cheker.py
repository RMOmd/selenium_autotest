def test_adding_channel_to_bookmarks():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--user-data-dir=C:/Users/ДанилаСан/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(options=options, executable_path=r'E:/selenium/chromedriver.exe')
    driver.get("http://play.polbox.tv/")
    #driver.get("http://play.polbox.tv/#/bookmarks")

    print("\nОткрыта страница Succesful")

    choose_channel = wait_of_element(xpath='//*[@id="root"]//div[2]/div[1]/div[2]/div[1]', driver=driver) # Выбираем канал
    choose_channel.click()
    time.sleep(1)
    channel_name = wait_of_element(xpath='//*[@id="root"]/div/div/div/div[1]/div/div[1]/div/div/div', driver=driver) # Находим и запоминаем имя канала
    first_name = str(channel_name.text)
    print(first_name)
    choose_channel0 = wait_of_element(xpath='//*[@id="root"]/div/div/div/div[1]/div/div[2]/div[1]/video', driver=driver) # Ставим канал на паузу
    time.sleep(2)
    choose_channel0.click()
    print("пауза")

    channel_time = wait_of_element(xpath='//*[@id="root"]/div/div/div/div[1]/div/div[2]/div[3]/div[1]', driver=driver)  # Находим и запоминаем время канала
    first_time = str(channel_time.text)
    print(first_time)
    print("time")
    # channel_to_bookmarks = wait_of_element(xpath='//*[@id="root"]//div[2]/div[2]/button', driver=driver) # Жмем добавить в закладки
    # channel_to_bookmarks.click()
    # print("добавили в закладки")
    # bookmarks_button = wait_of_element(xpath='//*[@id="root"]//header//button[4]', driver=driver)# Переход в закладки
    # bookmarks_button.click()
    # print("переход в закладки")
    # time.sleep(1)
    # bookmarks_channel = wait_of_element(xpath='//*[@id="root"]/div/div/div/div[1]/div/div[2]/button', driver=driver)# Переход в закладки каналов
    # bookmarks_channel.click()
    # print("переход в каналы в закладках")
    # time.sleep(1)
    # channel_in_bookmarks = wait_of_element(xpath='//*[@id="root"]//div[2]/div/div/div/div/div/div[1]/div', driver=driver) # Находим и проверяем имя канала в закладках
    # second_name = str(channel_in_bookmarks.text)
    # print(second_name)
    # if first_name == second_name:
    #     print("Adding to bookmarks Succesful")
    # else:
    #     print("Adding to bookmarks failed")
    #
    # wait = WebDriverWait(driver, 10)
    # channel_remove = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[2]//div[1]/div/div[3]'))) # Наводим курсор на канал в закладках
    # ActionChains(driver).move_to_element(channel_remove).perform()
    #
    # bookmarks_play_channel = wait_of_element(xpath='//*[@id="root"]//div[5]/button', driver=driver)  # Переход в закладки каналов
    # bookmarks_play_channel.click()
    #
    # bookmarks_stop_channel = wait_of_element(xpath='//*[@id="root"]//div[1]/video', driver=driver)  # Переход в закладки каналов
    # bookmarks_stop_channel.click()
    #
    # channel_time_bookmarks = wait_of_element(xpath='//*[@id="root"]/div/div/div/div[1]/div/div[2]/div[3]/div[1]/div[1]', driver=driver)  # Находим и проверяем имя канала в закладках
    # second_time = str(channel_time_bookmarks.text)
    # print(second_time)
    # if first_time == second_time:
    #     print("Time in bookmarks Succesful")
    # else:
    #     print("Time in bookmarks failed")
    #
    # bookmarks_button = wait_of_element(xpath='//*[@id="root"]//header//button[4]', driver=driver)  # Переход в закладки
    # bookmarks_button.click()
    # print("переход в закладки")
    # time.sleep(1)
    # bookmarks_channel = wait_of_element(xpath='//*[@id="root"]/div/div/div/div[1]/div/div[2]/button',
    #                                     driver=driver)  # Переход в закладки каналов
    # bookmarks_channel.click()
    # print("переход в каналы в закладках")
    #
    # wait = WebDriverWait(driver, 10)
    # channel_remove = wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, '//*[@id="root"]//div[2]//div[1]/div/div[3]')))  # Наводим курсор на канал в закладках
    # ActionChains(driver).move_to_element(channel_remove).perform()
    # remove_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[6]/button')))# Жмем удалить канал из закладок
    # ActionChains(driver).move_to_element(remove_button).click().perform()
    #
    # yes_button = wait_of_element(xpath='/html/body//div[3]/div//div/div[2]/button[1]', driver=driver)# Жмем да
    # yes_button.click()
    # print('Deleting from bookmarks Succesful')

if __name__ == '__main__':
    test_adding_channel_to_bookmarks()
