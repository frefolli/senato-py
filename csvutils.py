import csv

def naive_cast(string):
    try:
        return int(string)
    except:
        try:
            return float(string)
        except:
            return string

def read_senato(filepath: str = "senato.csv"):
    with open(filepath) as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        return list([naive_cast(_) for _ in row] for row in reader)[1:]