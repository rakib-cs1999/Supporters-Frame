from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)


try:
    # Go to website
    driver.get("https://supportersframe.com/")
    driver.maximize_window()
    
    
    # Click on sidebar button 
    sidebar_button = driver.find_element(By.XPATH, "//button[@id='desktop-hamburger']//i[@class='fa-solid fa-bars']")
    sidebar_button.click()
    

    # Click on Leaderboard
    leaderboard = driver.find_element(By.XPATH, "//ul[contains(@class,'flex flex-col space-y-2 px-4 py-2 text-gray-700 min-h-screen')]//a[contains(@class,'block hover:bg-gray-300 py-2 px-3 rounded-md')][normalize-space()='Leaderboard']")
    leaderboard.click()
    

    # Locate filter buttons 
    filters = ["7 days", "30 days", "All"]

    for f in filters:
        try:
            button = driver.find_element(By.XPATH, f"//button[normalize-space()='{f}']")
            button.click()
            
        except Exception as e:
            print(f"Could not click {f}: {e}")

    

    # back to main content
    driver.switch_to.default_content()


    # Click on explore button
    explore = driver.find_element(By.XPATH, "//i[@class='fa-solid fa-compass text-gray-600 bg-gray-200 py-2 px-3 rounded-full hover:text-blue-600 cursor-pointer text-xl transition-colors']")
    explore.click()
    

    # Click on campaign
    campaign = driver.find_element(By.XPATH, "//div[contains(@class,'grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-2')]//div[1]//div[1]//div[1]//a[1]//div[1]//button[1]")
    campaign.click()
    

    # Scrll down 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    

    # Click on more campaign
    more_campaign = driver.find_element(By.XPATH, "//h3[normalize-space()='More Campaigns']")
    more_campaign.click()
    

    # back to main content
    driver.switch_to.default_content()

    # Click on privacy policy
    privacy_policy = driver.find_element(By.XPATH, "//a[normalize-space()='Privacy Policy']")
    privacy_policy.click()
    

    # Scrll down 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    

    # click on www.supportersframe.com 
    contact_us_link = driver.find_element(By.XPATH, "//span[normalize-space()='www.supportersframe.com']")
    contact_us_link.click()
    driver.back()
    

    # back to main content
    driver.switch_to.default_content()
        
    # Send text for search
    driver.find_element(By.XPATH, "//input[@class='w-full pl-4 pr-4 py-2 rounded-full border border-gray-300 focus:outline-none focus:border-blue-500 transition-all']").send_keys("boishakh campaign")
    

    # Click on search button
    search_button = driver.find_element(By.XPATH, "//i[@class='fa-solid fa-magnifying-glass text-black']")
    search_button.click()
    


finally:
    driver.quit()