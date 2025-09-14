from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_shopify_partner_account():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("🚀 Shopify Partner 페이지 로딩 중...")
        driver.get("https://partners.shopify.com/signup")
        wait = WebDriverWait(driver, 15)

        print("⏳ 이메일 입력 대기 중...")
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "user[email]")))
        email_field.send_keys("vvv861005@gmail.com")

        driver.find_element(By.NAME, "user[password]").send_keys("rnjsgksrhksflwk")
        driver.find_element(By.NAME, "user[first_name]").send_keys("Auto")
        driver.find_element(By.NAME, "user[last_name]").send_keys("Bot")
        driver.find_element(By.NAME, "user[company]").send_keys("AutoBot")

        print("✅ 회원가입 제출 중...")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)

        print("✅ 개발 스토어 생성 중...")
        driver.get("https://partners.shopify.com/current/apps/development_stores/new")
        store_name_field = wait.until(EC.presence_of_element_located((By.NAME, "store[name]")))
        store_name_field.send_keys("autostore")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        print("✅ 스토어 생성 완료: autostore.myshopify.com")

    except Exception as e:
        print("❌ 오류 발생:", e)
        driver.save_screenshot("error.png")  # 디버깅용 스크린샷
    finally:
        driver.quit()

if __name__ == "__main__":
    create_shopify_partner_account()
