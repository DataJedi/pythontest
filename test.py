# Sommige exceptions hebben argumenten, en sommige niet
# KeyboardInterrupt niet
# FileNotFoundError wel
def main():
    try:
        fil = openFile("bestand")
    except FileNotFoundError as fnfe:
        print(fnfe.args[0])

def openFile(naam):
    if naam == "bestand":
        raise FileNotFoundError("Bestand mist")
    fil = open(naam)
    
main()
