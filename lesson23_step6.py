import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_css_selector("span#input_value").text
    browser.find_element_by_css_selector("input#answer").send_keys(calc(x))
    browser.find_element_by_css_selector("button.btn-primary").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
