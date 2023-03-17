from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    #ожидание в 5 секунд, если что-то не успеет прогрузиться
    browser.implicitly_wait(5)
    browser.get("https://www.google.com/")
    #вводим в поисковой строке google запрос nesk и подтвержаем
    search_box = browser.find_element(By.CLASS_NAME, "gLFyf")
    search_box.send_keys("nesk")
    search_box.submit()

    # Ищем ссылку на сайт "nesk.ru" в результатах поиска
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "https://www.nesk.ru")
    link.click()
    #на сайте nesk.ru ищем ссылку на "новости"
    while True:
        try:
            # находим нужный элемент
            novosti= browser.find_element(By.XPATH, "//*[@id='page']/div/section[4]/div/header/div/a")

            # если элемент найден, то кликаем на него и выходим из цикла
            novosti.click()
            break
        except:
            # если элемент не найден, то проматываем страницу на 500 пикселей вниз
            browser.execute_script("window.scrollBy(0, 500)")

finally:

    # закрываем вебдрайвер
    browser.quit()