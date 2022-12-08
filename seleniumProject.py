from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://portal-cn.fpmarkets.com/sessions/signin"
username = "hong344763175@outlook.com"
password = "guan123456"
driver.get(url)

#wait
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys(username)
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(password)
driver.find_element(By.XPATH,'//button[@color="primary"]').click()

#wait
driver.find_element(By.XPATH,'//span[text()="Reporting"]').click()

# driver.close()
# driver.quit()
