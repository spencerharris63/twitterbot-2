from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

X_EMAIL = os.environ.get("twitter_email")
X_PASSWORD = os.environ.get("twitter_password")
X_USERNAME = os.environ.get("twitter_username")

tweet = "It's HOTDAWGTIME"
gif_search = "hot dogs"

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://twitter.com/?lang=en")

# wait = WebDriverWait(driver, 10)

time.sleep(8)
signin_button = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div")
signin_button.click()

time.sleep(5)

email = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
email.send_keys(X_EMAIL)
email.send_keys(Keys.ENTER)

time.sleep(5)

try:
    username_or_phone_input = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    time.sleep(2)
    username_or_phone_input.send_keys(X_USERNAME)
    username_or_phone_input.send_keys(Keys.ENTER)
except:
    pass

time.sleep(2)

password = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys(X_PASSWORD)
time.sleep(2)
password.send_keys(Keys.ENTER)

time.sleep(5)

tweet_compose = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
tweet_compose.send_keys(tweet)

time.sleep(2)

gif_button = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/nav/div/div[2]/div/div[2]")
gif_button.click()
time.sleep(5)
search_for_gif = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div/label/div[2]/div/input")
search_for_gif.click()
search_for_gif.send_keys(gif_search)
time.sleep(3)
hot_dog_gif = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[5]/div/div[3]/div/img")
hot_dog_gif.click()
time.sleep(3)

post_button = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span")
post_button.click()

time.sleep(3)

driver.quit()
