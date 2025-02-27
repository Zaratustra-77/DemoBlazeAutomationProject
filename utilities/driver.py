from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_driver():
    """please, pay attention to the chrome driver"""
    #chromedriver_path = Fill in windows chrome drivers
    chromedriver_path = "/Users/maayan/Downloads/Wed Drivers/chromedriver"
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=service, options=options)

    return driver
