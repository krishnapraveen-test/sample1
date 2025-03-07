from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.execute_script("window.scrollBy(0, 500);")
#click on the alert button to generate the simple alert
button=driver.find_element(By.XPATH,"//*[text()='Simple Alert']")
button.click()
#switch the control to the alert window
Alert=driver.switch_to.alert
#retrive the message on th alert window
msg=Alert.text
print("Alert shows following message:" + msg)
time.sleep(2)
#use the accept() method to accept the alert
Alert.accept()
    #alert.dismiss()
print("Clicked on the ok button in the alert window")
driver.close
