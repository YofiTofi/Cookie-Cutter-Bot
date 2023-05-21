from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def update_prices():
    for key in upgrades:
        pass

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie")
mouse = driver.find_element(By.ID, "cookie")
upgrades = {"buyTime machine":0, "buyPortal":0, "buyAlchemy lab":0, "buyShipment":0, "buyMine":0, "buyFactory":0,
            "buyGrandma":0, "buyCursor":0}
timeout = time.time() + 5
while True:
    if time.time() > timeout:
        for key in upgrades.keys():
            purchase = driver.find_element(By.ID, key)
            try:
                purchase.click()
            except:
                mouse.click()
        timeout = time.time() + 5
    else:
        mouse.click()