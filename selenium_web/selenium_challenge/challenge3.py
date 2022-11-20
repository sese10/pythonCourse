# navigate any browser to https://weather.com/ get the current temperature and print it out in the terminal.
# then print out the temperature for Morning, Afternoon, Evening and Overnight.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com/weather/today/")
    current_condition = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[1]/div/section/div')
    print("Current Temperature:", current_condition.text)
    morning = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[7]/section/div/ul/li[1]')
    print("Morning Temperature:", morning.text)
    afternoon = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[7]/section/div/ul/li[2]')
    print("Afternoon Temperature:", afternoon.text)
    evening = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[7]/section/div/ul/li[3]')
    print("Evening Temperature:", evening.text)
    overnight = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[7]/section/div/ul/li[4]')
    print("Overnight Temperature:", overnight.text)


if __name__ == '__main__':
    main()
