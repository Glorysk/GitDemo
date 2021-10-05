import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

option1 = Options()
option1.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path="C:\\Users\\Glory\\OneDrive\\Documents\\Drivers\\chromedriver.exe",chrome_options=option1)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.irctc.co.in/")
print(driver.title)
time.sleep(3)
scrol = driver.find_element_by_tag_name('html')
scrol.send_keys(Keys.END)
time.sleep(3)

#Ok button
driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button').click()
time.sleep(4)

start = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input').send_keys('KALABURAGI - KLBG')
time.sleep(4)
#KLBG dropdown value click madthu
driver.find_element(By.XPATH, '//*[@id="destination"]/span/input').send_keys('SBC')
time.sleep(6)

driver.find_element(By.XPATH, '//*[@id="destination"]/span/div').click()
time.sleep(3)

#sleeper class

driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div').click()
time.sleep(2)
#sleeper class dropdown valule

driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[4]/div/ul/p-dropdownitem[10]/li').click()
time.sleep(3)

#calander

driver.find_element(By.XPATH, '//*[@id="jDate"]/span/input').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="jDate"]/span/div/div/div[1]/a[2]/span').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="jDate"]/span/div/div/div[2]/table/tbody/tr[1]/td[7]').click()

time.sleep(4)
#Search

driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button').click()
time.sleep(15)


#login button

driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]').click()

time.sleep(4)

#User name

driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys("Glorysk")
time.sleep(5)
#Password

driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys("Window1998")

time.sleep(5)

#Captcha:

driver.find_element(By.XPATH, '//*[@id="nlpAnswer"]').click()
time.sleep(20)
#Sign ON

driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button').click()