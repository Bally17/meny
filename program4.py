import schedule
import time
import requests
import csv
import os

# API key pre Alpha Vantage
API_KEY = 'EMOUY7PWDO84PXRC'
BASE_URL = 'https://www.alphavantage.co/query'

# Menové páry, ktoré chceme sledovať
CURRENCY_PAIRS = [
    ("INR", "EUR"),
    ("USD", "EUR"),
    ("CZK", "EUR"),
    ("GBP", "EUR")
]

# Kryptomeny, ktoré chceme sledovať
CRYPTO_PAIRS = [
    ("BTC", "EUR"),  # Bitcoin to EUR
    ("ETH", "EUR")   # Ethereum to EUR
]

# Názov CSV súboru
CSV_FILE = 'fx_crypto_rates.csv'

# Funkcia na získanie dát z Alpha Vantage API pre FX kurzy
def fetch_fx_rates(from_symbol, to_symbol):
    params = {
        'function': 'FX_DAILY',
        'from_symbol': from_symbol,
        'to_symbol': to_symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Overenie, či API vracia validné dáta
    if "Time Series FX (Daily)" in data:
        return data["Time Series FX (Daily)"]
    else:
        print(f"Error fetching data for {from_symbol}/{to_symbol}")
        return None

# Funkcia na získanie dát z Alpha Vantage API pre kryptomeny
def fetch_crypto_rates(symbol, market):
    params = {
        'function': 'DIGITAL_CURRENCY_DAILY',
        'symbol': symbol,
        'market': market,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Overenie, či API vracia validné dáta
    if "Time Series (Digital Currency Daily)" in data:
        return data["Time Series (Digital Currency Daily)"]
    else:
        print(f"Error fetching data for {symbol}/{market}")
        return None

# Funkcia na kontrolu existencie CSV súboru a vytvorenie hlavičky, ak súbor ešte neexistuje
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Vytvorenie hlavičky s požadovaným poradím stĺpcov
            writer.writerow(['from_symbol', 'to_symbol', 'date', 'close_rate'])

# Funkcia na kontrolu, či záznam už existuje v CSV
def record_exists(date, from_symbol, to_symbol):
    if not os.path.exists(CSV_FILE):
        return False
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == date and row[0] == from_symbol and row[1] == to_symbol:
                return True
    return False

# Funkcia na uloženie dát do CSV súboru
def save_to_csv(data, from_symbol, to_symbol):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        for date, rates in data.items():
            if not record_exists(date, from_symbol, to_symbol):
                # Ukladáme len stĺpce from_symbol, to_symbol, date a close_rate
                writer.writerow([
                    from_symbol,
                    to_symbol,
                    date,
                    float(rates['4a. close (USD)'] if '4a. close (USD)' in rates else rates['4. close'])
                ])

# Hlavná funkcia na sťahovanie FX kurzov a kryptomien a ich ukladanie
def fetch_and_store_fx_crypto_rates():
    initialize_csv()  # Inicializuje CSV, ak neexistuje
    
    # Sťahovanie FX kurzov
    for from_symbol, to_symbol in CURRENCY_PAIRS:
        print(f"Fetching rates for {from_symbol}/{to_symbol}...")
        data = fetch_fx_rates(from_symbol, to_symbol)
        if data:
            save_to_csv(data, from_symbol, to_symbol)
        print(f"Data for {from_symbol}/{to_symbol} saved to CSV.")
    
    # Sťahovanie kryptomenových kurzov
    for symbol, market in CRYPTO_PAIRS:
        print(f"Fetching rates for {symbol}/{market}...")
        data = fetch_crypto_rates(symbol, market)
        if data:
            save_to_csv(data, symbol, market)
        print(f"Data for {symbol}/{market} saved to CSV.")

# Funkcia na naplánovanie denného spúšťania
def schedule_daily_fetch():
    schedule.every().day.at("08:00").do(fetch_and_store_fx_crypto_rates)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Čaká 60 sekúnd pred ďalším kontrolovaním plánovaných úloh

# Spustenie programu
if __name__ == "__main__":
    fetch_and_store_fx_crypto_rates()
    # schedule_daily_fetch()
