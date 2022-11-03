import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_tag_name(driver):
    first_input = driver.find_element(By.TAG_NAME, "input")
    print("first Input Element:", first_input)
    div_elements = driver.find_elements(By.TAG_NAME, "div")
    print("Total Divs:", len(div_elements))
    for div_element in div_elements:
        print("Div Element:", div_element)


def locate_by_css_selector(driver):
    firstname_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.contact-section > div" )
    print("Firstname Element By CSS Selector:", firstname_element)
    input_elements = driver.find_elements(By.CSS_SELECTOR, "div.relative")
    print("Total Divs:", len(input_elements))
    for input_element in input_elements:
        print("Div Element:", input_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    # locate_by_tag_name(driver)
    locate_by_css_selector(driver)


if __name__ == '__main__':
    main()
