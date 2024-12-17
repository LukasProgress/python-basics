def addiere_zahlen():
    zahl1 = input("Gib die erste Zahl ein: ")

    if not zahl1.isdigit():
        return "Keine gültige Zahl!"
        
    zahl2 = input("Gib die zweite Zahl ein: ")

    # Überprüfung: Sind zahl1 und zahl2 NUR ziffern?
    if zahl2.isdigit():
        return int(zahl1) + int(zahl2)
    else:
        return "Keine gültigen Zahlen!"
        

    

print(addiere_zahlen())