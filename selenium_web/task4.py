# navigate to the website https://www.facebook.com/
# find the email box and enter an email value
# find the password box and enter a password value
# find the Login button and click it

import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    emailField = driver.find_element(By.XPATH, '//*[@id="email"]')
    emailField.click()
    send_keys_to_element(emailField, 'Rita@gmail.com')
    passwordButton = driver.find_element(By.XPATH, '//*[@id="pass"]')
    ActionChains(driver).move_to_element(passwordButton).click(passwordButton).perform()
    send_keys_to_element(passwordButton, '*******')
    driver.find_element(By.TAG_NAME, 'form')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    driver.find_element(By.NAME, "login").click()
    time.sleep(10)



    """emailField = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
    emailField.click()
    send_keys_to_element(emailField, 'Rita@gmail.com')
    passwordButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
    driver.implicitly_wait(5)
    ActionChains(driver).move_to_element(passwordButton).click(passwordButton).perform()
    send_keys_to_element(passwordButton, '*******')
    driver.find_element(By.NAME, 'login').click()"""









if __name__ == '__main__':
    main()
