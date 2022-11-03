from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path="C:/Program Files/chromedriver5.exe")
    driver.get("http://www.google.com")
    sleep(2000)
    driver.close()


main()
