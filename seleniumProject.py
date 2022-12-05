from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def main():
    wd = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
    url = "https://portal-cn.fpmarkets.com/sessions/signin"
    username = "hong344763175@outlook.com"
    password = "guan123456"
    wd.get(url)
    # print(wd.page_source)
    WebDriverWait(wd, timeout=30)
    wd.find_element(By.XPATH,'//input[@name="username"]').send_keys(username)
    wd.find_element(By.XPATH,'//input[@name="password"]').send_keys(password)
    wd.find_elements(By.XPATH,'//botton[@color="primary"]').click()

    wd.close()
    wd.quit()

if __name__ == '__main__':
    main()