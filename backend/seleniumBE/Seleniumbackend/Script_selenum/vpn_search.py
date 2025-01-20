# vpn_search.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess

def change_vpn_location(country_name):
    try:
        command = f"nordvpn -c -g {country_name}" 
        subprocess.run(command, shell=True, check=True)
        time.sleep(5)  # Wait for the VPN to connect
    except Exception as e:
        print(f"Error changing VPN location: {e}")

def perform_search(keyword):
    """Automate keyword search on DuckDuckGo."""
    try:
        # Set up Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Open DuckDuckGo
        driver.get("https://duckduckgo.com")
        time.sleep(2)

        # Enter the keyword and search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Click the first ad link
        try:
            ad_link = driver.find_element(By.CLASS_NAME, "ad-link") 
            ad_link.click()
            time.sleep(5)  # Browse briefly
            result = f"Clicked on ad for keyword: {keyword}"
        except Exception as e:
            result = f"No ad found for keyword: {keyword}"

        driver.quit()
        return result
    except Exception as e:
        return f"Error during search: {e}"
