import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    driver.get(BASE_URL)
   
    sleep(5) 
    
    search_icon_xpath = "//div[contains(@class, 'container-img')]"
    search_icon = driver.find_element(By.XPATH, search_icon_xpath)
    search_icon.click()
    # assert search_icon.is_displayed(), "Search icon is not displayed"

    sleep(2)
    
    search_input_xpath = "//input[@placeholder='Search']"
    search_input = driver.find_element(By.XPATH, search_input_xpath)
    assert search_input.is_displayed(), "Search input is not displayed"
    
    search_text = "Event"
    search_input.send_keys(search_text + "\n")
    sleep(5)

    try:
        result_card = driver.find_element(By.XPATH, "//div[(@class='image-container')]")
        assert result_card.is_displayed(), "Result card is not displayed"
        if result_card.is_displayed():
            print("Є івенти!")
    except:
        print("Немає івентів!")

    driver.quit()