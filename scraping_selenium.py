from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import urllib.request
import requests
import pandas as pd


PATH = r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://instagram.com")

#login

def loggedIn(userName, password):
    time.sleep(5)
    user_name = driver.find_element(
        By.XPATH, "//input[@name='username'][@type= 'text']")
    pass_word = driver.find_element(
        By.XPATH, "//input[@name='password'][@type= 'password']")
    user_name.clear()
    pass_word.clear()
    user_name.send_keys(userName)
    pass_word.send_keys(password)
    login = driver.find_element(By.XPATH, "//button[@type= 'submit']").click()

    # save you login info?
    time.sleep(5)
    notnow = driver.find_element(
        By.XPATH, "//button[normalize-space()='Not Now']").click()
    time.sleep(10)
    notnow1 = driver.find_element(
        By.XPATH, "//button[@class='_a9-- _a9_1']").click()


# searchbox
def searchBox(search):
    searchBox = driver.find_element(
        By.XPATH, "//div[@class='_aacl _aacp _aacu _aacx _aada'][normalize-space()='Search']").click()
    time.sleep(5)
    searchBox1 = driver.find_element(
        By.XPATH, "//input[@placeholder='Search']")
    searchBox1.clear()
    searchBox1.send_keys(search)
    searchBox1.send_keys(Keys.ENTER)
    time.sleep(5)
    searchBox1.send_keys(Keys.ENTER)

def user_data():
    URL = driver.current_url
    time.sleep(10)
    accountUsername = driver.find_element(By.XPATH, "//a[@href = '#'][@role ='link']/h2").text
    accountName = driver.find_element(By.XPATH, "//span[@class='_aacl _aacp _aacw _aacx _aad7 _aade']").text
    accountFollowers = driver.find_element(By.XPATH, "//a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']/span[@class ='_ac2a']").get_attribute('title')
    print(URL,accountUsername, accountName, accountFollowers)

# main
loggedIn("iambadmunda21", "Mazhar.122")
searchBox("leomessi")
time.sleep(10)
user_data()
Following = driver.find_element(By.XPATH, "//a[@href='/leomessi/following/']//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
time.sleep(5)
n = driver.find_element(By.XPATH, "//a[@role='link']//span[contains(@class,'_aacl _aaco _aacw _aacx _aad7 _aade')]//div[contains(@class,'_ab94 _ab97 _ab9f _ab9k _ab9p _abcm')]").click()
time.sleep(5)
user_data()

