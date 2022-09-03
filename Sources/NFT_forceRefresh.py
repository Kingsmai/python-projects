from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SUCCESS_MSG = "We've queued this item for an update! Check back in a minute..."


failed_no = []

try:
    driver = webdriver.Firefox()
    start_time = time.time()
    for i in range(0, 8888):
        url = f"https://opensea.io/assets/matic/0xe63b8e3fc67af4afa4022e2b28e3d7761ac8f74f/{i}"
        try:
            driver.get(url)
            btn = driver.find_element(By.CSS_SELECTOR, "button.sc-1xf18x6-0.sc-glfma3-0.hiIVBZ.gVeaIW.sc-1skvztv-0.fPnOUC:nth-child(1)")
            btn.click()
            time.sleep(0.2)
            msg = driver.find_element(By.CSS_SELECTOR, "#__next > div.sc-1xf18x6-0.sc-1twd32i-0.sc-ihijgw-0.haVRLx.kKpYwv.gpOOSX > div > div.sc-1xf18x6-0.sc-1twd32i-0.iQOhGx.kKpYwv")
            if msg.text != SUCCESS_MSG:
                failed_no.append(i)
        except:
            failed_no.append(i)
        finally:
            current_time = time.time()
            estimateTime = round(((current_time - start_time) / (i + 1) * 8888) / 60, 2)
            print(f"Processing: {url}, estimate time: {estimateTime}mins")
            time.sleep(0.8)
finally:
    success = True
    print(f'Operation {"SUCCESS" if success else "FAILED"} in {current_time - start_time} seconds')
    print(f'FAILED NFTs => {failed_no}')
try:
    driver.close()
finally:
    print("Browser Closed!")
