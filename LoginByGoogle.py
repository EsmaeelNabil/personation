import time

from SelinumUtils import get

login_by_google_button = '//*[@id="sessions-login-container"]/div/section/div/form/div[1]/a'


def login_by_google_if_session_not_exist(driver):
    get(driver, login_by_google_button).click()
    time.sleep(2)
