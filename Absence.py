import time
from SelinumUtils import get

requestAbsenceXPath = '//*[@id="content"]/div/div/main/div/div/div/div/div[2]/div[2]/div[1]/div[2]/button'
absenceTypesDropdownXPath = '//*[@id="absence-type-select"]'
searchAbsenceInputXPath = '//*[@id="component-1"]'
mobileOfficeXPath = '//*[@id="ui-components-portals-container"]/div[5]/div[2]/section/div/form/div[1]/div[1]/div[2]/div/div[2]/ul/li'
startDateInputXPath = '//*[@id="absencePeriod-start-date-input"]'
endDateInputXPath = '//*[@id="absencePeriod-end-date-input"]'
submitAbsenceXPath = '//*[@id="ui-components-portals-container"]/div[5]/div[2]/section/div/form/div[2]/div[2]/button[2]'


def request_absence(driver, absence_type, start_date, end_date):
    # request absence button
    time.sleep(1)
    get(driver, requestAbsenceXPath).click()
    # -------------------------------------- Absense dialog ------------------------------#
    time.sleep(1)

    # open absence type dropdown
    get(driver, absenceTypesDropdownXPath).click()

    # Write Mobile in the search input
    get(driver, searchAbsenceInputXPath).send_keys(absence_type)

    # click on the Mobile Office
    get(driver, mobileOfficeXPath).click()

    # -------------------------------------- Date range ------------------------------#
    # start date input
    start_date_input = get(driver, startDateInputXPath)
    end_date_input = get(driver, endDateInputXPath)

    start_date_input.click()
    start_date_input.send_keys(start_date)
    # end date input
    end_date_input.click()
    end_date_input.send_keys(end_date)

    # -------------------------------------- Submit ------------------------------#
    # submit button
    get(driver, submitAbsenceXPath).click()
