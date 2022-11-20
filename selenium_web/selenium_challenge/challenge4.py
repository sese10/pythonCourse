# navigate to https://www.bbc.com/
# print out the top 10 latest news from the home page.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    news = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]')
    i = 0
    while i < 10:
        print("Headline: ", news.text)
        i = i + 1


if __name__ == '__main__':
    main()
