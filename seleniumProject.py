from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

start_date = "1/12/2022"
end_date = "7/12/2022"
start_date_dt = datetime.strptime(start_date,r"%d/%m/%Y")
end_date_dt = datetime.strptime(end_date,r"%d/%m/%Y")
platform_list = ["MT4", "MT5"]
account_list = ["34316","34330"]

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': r'D:\FPReporting\20221211\MT4'}
service = Service(executable_path=ChromeDriverManager().install())
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=service, options = options)
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

#wait
calendar = driver.find_elements(By.XPATH,'//button[@aria-label="Open calendar"]')
start_date_year = start_date_dt.year
start_date_month = start_date_dt.strftime("%B")
start_date_day = start_date_dt.day
end_date_year = end_date_dt.year
end_date_month = end_date_dt.strftime("%B")
end_date_day = end_date_dt.day

calendar[0].click()
driver.find_element(By.XPATH,'//div[@class="mat-calendar-arrow"]').click()
driver.find_element(By.XPATH,'//td[@aria-label="'+str(start_date_year)+'"]').click()
driver.find_element(By.XPATH,'//td[@aria-label="'+start_date_month+' '+str(start_date_year)+'"]').click()
driver.find_element(By.XPATH,'//td[@aria-label="'+start_date_month+' '+str(start_date_day)+', '+str(start_date_year)+'"]').click()

calendar[1].click()
driver.find_element(By.XPATH,'//div[@class="mat-calendar-arrow"]').click()
driver.find_element(By.XPATH,'//td[@aria-label="'+str(end_date_year)+'"]').click()
driver.find_element(By.XPATH,'//td[@aria-label="'+end_date_month+' '+str(end_date_year)+'"]').click()
driver.find_element(By.XPATH,'//td[@aria-label="'+end_date_month+' '+str(end_date_day)+', '+str(end_date_year)+'"]').click()

driver.find_element(By.XPATH,'//span[text()="Include All Sub-IBs"]').click()

platform = platform_list[0]
driver.find_element(By.XPATH,'//mat-select[@aria-label="PLATFORM"]').click()
driver.find_element(By.XPATH,'//span[@class="mat-option-text" and text()="'+ platform +'"]').click()

#  ------------- repeat download progress --------------
account = account_list[0]
driver.find_element(By.XPATH,'//mat-select[@aria-label="IB"]').click()
driver.find_element(By.XPATH,'//span[@class="mat-option-text" and text()="'+ account +'"]').click()
driver.find_element(By.XPATH,'//div[@class="cdk-overlay-container"]').click()
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
#wait shortly
driver.find_element(By.XPATH,'//span[@class="mat-button-wrapper" and text()="OK"]').click()
#wait longer 
driver.find_element(By.XPATH,'//span[@class="mat-button-wrapper" and text()=" Refresh "]').click()
#if status is still In Progress, wait and refresh again, until status turn cloud_download
driver.find_elements(By.XPATH,'//mat-icon[@role="img" and text()="cloud_download"]')[1].click()
#after download finish
driver.find_elements(By.XPATH,'//mat-icon[@role="img" and text()="cancel"]')[0].click()
driver.find_element(By.XPATH,'//span[@class="mat-button-wrapper" and text()="Confirm"]').click()
driver.find_element(By.XPATH,'//mat-select[@aria-label="IB"]').click()
driver.find_element(By.XPATH,'//span[@class="mat-option-text" and text()="'+ account +'"]').click()
driver.find_element(By.XPATH,'//div[@class="cdk-overlay-container"]').click()
# ------------------------------------------------------------

# driver.close()
# driver.quit()
