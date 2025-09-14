from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import json

# 자동값 (고정)
EMAIL = "vvv861005@gmail.com"
PASSWORD = "rnjsgksrhksflwk"
STORE_NAME = "autostore"

def full_auto():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("🚀 Shopify Partner 자동 가입 중...")
        driver.get("https://partners.shopify.com/signup")
        wait = WebDriverWait(driver, 15)

        wait.until(EC.presence_of_element_located((By.NAME, "user[email]"))).send_keys(EMAIL)
        driver.find_element(By.NAME, "user[password]").send_keys(PASSWORD)
        driver.find_element(By.NAME, "user[first_name]").send_keys("Auto")
        driver.find_element(By.NAME, "user[last_name]").send_keys("Bot")
        driver.find_element(By.NAME, "user[company]").send_keys("AutoBot")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)

        print("✅ 개발 스토어 자동 생성 중...")
        driver.get("https://partners.shopify.com/current/apps/development_stores/new")
        wait.until(EC.presence_of_element_located((By.NAME, "store[name]"))).send_keys(STORE_NAME)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        print("✅ Admin API 키 자동 발급 중...")
        driver.get("https://partners.shopify.com/current/apps/private/new")
        wait.until(EC.presence_of_element_located((.By.NAME, "app[name]"))).send_keys("AutoApp")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # API 키 추출
        token = driver.find_element(By.XPATH, "//code").text
        with open(".env", "a") as f:
            f.write(f"\nSHOPIFY_TOKEN={token}\n")
        print("✅ API 키 저장 완료:", token)

        print("✅ 모두 완료! 이제 main.py 실행하세요.")
    except Exception as e:
        print("❌ 오류:", e)
        driver.save_screenshot("error.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    full_auto()
