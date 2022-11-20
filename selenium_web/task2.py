# visit the website https://academy.testifyltd.com/
# locate the button with the text "Explore Courses" and print out the element
# locate the element with the text "Subscribe to receive training updates from Testify" and print it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_link_text(driver):
    explore_courses_link = driver.find_element(By.XPATH, "/html/body/div/main/section[8]/div/div/div[1]/div[2]/button/span[1]")
    print("EXPLORE COURSES:", explore_courses_link)


def locate_by_link_text2(driver):
    subscribe_to_receive_training_updates_from_testify_link = driver.find_element(By.XPATH, "/html/body/div/main/section[11]/div/div/div[1]/h2")
    print("SUBSCRIBE TRAINING:", subscribe_to_receive_training_updates_from_testify_link)
    """subscribe_to_receive_training_updates_from_testify_link = driver.find_element(By.TAG_NAME, "h2")
    print("SUBSCRIBE TRAINING:", subscribe_to_receive_training_updates_from_testify_link)"""


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_link_text(driver)
    locate_by_link_text2(driver)


if __name__ == '__main__':
    main()
