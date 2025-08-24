import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# ==== CONFIGURATION ====
HEADLESS = True                      # Set False for debugging
COIN_LIMIT = 10                      # Number of coins to scrape
WAIT_TIME_SECONDS = 10               # Max wait for page load
SAVE_PATH = "crypto_data.csv"        # Output file path

def scrape_crypto_data():
    # Setup Chrome
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    driver.get("https://coinmarketcap.com/")
    WebDriverWait(driver, WAIT_TIME_SECONDS).until(
        EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr'))
    )

    coins = driver.find_elements(By.XPATH, '//tbody/tr')[:COIN_LIMIT]
    data = []
    for coin in coins:
        try:
            name = coin.find_element(By.XPATH, './/td[3]//p').text
        except:
            name = "N/A"
        try:
            price = coin.find_element(By.XPATH, './/td[4]//span').text
        except:
            price = "N/A"
        try:
            change_24h = coin.find_element(By.XPATH, './/td[5]//span').text
        except:
            change_24h = "N/A"
        try:
            market_cap = coin.find_element(By.XPATH, './/td[7]//span').text
        except:
            market_cap = "N/A"
        data.append([name, price, change_24h, market_cap])
    driver.quit()

    # Create DataFrame
    df = pd.DataFrame(data, columns=["Name", "Price", "24h Change", "Market Cap"])
    df["Timestamp"] = datetime.now()

    # Show in terminal
    print("\n Scraped Data:\n")
    print(df.to_string(index=False))

    # Save to CSV
    os.makedirs(os.path.dirname(SAVE_PATH) or ".", exist_ok=True)
    df.to_csv(SAVE_PATH, mode="a", index=False, header=not os.path.exists(SAVE_PATH))
    print(f"\n Data saved to {SAVE_PATH}")

if __name__ == "__main__":
    scrape_crypto_data()


