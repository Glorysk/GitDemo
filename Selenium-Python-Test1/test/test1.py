import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Users\\Glory\\OneDrive\\Documents\\Drivers\\chromedriver.exe")

driver.get("https://www.flipkart.com/")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div[3]/a/div[1]/div/img').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/a/div/img').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[1]/div[2]/div/span/label/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[1]/div[2]/div/span/label/div').click()
time.sleep(2)
min = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[1]/select')
time.sleep(2)
select = Select(min)
time.sleep(2)
select.select_by_value('7000')
time.sleep(2)
scrol = driver.find_element_by_tag_name('html')
scrol.send_keys(Keys.END)
time.sleep(5)
scrol.send_keys(Keys.HOME)
time.sleep(5)
print(driver.title)
driver.quit()
