import csv, json

# Pfad zur JSON-Datei
json_file_path = 'response.json'

# Pfad zur CSV-Datei
csv_file_path = 'eval_data.csv'

# JSON-Daten laden
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Feldnamen für die CSV-Datei
fieldnames = json_data[0].keys()

# CSV-Datei zum Schreiben öffnen
with open(csv_file_path, 'w', newline='') as csv_file:
    # CSV-Writer-Objekt erstellen
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Feldnamen in die CSV-Datei schreiben
    writer.writeheader()
    
    # Daten aus dem JSON in die CSV-Datei schreiben
    for row in json_data:
        writer.writerow(row)

print("Conversion successful!")