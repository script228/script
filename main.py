from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options)
driver.get("https://достижения.рф/achievements/region/601")
t = 0
while True:
    xpath = '//*[@id="__nuxt"]/div/main/div/div[2]/div[3]/div[1]/div[2]/div[2]/button'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    # driver.delete_all_cookies()
    driver.execute_script('localStorage.clear();')
    print(t)
    t += 1
