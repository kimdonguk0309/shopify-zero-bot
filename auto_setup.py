from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

EMAIL = input("이메일: ")
PASSWORD = input("비밀번호: ")
STORE_NAME = input("스토어 이름: ")

def create_shopify_partner_account():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://partners.shopify.com/signup")
    time.sleep(3)

    driver.find_element(By.NAME, "user[email]").send_keys(EMAIL)
    driver.find_element(By.NAME, "user[password]").send_keys(PASSWORD)
    driver.find_element(By.NAME, "user[first_name]").send_keys("Auto")
    driver.find_element(By.NAME, "user[last_name]").send_keys("Bot")
    driver.find_element(By.NAME, "user[company]").send_keys("AutoBot")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # 개발 스토어 생성
    driver.get("https://partners.shopify.com/current/apps/development_stores/new")
    driver.find_element(By.NAME, "store[name]").send_keys(STORE_NAME)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    print("✅ Shopify 개발 스토어 생성 완료:", STORE_NAME + ".myshopify.com")
    driver.quit()

if __name__ == "__main__":
    create_shopify_partner_account()
