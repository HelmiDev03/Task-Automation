from asyncio import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver

index=0
options = webdriver.ChromeOptions()
# Add any options you need (e.g., headless mode for servers)
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
while True:
    try:
        print (f"iteration {index+1}")    
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 30)  # Increased timeout to 30 seconds
        # Open the initial URL
        driver.get('https://learn.microsoft.com/training/paths/security-copilot-and-ai/?wt.mc_id=studentamb_394481')

        # Click on the "Start" button
        start_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start-path"]')))
        start_button.click()

       

        for i in range(9):
            try:
                button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="next-section"]/div/div/p/a')))
                button1.click()
                time.sleep(1)
            except:
                break

        button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quiz-choice-2-0"]')))
        button1.click()
        button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quiz-choice-1-0"]')))
        button1.click()
        button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quiz-choice-0-0"]')))
        button1.click()
        button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unit-inner-section"]/form/fieldset/button')))
        button1.click()
        button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quiz-button-holder"]/div/a')))
        button1.click()
        time.sleep(1)
        button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="next-section"]/div/div/p/a')))
        button1.click()
        time.sleep(5)
        print (f"iteration {index+1} success")   
        driver.quit()
   

    except:
        print (f"iteration {index+1} failed")    
    index+=1    

