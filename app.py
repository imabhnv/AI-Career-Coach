from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://roadmap.sh/react-native")

# wait until the element is present again
wait = WebDriverWait(driver, 30)
element = wait.until(EC.presence_of_element_located((By.ID, "resource-svg-wrap")))

# take screenshot
path = "D:/PROGRAMMING LANGUAGES/PYTHON/justANewProject/android(react native).png"
element.screenshot(path)

driver.quit()