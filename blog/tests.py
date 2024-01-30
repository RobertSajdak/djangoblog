import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element_by_xpath('//*[@id="id_user_name"]').send_keys("robee")
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("qwerty4321!")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="user-tools"]/a[1]').click()
    driver.find_element_by_xpath('/html/body/nav/div/a/span').click()


# element_is_clickable()


def response_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)


response_check(900, "test900.png")
response_check(1200, "test1200.png")
response_check(1800, "test1800.png")
response_check(600, "test600.png")
