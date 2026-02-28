import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_automation_practice():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(5)

    # Radio Button

    driver.find_element(By.XPATH, "//input[@value='radio2']").click()
    print("Radio button selected")
    time.sleep(3)


    # Suggestion Class (Auto Dropdown)

    suggestion = driver.find_element(By.ID, "autocomplete")
    suggestion.send_keys("Ind")

    time.sleep(2)
    options = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")

    for option in options:
        if option.text == "India":
            option.click()
            break

    print("Auto suggestion selected")
    time.sleep(3)


    #  Static Dropdown

    dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
    dropdown.select_by_visible_text("Option2")
    print("Static dropdown selected")
    time.sleep(3)


    # Checkboxes

    driver.find_element(By.ID, "checkBoxOption1").click()
    driver.find_element(By.ID, "checkBoxOption2").click()
    print("Checkboxes selected")
    time.sleep(3)


    # Switch Window

    driver.find_element(By.ID, "openwindow").click()
    parent = driver.current_window_handle
    time.sleep(2)

    for window in driver.window_handles:
        if window != parent:
            driver.switch_to.window(window)
            print("Switched to new window")
            driver.close()

    driver.switch_to.window(parent)
    time.sleep(3)


    #Alert Handling

    driver.find_element(By.ID, "name").send_keys("Aditya")
    driver.find_element(By.ID, "alertbtn").click()
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()
    time.sleep(3)


    # Web Table


    rows = driver.find_elements(By.XPATH, "//table[@name='courses']/tbody/tr")

    for row in rows:
        if "Advanced Selenium" in row.text:
            columns = row.find_elements(By.TAG_NAME, "td")

            course_name = columns[1].text
            city = columns[2].text

            print("Course Name:", course_name)
            print("City:", city)
    time.sleep(3)


    # Mouse Hover

    hover = driver.find_element(By.ID, "mousehover")
    actions = ActionChains(driver)
    actions.move_to_element(hover).perform()

    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Top").click()

    print("Mouse hover action completed")

    time.sleep(3)
    driver.quit()