from datetime import datetime
# Python wird Zeile für Zeile interpretiert
print("Erster Befehl")
print("Zweiter Befehl")

# Wir können Werte an Namen binden (Variablen):
mein_name = "Lukas"

# Wir können Variablen überall im Code nutzen:
print(mein_name)

# Wir können mit variablen Berechnungen durchführen: 
print(mein_name + " Probst")

# Wir können aber auch den Wert von Variablen verändern:
mein_name = "Tom Schiffmann"
print(mein_name)

# Wenn wir Zahlen in die Variablen schreiben, können wir damit rechnen:
print(2 + 3)
zahl = 7
print(2 + zahl)
print(8 - zahl)
print(zahl * zahl)
print(zahl / 3)
print(zahl % 3)

# Modulo 
# -----------------------------------
# Modulo als Operator, kann dafür genutzt werden Teilbarkeit zu bestimmen: 
print(zahl % 2 == 0) # True, wenn zahl durch 2 teilbar ist
# Wir können Modulo aber auch benutzen, um den Wert unserer Variablen zu beschränken

# Bspw 60 Minuten pro stunde
minuten = 0
# 150 Minuten vergehen
minuten = (minuten + 150) % 60
print(minuten)
# -----------------------------------

# Funktionen
#------------------------------------
# Wir können Funktionen definieren um Blöcke von Code an einen Namen zu binden
# Funktionsdefinition (Die Funktion erhält 2 Argumente und gibt deren Summe zurück)
def add(zahl1, zahl2):
    return zahl1 + zahl2

print(add(4,1)) # Funktionsaufruf

# Fallunterscheidungen: 
# Mit if-elif-else können wir Fallunterscheidungen machen:

# Listen:
meine_liste = [1,2,3,4,5]

if 6 in meine_liste:    # Wenn 
    print("Die 6 ist drin!")
elif 5 in meine_liste:  # Sonst wenn
    print(f"In der {len(meine_liste)}-Elementigen Liste ist die 5 enthalten")
else:                   # Sonst
    print("War wohl nix")


# Imports
#-----------------
# Wir können Dateien und Module/Pakete importieren, die bestimme Aufgaben erfüllen (Siehe erste Zeile(n))

# Datetime gibt uns Zeitfunktionen:
print(datetime.now())

# Andere Pakete: 
# - random
# - math
# - os (operating system -> Dateizugriffe auf dem Rechner)
# - pyplot
# - turtle (wenn ihr in den Ferien rumexperimentieren wollt -> Probiert turtle)
# - ... Viele weitere
