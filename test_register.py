import time
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8000"

# TC_REG_01
def test_register_valid(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/register.php")
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "email").send_keys("test@pengupil.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "repassword").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    # Sukses jika redirect ke index.php atau login.php (bukan tetap di register.php dengan error)
    assert "register.php" not in driver.current_url or "berhasil" in driver.page_source.lower()

# TC_REG_02
def test_register_empty(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/register.php")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(1)

    assert "kosong" in driver.page_source.lower() or "register.php" in driver.current_url

# TC_REG_03
def test_register_duplicate(driver):
    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/register.php")
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "email").send_keys("test@pengupil.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "repassword").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    assert "register.php" in driver.current_url or "sudah" in driver.page_source.lower()
