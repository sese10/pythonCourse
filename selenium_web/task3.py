# navigate to the website https://academy.testifyltd.com/
# get the element with the text "© 2022 Testify Limited. All rights reserved."
# print out the element text, and properties, and it attributes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element_fields(element):
    print("Text:", element.text)
    print("Size:", element.size)
    print("Tag Name:", element.tag_name)
    print("Location:", element.location)
    print("Accessible Name:", element.accessible_name)
    print("Aria Role:", element.aria_role)
    print("ID:", element.id)
    print("Rectangle:", element.rect)


def print_element_attributes(element):
    print("Class:", element.get_attribute("class"))


"""
def print_element_properties(element):
    print("Checked State:", element.get_property("checked")) """


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    # element = driver.find_element(By.TAG_NAME, "h2")
    element = driver.find_element(By.LINK_TEXT, "Academy")
    print_element_fields(element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    # academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    academy_link = driver.find_element(By.TAG_NAME, "form")
    print_element_attributes(academy_link)


"""
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    lettuce_checkbox = driver.find_element(By.ID, "cond1")"""

if __name__ == '__main__':
    main()
