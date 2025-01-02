def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

def ist_gerade2(zahl):
    return zahl % 2 == 0



name = "Lukas"
alter = 28
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")


print(f"Die Zahl 42 ist gerade: {ist_gerade(42)}")