import csv

# Funkcia na extrakciu dát a uloženie do spoločného CSV súboru
def extract_date_and_close(input_file, output_file, currency_name):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'a', newline='', encoding='utf-8') as outfile:
        csv_reader = csv.DictReader(infile)  # Čítanie CSV súboru ako slovník
        csv_writer = csv.writer(outfile)

        # Prejdeme všetky riadky v súbore
        for row in csv_reader:
            date = row['Date']  # Extrahujeme dátum z prvého stĺpca
            close = row['Close']  # Extrahujeme uzatváraciu cenu zo stĺpca "Close"
            
            # Zápis dát do výstupného CSV súboru s pridaním informácie o mene
            csv_writer.writerow([currency_name, date, close])
            print(f"Zapísaná hodnota: {currency_name}, {date}, {close}")

# Hlavný program
output_file = 'combined_btc_eth.csv'  # Výstupný CSV súbor

# Zapíš hlavičku len raz
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(['Currency', 'Date', 'Close'])  # Hlavička pre výstupný súbor

# Spracovanie BTC-EUR.csv
input_file_btc = 'BTC-EUR.csv'  # Pôvodný súbor pre BTC
extract_date_and_close(input_file_btc, output_file, 'EUR/BTC')

# Spracovanie ETH-EUR.csv
input_file_eth = 'ETH-EUR.csv'  # Pôvodný súbor pre ETH
extract_date_and_close(input_file_eth, output_file, 'EUR/ETH')
