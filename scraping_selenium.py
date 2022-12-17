from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import requests

# proxy
# prox =Proxy()
# prox.proxy_type = ProxyType.MANUAL

# chrome_options = Options()
# chrome_options.binary_location="../Google Chrome"
# chrome_options.add_argument("disable-infobars")
# driver = webdriver.Chrome(chrome_options=chrome_options)

PATH= r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"
driver =webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://instagram.com")

# # login
time.sleep(5)

username = driver.find_element(By.XPATH, "//input[@name='username'][@type= 'text']")
password = driver.find_element(By.XPATH, "//input[@name='password'][@type= 'password']")
username.clear()
password.clear()

username.send_keys("iambadmunda21")
password.send_keys("Mazhar.122")
login = driver.find_element(By.XPATH, "//button[@type= 'submit']")
login.click()

#save you login info?
time.sleep(10)
notnow = driver.find_element(By.XPATH, "//button[normalize-space()='Not Now']").click()
time.sleep(10)
notnow1 = driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']").click()
time.sleep(10)


#searchbox
searchBox= driver.find_element(By.XPATH, "//body/div[@id='mount_0_0_eU']/div/div/div[@class='x9f619 x1n2onr6 x1ja2u2z']/div[@class='x9f619 x1n2onr6 x1ja2u2z']/div[@class='x78zum5 xdt5ytf x1n2onr6 x1ja2u2z']/div[@class='x78zum5 xdt5ytf x1n2onr6']/div[@class='x78zum5 xdt5ytf x1n2onr6 xat3117 xxzkxad']/div[@class='x78zum5 xdt5ytf x10cihs4 x1t2pt76 x1n2onr6 x1ja2u2z']/div[@class='x9f619 xnz67gz x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1qughib']/div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1 xeq5yr9 x1dr59a3 xixxii4 x13vifvy x1n327nk']/div[@class='x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj']/div[@class='x78zum5 x1q0g3np x1dr59a3 x1qughib xleuxlb xxfw5ft x1mh60rb x1f91t4q x1n2onr6']/div[contains(@class,'xvb8j5 x1vjfegm')]/div[contains(@class,'x1cy8zhl x9f619 x78zum5 xdt5ytf x1dr59a3 x1y1aw1k xn6708d xx6bls6 x1ye3gou xvbhtw8 x1xgvd2v x1o5hw5a xaeubzz')]/div[@class='xh8yej3 x1iyjqo2']/div[2]/div[1]/a[1]/div[1]" ).click()

time.sleep(5)
searchBox1= driver.find_element(By.XPATH, "//input[@placeholder='Search']").click()
searchBox1.clear()
time.sleep(5)
searchBox1.send_keys("leomessi")
time.sleep(5)
searchBox1.send_keys(Keys.Enter)
time.sleep(5)
searchBox1.send_keys(Keys.Enter)
time.sleep(5)

driver.quit()