# Eine Funktion ohne Argumente:
def write_something():
    print("Dieser Text kommt aus einer Funktion!")

# Wir schreiben eine Funktion, die den User nach dem Alter fragt und dieses auf der
# Konsole ausgibt
def altersabfrage():
    alter = int(input("Gib dein Alter an: "))
    print(f"Du bist also {alter} Jahre alt")
    

# 1. Schreibe eine Funktion, die den Benutzer nach seinem Namen fragt und diesen
# auf der Konsole ausgibt.
def namensabfrage():
    name = input("Gib dein Namen an: ")
    print(f"Du bist also {name}.")


# 2. Schreibe eine Funktion, die den Benutzer nach seinem Namen fragt und diesen
# mit return zurückgibt.
def namensabfrage2():
    name = input("Gib deinen Namen an: ")
    return (f"Du bist also {name}.")

print(namensabfrage())
print(namensabfrage2())