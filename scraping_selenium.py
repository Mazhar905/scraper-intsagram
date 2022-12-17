from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import requests
# import mysql
# .connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword"
# )

# print(mydb)

PATH = r"C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://instagram.com")

# # login
time.sleep(10)

username = driver.find_element(
    By.XPATH, "//input[@name='username'][@type= 'text']")
password = driver.find_element(
    By.XPATH, "//input[@name='password'][@type= 'password']")
username.clear()
password.clear()

username.send_keys("iambadmunda21")
password.send_keys("Mazhar.122")
login = driver.find_element(By.XPATH, "//button[@type= 'submit']")
login.click()

# save you login info?
time.sleep(10)
notnow = driver.find_element(
    By.XPATH, "//button[normalize-space()='Not Now']").click()
time.sleep(10)
notnow1 = driver.find_element(
    By.XPATH, "//button[@class='_a9-- _a9_1']").click()
time.sleep(10)


# searchbox
searchBox = driver.find_element(
    By.XPATH, "//div[@class='_aacl _aacp _aacu _aacx _aada'][normalize-space()='Search']").click()

time.sleep(5)
searchBox1 = driver.find_element(
    By.XPATH, "//input[@placeholder='Search']")
searchBox1.clear()
searchBox1.send_keys("leomessi")
searchBox1.send_keys(Keys.ENTER)
time.sleep(5)
searchBox1.send_keys(Keys.ENTER)
time.sleep(5)

accountName = driver.find_element(
    By.XPATH, "//h2[@class='_aacl _aacs _aact _aacx _aada']")
accountFollowers = driver.find_element(
    By.XPATH, "//a[@href='/leomessi/followers/']")
