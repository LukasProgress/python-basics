class Buch():
    # Konstruktor belegt Eigenschaften Titel und Author
    def __init__(self, titel, author):
        self.titel = titel
        self.author = author
    
    def text(self):
        print(f"Dieses Buch heißt {self.titel} und ist geschrieben von {self.author}")

    

dracula = Buch("Count Dracula", "Bram Stoker")
#print(dracula.titel)
#print(dracula.author)

frankenstein = Buch("Frankenstein", "Mary Shelly")
#print(frankenstein.titel)
frankenstein.titel = "Frankensteins Monster"
#print(frankenstein.titel)

dracula.text()
frankenstein.text()