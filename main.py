# from selenium import webdriver
#
#
# def get_driver():
#     """ This function help us to selenium work easier"""
#     options = webdriver.ChromeOptions()
#     options.add_argument("disable-infobars")
#     options.add_argument("start-maximized")
#     options.add_argument("disable-dev-shm-usage")
#     options.add_argument("no-sandbox")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("disable-blink-features=AutomationControlled")
#     driver = webdriver.Chrome("C:\Development\chromedriver.exe",  options=options)
#     driver.get("https://automated.pythonanywhere.com/")
#     return driver
#
#
# def main():
#     driver = get_driver()
#     element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[1]')
#     return element.text
#
#
# print(main())

from selenium import webdriver
import time

def get_driver():
    """ This function help us to selenium work easier"""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome("C:\Development\chromedriver.exe",  options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    return float(text.split(": ")[1])


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
    return clean_text(element.text)


print(main())




