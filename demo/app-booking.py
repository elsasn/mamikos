from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path="/Users/user/Downloads/geckodriver")

print("Akses URL")
driver.get("https://mamikos.com/room/kost-kabupaten-simeulue-kost-campur-eksklusif-kos-agen-duo-tenant-1#/")
print(driver.title)
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@class='booking-input-checkin__input']").click()
driver.find_element(By.XPATH, "//span[@class='cell day']").click()
driver.find_element(By.XPATH, "//div[@role='radiobutton']").click()
driver.find_element(By.XPATH, "//button[@class='mami-button booking-card__booking-action track_request_booking mami-button--primary mami-button--large mami-button--block']").click()
print("Login - Input Nomor HP dan Password")
print(driver.current_url)
get_username = driver.find_element(By.XPATH, '//input[@type="tel"]')
get_username.send_keys("083159526508")
get_password = driver.find_element(By.XPATH, '//input[@type="password"]')
get_password.send_keys("Password123")
submit = driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-mamigreen login-button track-login-tenant"]')
submit.click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="cell day"]'))).click()
#driver.find_element(By.XPATH, "//span[@class='cell day']").click()
driver.find_element(By.XPATH, "//div[@role='radiobutton']").click()
driver.find_element(By.XPATH, "//button[@class='mami-button booking-card__booking-action track_request_booking mami-button--primary mami-button--large mami-button--block']").click()
#driver.implicitly_wait(5)