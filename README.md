🚀 Cryptocurrency Price Tracker

A Python-based mini project that automatically fetches real-time cryptocurrency prices from CoinMarketCap
 using Selenium and saves them into a CSV file for analysis.

📌 Features

Scrapes live cryptocurrency data (Name, Price, 24h Change, Market Cap).

Configurable limit (e.g., top 10 coins).

Runs in headless mode (no browser popup).

Saves results into CSV file with timestamps.

Prints tabular output directly in the terminal.

Robust with error handling for missing values.

🛠️ Tech Stack

Language: Python 3

Libraries: Selenium, Pandas, WebDriver Manager, Datetime, OS

Source: CoinMarketCap

⚙️ Installation

Clone this repository:

git clone https://github.com/yourusername/crypto-price-tracker.git
cd crypto-price-tracker


Install required dependencies:

pip install -r requirements.txt


Run the script:

python crypto_tracker.py

📂 File Structure
crypto-price-tracker/
│── crypto_tracker.py        # Main Python script
│── requirements.txt         # Required Python libraries
│── crypto_data.csv          # Output data file (auto-generated)
│── README.md                # Project documentation
