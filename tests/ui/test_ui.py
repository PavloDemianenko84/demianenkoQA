import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"C:/Users/Инна/demianenkoQA" + "chromedriver.exe")
    )

    #відкриваэмо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
    
    pass_elem = driver.find_element(By.ID, "password")

    pass_elem.send_keys("wrong password")
   
    btn_elem = driver.find_element(By.NAME, "commit")

    btn_elem.click()
    
    assert driver.title == "Sign in to GitHub - GitHub"

    #закриваємо браузер
    driver.close()


