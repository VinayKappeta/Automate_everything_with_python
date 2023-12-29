from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
def get_driver():
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument('disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options=options)
  driver.get('http://automated.pythonanywhere.com/login/')
  return driver

def clean_text(text):
  """Extract only temperature from text"""
  output = float(text.split(": ")[1])
  return output
def write_file(text):
  """Write input texgt into a text file"""
  filename = f'{dt.now().strftime("%Y-%m-%d.%H-%M-%s")}.txt'
  with open(filename,'w') as file:
    file.write(text)

def login(driver):
  driver.find_element(by = 'id',value='id_username').send_keys('automated')
  time.sleep(2)
  driver.find_element(by = 'id',value='id_password').send_keys('automatedautomated'+Keys.RETURN)
  time.sleep(2)
  driver.find_element(by = 'xpath',value = "/html/body/nav/div/a").click()
  print(driver.current_url)
def main():
  driver = get_driver()
  login(driver)
  while True:
    time.sleep(2)
    text = driver.find_element(by = 'xpath',value = '/html/body/div[1]/div/h1[2]').text
    text2 = str(clean_text(text))
    print(text2)
    write_file(text2)

print(main())

