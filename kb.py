from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

edge_driver_path = r"E:\Pulpit\msedgedriver.exe"

edge_options = Options()
edge_options.use_chromium = True

service = Service(executable_path=edge_driver_path)

driver = webdriver.Edge(service=service, options=edge_options)

driver.get("https://www.bing.com/")

sleep(5)

search = driver.find_element(By.NAME, "q")

search.send_keys("Cristiano Ronaldo", Keys.RETURN)
sleep(5)
driver.get("https://www.bing.com/")
search = driver.find_element(By.NAME, "q")

search.send_keys("Lionel Messi", Keys.RETURN)

sleep(3)
driver.get("https://www.bing.com/")
search = driver.find_element(By.NAME, "q")

search.send_keys("Lionel Messi", Keys.RETURN)


sleep(15)
driver.quit()
