import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Users\\Glory\\OneDrive\\Documents\\Drivers\\chromedriver.exe")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.dell.com/")
time.sleep(5)
laptop=driver.find_element(By.CSS_SELECTOR, '#category-bar > div:nth-child(1) > div > div.hpg-cat-label')
time.sleep(2)
act=ActionChains(driver)
act.move_to_element(laptop).perform()
driver.find_element(By.XPATH, '//*[@id="category-bar"]/div[1]/div/div[2]/a[1]').click()
time.sleep(3)
scrol = driver.find_element_by_tag_name('html')
scrol.send_keys(Keys.END)
time.sleep(5)
scrol.send_keys(Keys.HOME)
time.sleep(5)

driver.find_element(By.XPATH, '//input[@name="9975"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="icc-c784502win8"]/section[1]/div[3]/a/img').click()
time.sleep(2)
desc = driver.find_element(By.XPATH, '//*[@id="cf-body"]/div[4]/div[2]/div[4]/ul')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#cf-body > div.row.cf-hero-section > div.col.cf-hero-details > div.cf-padding-bottom-10.cta_form > button').click()

time.sleep(5)

driver.quit()
