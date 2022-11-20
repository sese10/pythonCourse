# using any browser navigate to any YouTube video of your choice
# allow your script to wait for the comments to load then get the first two comments
# print them in the terminal


import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=e2QRV7Bxg2E&list=RDe2QRV7Bxg2E&start_radio=1/")
    action = ActionChains(driver)
    driver.maximize_window()
    web_driver_wait = WebDriverWait(driver, 40)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'ytd-comment-renderer')))
    comments = driver.find_elements(By.TAG_NAME, 'ytd-comment-renderer')
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content-text')
        print(comment_content.text)
    time.sleep(5)


if __name__ == '__main__':
    main()
