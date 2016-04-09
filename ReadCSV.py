import csv

with open("C:\Projects\Yahoo.csv") as DataSourceFile:
    reader = csv.DictReader(DataSourceFile) # assume first row is header row that gives fieldname
    for row in reader:
        print(row['Open'], row['Close'])

        
