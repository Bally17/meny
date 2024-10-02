import csv

# Funkcia na nájdenie riadku s hodnotou "D,AVG,NAC,CZK" a ukladanie jednotlivých hodnôt do CSV súboru
def extract_and_save_czk_rates(tsv_file, output_file):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile, open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        csv_writer = csv.writer(csvfile)

        # Načítaj hlavičku (riadok s dátumami)
        header = next(tsv_reader)
        dates = header[1:]  # Dátumy sú od druhého stĺpca

        # Zápis hlavičky do výstupného CSV súboru
        csv_writer.writerow(['pair', 'effective_date', 'rate'])

        # Nájdeme riadok s presnou zhodou pre "D,AVG,NAC,CZK"
        for row in tsv_reader:
            if row[0] == 'D,AVG,NAC,CZK':  # Presná zhoda na základe prvého stĺpca
                print(f"Nájdený riadok: {row[0]}")
                # Prejdeme cez hodnoty a spárujeme ich s dátumami
                for i, rate in enumerate(row[1:]):
                    # Kontrola, aby sme nezapísali prázdne hodnoty alebo hodnotu ":"
                    if rate.strip() and rate.strip() != ':':  
                        date = dates[i]
                        # Zápis dát do CSV súboru vo formáte CZK/EUR, dátum, hodnota
                        csv_writer.writerow([f'CZK/EUR', date, rate])
                        print(f"Zapísaná hodnota: CZK/EUR, {date}, {rate}")
                break  # Po nájdení riadku skončíme prehľadávanie
            else:
                print(f"Preskočený riadok: {row[0]}")  # Pre informáciu, ktoré riadky preskakujeme

# Príklad použitia
tsv_file = 'estat_ert_bil_eur_d.tsv'  # Názov TSV súboru
output_file = 'czk_rates.csv'  # Názov CSV výstupného súboru
extract_and_save_czk_rates(tsv_file, output_file)
import csv

# Funkcia na nájdenie riadku s hodnotou "D,AVG,NAC,CZK" a ukladanie jednotlivých hodnôt do CSV súboru
def extract_and_save_czk_rates(tsv_file, output_file):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile, open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        csv_writer = csv.writer(csvfile)

        # Načítaj hlavičku (riadok s dátumami)
        header = next(tsv_reader)
        dates = header[1:]  # Dátumy sú od druhého stĺpca

        # Zápis hlavičky do výstupného CSV súboru
        csv_writer.writerow(['pair', 'effective_date', 'rate'])

        # Nájdeme riadok s presnou zhodou pre "D,AVG,NAC,CZK"
        for row in tsv_reader:
            if row[0] == 'D,AVG,NAC,CZK':  # Presná zhoda na základe prvého stĺpca
                print(f"Nájdený riadok: {row[0]}")
                # Prejdeme cez hodnoty a spárujeme ich s dátumami
                for i, rate in enumerate(row[1:]):
                    # Kontrola, aby sme nezapísali prázdne hodnoty alebo hodnotu ":"
                    if rate.strip() and rate.strip() != ':':  
                        date = dates[i]
                        # Zápis dát do CSV súboru vo formáte CZK/EUR, dátum, hodnota
                        csv_writer.writerow([f'CZK/EUR', date, rate])
                        print(f"Zapísaná hodnota: CZK/EUR, {date}, {rate}")
                break  # Po nájdení riadku skončíme prehľadávanie
            else:
                print(f"Preskočený riadok: {row[0]}")  # Pre informáciu, ktoré riadky preskakujeme

# Príklad použitia
tsv_file = 'estat_ert_bil_eur_d.tsv'  # Názov TSV súboru
output_file = 'czk_rates.csv'  # Názov CSV výstupného súboru
extract_and_save_czk_rates(tsv_file, output_file)
