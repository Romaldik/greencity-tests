from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
 
BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

if __name__ == "__main__":
    oprions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=oprions)
    
    driver.maximize_window()
    driver.get(BASE_URL)
    print(driver.title)
    sleep(5)
    
    sign_up_button_selector = ".header_navigation-menu-right-list > .header_sign-up-link"
    sign_up_button = driver.find_element(By.CSS_SELECTOR, sign_up_button_selector)
    
    sign_up_button.click()
    email_input = driver.find_element(By.ID, "email")
    user_name_input = driver.find_element(By.ID, "firstName")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "repeatPassword")
    sign_up_button_xpath = "//button[@class='greenStyle']"
    sign_up_button = driver.find_element(By.XPATH, sign_up_button_xpath)
    assert sign_up_button.is_displayed(), "Sign up button is not displayed"
    wait = WebDriverWait(driver, 10)
    
    submit_button_xpath = "//button[@type='submit' and contains(@class, 'greenStyle')]"
    submit_button = driver.find_element(By.XPATH, submit_button_xpath)
    
    email_input.send_keys("Test1235@test.com")
    user_name_input.send_keys("Roman")
    password_input.send_keys("Test1234!")
    confirm_password_input.send_keys("Test1234!")
    sign_up_button.click()
    
    wait = WebDriverWait(driver, 10)
    
    try:
        error_message_xpath = "//div[@class='alert-general-error']"
        # Чекаємо лише 3-5 секунд, щоб не гаяти час
        short_wait = WebDriverWait(driver, 5)
        error_element = short_wait.until(lambda d: d.find_element(By.XPATH, error_message_xpath))
        print("Знайдено помилку")
    except:
        print("Помилки не виявлено.")
    
    # error_message_xpath = "//div[@class='alert-general-error']"
    # wait.until(lambda d: d.find_element(By.XPATH, error_message_xpath).is_displayed())
    # error_message = driver.find_element(By.XPATH, error_message_xpath)
    # assert error_message.is_displayed(), "Error message is not displayed"
    
    # close_button_xpath = "//img[@alt='close button']"
    # close_button = driver.find_element(By.XPATH, close_button_xpath)
    # assert close_button.is_displayed(), "Close button is not displayed"
    # close_button.click()
    
    
    driver.quit()
    