import time
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8000"

# TC_LOG_01
def test_login_valid(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/login.php")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    assert "login.php" not in driver.current_url or "selamat datang" in driver.page_source.lower()

# TC_LOG_02
def test_login_invalid(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/login.php")
    driver.find_element(By.NAME, "username").send_keys("salahuser")
    driver.find_element(By.NAME, "password").send_keys("salahpass")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    assert "salah" in driver.page_source.lower() or "login.php" in driver.current_url

# TC_LOG_03
def test_login_empty(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/login.php")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(1)

    assert "login.php" in driver.current_url

# TC_LOG_04
def test_login_sql_injection(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/login.php")
    driver.find_element(By.NAME, "username").send_keys("admin' OR '1'='1")
    driver.find_element(By.NAME, "password").send_keys("bebas123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    assert "login.php" in driver.current_url or "salah" in driver.page_source.lower()
