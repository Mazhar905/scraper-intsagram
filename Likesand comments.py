import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(executable_path=CM().install(), options=options)
# driver.set_window_size(600, 1000)
driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/')

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
  database = "userdetails"
)
print(mydb)
mycursor = mydb.cursor()



def get_user_info(user):
    driver.get('https://www.instagram.com/{}/'.format(user))
    time.sleep(5)
    print("[Info] - Getting "+user+" Info...")
    time.sleep(5)
    URL = driver.current_url
    accountUsername = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]//h2").text
    accountName = driver.find_element(
        By.XPATH, "//span[@class='_aacl _aacp _aacw _aacx _aad7 _aade']").text
    userFollowers = driver.find_element(
        By.XPATH, "//a[@role='link']/div/span[@class ='_ac2a']").get_attribute('title')
    Foll_int = int(userFollowers.replace(',', ''))
    return {
        'AccountUser': accountUsername,
        'AccountURL': URL,
        'AccountName': accountName,
        'Follower': Foll_int
    }


def login(username, password):
    time.sleep(2)
    print("[Info] - Logging in...")

    user_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

    user_element.send_keys(username)

    pass_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

    pass_element.send_keys(password)

    login_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))
    time.sleep(0.4)
    login_button.click()
    time.sleep(5)


# Complete these 2 fields ==================
# USERNAME = input('Enter Your Username: ')
# PASSWORD = input('Enter Your Password: ')
# usr = input('[Required] - Whose followers do you want to scrape: ')
# user_input = int(input('[Required] - How many followers do you want to scrape (60-500 recommended): '))
USERNAME = 'mazhardev1' #'iambadmunda21' 
PASSWORD =  'Mazhar.123' #'01478520.369' 
usr = "khloekardashian"
# ==========================================
TIMEOUT = 15
login(USERNAME, PASSWORD)
# thistuple = ("apple", "banana", "cherry")
mycursor.execute("SELECT USERNAME FROM user_list")

# This SQL statement selects all data from the CUSTOMER table.
result = mycursor.fetchall()

for i in result:
    # print(result[i])
    data = get_user_info(i[0])
    print(data)
    # print("Here is the another")
    # print(i[0])
