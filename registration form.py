from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

driver = webdriver.Chrome()

driver.get("https://vinothqaacademy.com/demo-site/")
time.sleep(10)

First_name = driver.find_element(By.NAME, "vfb-5").send_keys("Jayavarsha")
time.sleep(2)
Last_name = driver.find_element(By.NAME, "vfb-7").send_keys("Thainees")
time.sleep(2)

Gender = driver.find_element(By.ID, "vfb-31-2").click()
time.sleep(2)

course = driver.find_element(By.ID, "vfb-20-0").click()
time.sleep(2)

address = driver.find_element(By.NAME, "vfb-13[address]").send_keys("Arul nagar")
time.sleep(2)

building = driver.find_element(By.NAME, "vfb-13[address-2]").send_keys("52")
time.sleep(2)

city = driver.find_element(By.NAME, "vfb-13[city]").send_keys("Chennai")
time.sleep(2)

state = driver.find_element(By.NAME, "vfb-13[state]").send_keys("Tamilnadu")
time.sleep(2)   

pincode = driver.find_element(By.NAME, "vfb-13[zip]").send_keys("600097")
time.sleep(2)

# country = driver.find_element(By.CLASS_NAME, "select2-selection__arrow").click()
# time.sleep(1)

# text = driver.find_element(By.NAME, "select2-search__field").send_keys("India")
# time.sleep(2)

Email = driver.find_element(By.NAME, "vfb-14").send_keys("jayavarsha23219@gmail.com")
time.sleep(10)