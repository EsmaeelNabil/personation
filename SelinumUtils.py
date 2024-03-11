import time

from selenium.webdriver.common.by import By


def get(driver, xpath, by=By.XPATH):
    """Get the element by the xpath"""
    return driver.find_element(by=by, value=xpath)


# get today date in the format of dd/mm/yyyy
today = time.strftime("%d.%m.%Y")
