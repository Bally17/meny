import csv

# Funkcia na nájdenie riadkov s konkrétnymi menovými pármi a ukladanie hodnôt do CSV súboru
def extract_and_save_rates(tsv_file, output_file, target_currencies):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile, open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        csv_writer = csv.writer(csvfile)

        # Načítaj hlavičku (riadok s dátumami)
        header = next(tsv_reader)
        dates = header[1:]  # Dátumy sú od druhého stĺpca

        # Zápis hlavičky do výstupného CSV súboru
        csv_writer.writerow(['pair', 'effective_date', 'rate'])

        # Prehľadáme všetky riadky v TSV súbore
        for row in tsv_reader:
            # Skontrolujeme, či prvý stĺpec obsahuje jeden z cieľových menových párov
            if row[0] in target_currencies:
                print(f"Nájdený riadok: {row[0]}")
                # D,AVG,NAC,INR
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

# Príklad použitia
tsv_file = 'estat_ert_bil_eur_d.tsv'  # Názov TSV súboru
output_file = 'inr_usd_czk_gbp_rates.csv'  # Názov CSV výstupného súboru
target_currencies = ['D,AVG,NAC,USD','D,AVG,NAC,CZK', 'D,AVG,NAC,GBP', 'D,AVG,NAC,INR']  # Menové páry, ktoré chceme spracovať
extract_and_save_rates(tsv_file, output_file, target_currencies)
