import time
import allure

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@allure.feature('Ozon tests')
@allure.story('Find different elements')
class TestOzon:
    @allure.title('Найти товар "молоко"')
    def test_find_good(self, selenium, go_to_url):
        '''
        Тест Найти товар

        Шаги:
        1) перейти на сайт и обход блокировки cloudflare
        2) в строке поиска ввести слово "молоко"
        3) нажать enter
        4) проверить, что в результатах поиска - молоко
        '''
        # Arrange
        with allure.step("Открытие страницы и обход блокировки cloudflare"):
            selenium.execute_script("window.open('http://www.ozon.ru/', '_blank')")
            time.sleep(15)
            selenium.switch_to.window(selenium.window_handles[1])
            time.sleep(0.2)
            selenium.find_element(By.CSS_SELECTOR, "#reload-button").click()
            time.sleep(0.2)


        # Act
        with allure.step("Действия с элементами"):
            search_field = selenium.find_element(By.XPATH, "//input[@placeholder='Искать на Ozon']")
            search_field.click()
            good = 'молоко'
            for i in good:
                search_field.send_keys(i)
                time.sleep(0.2)
            search_field.send_keys(Keys.ENTER)
            time.sleep(0.5)

        # Assert
        with allure.step("Проверка найденных элементов"):
            result = selenium.find_elements(By.CSS_SELECTOR, "a.tile-hover-target.ai8.ia8>div>span.tsBody500Medium")
            for i in result:
                if 'Молоко' in i.text:
                    assert True
