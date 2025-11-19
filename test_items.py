from selenium.webdriver.common.by import By

def test_add_to_cart_button_presence(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Для визуальной проверки языка (раскомментируйте при необходимости)
    # import time
    # time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Убеждаемся, что кнопка есть на странице
    assert len(add_to_cart_button) > 0, "Add to cart button is not present on the page"
    
    # Дополнительная проверка, что кнопка видима и активна
    assert add_to_cart_button[0].is_displayed(), "Add to cart button is not visible"
    assert add_to_cart_button[0].is_enabled(), "Add to cart button is not enabled"