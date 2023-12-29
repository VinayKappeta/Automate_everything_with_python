from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
#service = Service('/workspace/chromedriver.exe')
service = webdriver.ChromeService(executable_path=binary_path)

def get_driver():
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument('disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(service = service, options=options)
  driver.get('http://automated.pythonanywhere.com')
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by = 'xpath',value='/html/body/div[1]/div/h1[1]')
  return element.text

print(main())
webdriver.Chrome()