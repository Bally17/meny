import csv

# Funkcia na nájdenie riadkov s konkrétnymi menovými pármi a ukladanie hodnôt do CSV súboru
def extract_and_save_rates(tsv_file, output_file, target_currencies):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile, open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        csv_writer = csv.writer(csvfile)

        # Načítaj hlavičku (riadok s dátumami)
        header = next(tsv_reader)
        dates = header[1:]  

        # Zápis hlavičky do výstupného CSV súboru
        csv_writer.writerow(['pair', 'effective_date', 'rate'])

        # Prehľadáme všetky riadky v TSV súbore
        for row in tsv_reader:
            # Skontrolujeme, či prvý stĺpec obsahuje jeden z cieľových menových párov
            if row[0] in target_currencies:
                print(f"Nájdený riadok: {row[0]}")
                if row[0] == 'D,AVG,NAC,USD':
                    pair = 'USD/EUR'
                elif row[0] == 'D,AVG,NAC,CZK':
                    pair = 'CZK/EUR'
                elif row[0] == 'D,AVG,NAC,GBP':
                    pair = 'GBP/EUR'
                elif row[0] == 'D,AVG,NAC,INR':
                    pair = 'INR/EUR'
                
                # Prejdeme cez hodnoty a spárujeme ich s dátumami
                for i, rate in enumerate(row[1:]):
                    # Kontrola, aby sme nezapísali prázdne hodnoty alebo hodnotu ":"
                    if rate.strip() and rate.strip() != ':':  
                        date = dates[i]
                        # Zápis dát do CSV súboru vo formáte pair, dátum, hodnota
                        csv_writer.writerow([pair, date, rate])
                        print(f"Zapísaná hodnota: {pair}, {date}, {rate}")

# Funkcia na extrakciu dát a uloženie do spoločného CSV súboru
def extract_date_and_close(input_file, output_file, currency_name):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'a', newline='', encoding='utf-8') as outfile:
        csv_reader = csv.DictReader(infile)  
        csv_writer = csv.writer(outfile)

        csv_writer.writerow(['Currency', 'Date', 'Close'])  # Hlavička pre výstupný súbor

        # Prejdeme všetky riadky v súbore
        for row in csv_reader:
            date = row['Date']  
            close = row['Close'] 
            
            # Zápis dát do výstupného CSV súboru s pridaním informácie o mene
            csv_writer.writerow([currency_name, date, close])
            print(f"Zapísaná hodnota: {currency_name}, {date}, {close}")

tsv_file = 'estat_ert_bil_eur_d.tsv'  
input_file_btc = 'BTC-EUR.csv'  
input_file_eth = 'ETH-EUR.csv'  

output_file = 'once_get_data.csv'  

target_currencies = ['D,AVG,NAC,USD','D,AVG,NAC,CZK', 'D,AVG,NAC,GBP', 'D,AVG,NAC,INR']  
extract_and_save_rates(tsv_file, output_file, target_currencies)

extract_date_and_close(input_file_btc, output_file, 'EUR/BTC')
extract_date_and_close(input_file_eth, output_file, 'EUR/ETH')
