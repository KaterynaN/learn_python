from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)
cookie = driver.find_element(By.ID, 'cookie')
driver.implicitly_wait(0)

start_time = time.time()
last_checked_time = start_time

used_powers = []
duration = 60
interval = 5

while time.time() - start_time < duration:
    current_time = time.time()
    while current_time - last_checked_time >= interval:
        #----------max result-----------------------
        powers = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed)")
        powers[-1].click()


        #----------------take all achievments---------------
        # powers = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed)")
        # for power in powers:
        #     try:
        #         if power.get_attribute('id') not in used_powers:
        #             power.click()
        #             used_powers.append(power.get_attribute('id'))
        #     except:
        #         print("Stale element reference encountered; moving to the next element.")
        #         continue  # Move to the next power if this one is stale


        last_checked_time = current_time
    cookie.click()

cps = driver.find_element(By.CSS_SELECTOR, '#cps')
money = driver.find_element(By.CSS_SELECTOR, '#money')
print(f"{cps.text}\n money remained: {money.text}")

#close particular tab
# driver.close()
# #close browser
driver.quit()
