import math_functions as mf 
# Aufgabenstellung:
# ○ Schreibe zunächst 4 Funktionen: add(x,y), subtract(x,y), mult(x,y) und
# div(x,y)
# ○ Jede dieser 4 Funktionen soll 2 Argumente annehmen: x und y, und die
# miteinander addieren, subtrahieren, multiplizieren oder dividieren
# ○ Dann schreibt eine Funktion calculator(), die:


# ■ Den User fragt, ob er addieren, subtrahieren, multiplizieren oder
# dividieren will
# ■ Den user nach 2 Zahlen fragt
# ■ Die entsprechende Funktion aufruft
# ■ Das Ergebnis auf der Konsole anzeigt
def calculator():
    # Erst User nach Operation fragen
    op = input("Operation? (+, -, *, /): ")

    # Zahlen abfragen:
    zahl1 = float(input("Gib mir deine erste Zahl: "))
    zahl2 = float(input("Gib mir deine zweite Zahl: "))

    # Fallunterscheidung: Welche Operation wollen wir durchführen?
    # printe das Ergebnis
    if op == "+":
        print(f"{zahl1} + {zahl2} = {mf.add(zahl1, zahl2)}")
    elif op == "-":
        print(f"{zahl1} - {zahl2} = {mf.sub(zahl1, zahl2)}")
    elif op == "*":
        print(f"{zahl1} * {zahl2} = {mf.mult(zahl1, zahl2)}")
    elif op == "/":
        print(f"{zahl1} / {zahl2} = {mf.div(zahl1, zahl2)}")
    else: 
        print("Bitte gültige Operation wählen!")
        # Falls die Operation ungültig war können wir von vorn anfangen:
        # (Achtung, Gefahr einer Endlosschleife!)
        calculator()

    

# Funktionsaufruf:
calculator()


