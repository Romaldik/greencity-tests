import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

if __name__ == "__main__":
    oprions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=oprions)
    wait = WebDriverWait(driver, 10)
    
    driver.maximize_window()
    driver.get(BASE_URL)
    print(driver.title)
    sleep(5)
    
    filter_viewbox_xpath = "//div[@class='mat-mdc-select-arrow ng-tns-c3393473648-0']"
    filter_viewbox = driver.find_element(By.XPATH, filter_viewbox_xpath)
    
    assert filter_viewbox.is_displayed(), "Filter viewbox is not displayed"
    
    filter_viewbox.click()
    
    sleep(2)
    
    category_filter_xpath = "//div[@role='listbox']"
    category_filter = driver.find_element(By.XPATH, category_filter_xpath)
    
    assert category_filter.is_displayed(), "Category filter is not displayed"
    
    category_option_id = 'mat-option-4'
    category_option = driver.find_element(By.ID, category_option_id)
    
    category_option.click()
    assert category_option.is_displayed(), "Category option is not displayed"
    
    # category_anytime_id = 'mat-option-0'
    # category_anytime = driver.find_element(By.ID, category_anytime_id)
    # category_anytime.click()
    # assert category_anytime.is_displayed(), "Category filter Anytime is not displayed"
    
    # sleep(2)
    
    # category_upcoming_id = 'mat-option-4'
    # category_upcoming = driver.find_element(By.ID, category_upcoming_id)
    # category_upcoming.click()
    # assert category_upcoming.is_displayed(), "Category filter Upcoming is not displayed"
    
    #category_Upcoming_xpath = "//mat-option[@class='mat-mdc-option mdc-list-item mat-mdc-option-multiple ng-tns-c3393473648-0 ng-star-inserted mat-mdc-option-active']"
    #categort_Upcoming = driver.find_element(By.XPATH, category_Upcoming_xpath)
    
    #category_upcoming.click()
    #assert category_pcoming.is_displayed(), "Category filter Upcoming is not displayed"
    
    #apply_filter_button_xpath = "//button[@class='apply-filter-btn']"
    #apply_filter_button = driver.find_element(By.XPATH, apply_filter_button_xpath)
    
    #assert apply_filter_button.is_displayed(), "Apply filter button is not displayed"
    
    #apply_filter_button.click()
    
    sleep(5)
    
    
    driver.quit()