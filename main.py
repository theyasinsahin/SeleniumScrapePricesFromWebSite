
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

product = "uyku tulumu"
driver = webdriver.Chrome()
def trendyol_products_prices(driver, product):
    #To website
    driver.get("https://www.trendyol.com/")

    #wait
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "homepage-popup-gender")))
    page = driver.find_element(By.CLASS_NAME, "homepage-popup-gender")
    page.click()
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "N4M8bfaJ")))

    #write item that what you want
    search_label = driver.find_element(By.CLASS_NAME,"V8wbcUhU")
    search_label.send_keys(product)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "cyrzo7gC")))

    #click to search button
    search_button = driver.find_element(By.CLASS_NAME, "cyrzo7gC")
    search_button.click()

    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "hasRatings")))

    #get the titles
    title_texts = driver.find_elements(By.CLASS_NAME, 'hasRatings')

    #get the prices
    price_texts = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")

    for i in range(19):
        print(f"product title: {title_texts[i].text}\nprice: {price_texts[i].text}")


trendyol_products_prices(driver,product)
