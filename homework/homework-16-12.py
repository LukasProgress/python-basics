date = input("Geben Sie ein Datum ein (yyyy.mm.dd): ")

# "Wenn"
if date >= "2024.12.24" and date <= "2025.01.01":
    print("Es sind Winterferien!")

# "elif = Ansonsten, wenn"
elif date >= "2025.04.18" and date <= "2025.04.21":
    print("Es sind Osterferien!")

# "Ansonsten"
else:
    print("Du muss arbeiten 😔")