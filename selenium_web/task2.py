# visit the website https://academy.testifyltd.com/
# locate the button with the text "Explore Courses" and print out the element
# locate the element with the text "Subscribe to receive training updates from Testify" and print it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_link_text(driver):
    explore_courses_link = driver.find_element(By.LINK_TEXT, "Explore Courses")
    print("EXPLORE COURSES:", explore_courses_link)
    """hire_link = driver.find_element(By.LINK_TEXT, "Hire")
    print("Hire Link:", hire_link)"""


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_link_text(driver)


if __name__ == '__main__':
    main()
