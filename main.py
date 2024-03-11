import json
import os
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Absence import request_absence
from SelinumUtils import today


def load_config(config_file="config.json"):
    with open(config_file) as f:
        return json.load(f)


def launch_browser(browser_type="chrome") -> webdriver.Remote:
    """Launches the specified browser.

    Args:
        browser_type: "chrome" or "firefox" (default: "chrome")

    Returns:
         The WebDriver instance
    """

    command = f'{os.getcwd()}/launch_browser.sh'
    subprocess.Popen(command.split())
    time.sleep(1)

    options = Options()
    options.debugger_address = "127.0.0.1:9222"
    driver = None

    if browser_type == "chrome":
        driver = webdriver.Chrome(options=options)

    elif browser_type == "firefox":
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError("Invalid browser_type. Supported options are 'chrome' and 'firefox'")
    return driver


def main():
    """
    config.json =>   {
                        "PERSONIO_ABSENCE_URL": "https://xxxx.personio.de/time-off/employee/xxxxxxx/monthly"
                    }
    :return:
    """
    config = load_config()
    driver = launch_browser(browser_type=config["BROWSER"])

    driver.get(config["PERSONIO_ABSENCE_URL"])

    request_absence(
        driver=driver,
        absence_type="Mobile Office",
        start_date=today,
        end_date=today,
    )

    time.sleep(1)

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
