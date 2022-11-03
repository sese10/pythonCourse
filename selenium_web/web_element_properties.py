from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def print_element_properties(element):
    print("Checked State:", element.get_property("checked"))



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://w3.org/WAI/ARIA/apg/example-index/checkbox/checkbox-mixed")
    lettuce_checkbox = driver.find_element(By.ID, "cond1")
    tomatoes_checkbox = driver.find_element(By.ID, "cond2")
    mustard_checkbox = driver.find_element(By.ID, "cond3")
    sprouts_checkbox = driver.find_element(By.ID, "cond4")
    print_element_properties(lettuce_checkbox)
    print_element_properties(tomatoes_checkbox)
    print_element_properties(mustard_checkbox)
    print_element_properties(sprouts_checkbox)
    time.sleep(30)



if __name__ == '__main__':
    main()
