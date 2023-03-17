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
    #на сайте nesk.ru ищем ссылку на "выбор города"
    city = browser.find_element(By.CSS_SELECTOR, ".city-choice-link")
    city.click()
    # переключаемся на появившееся модальное окно
    modal = browser.switch_to.window(browser.window_handles[-1])

    form = browser.find_element(By.XPATH, "//*[@id='cityModal']/div/div/div[2]/form/ul/li[18]/a")
    form.click()

finally:
    # закрываем вебдрайвер
    browser.quit()





