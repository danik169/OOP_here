# Clasa Carte
class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titlu} de {self.autor}, ISBN: {self.isbn}"

# Clasa Bibliotecă
class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def elimina_carte(self, isbn):
        carte_gasita = None
        for carte in self.carti:
            if carte.isbn == isbn:
                carte_gasita = carte
                break
        if carte_gasita:
            self.carti.remove(carte_gasita)
            print(f"Cartea cu ISBN {isbn} a fost eliminată.")
        else:
            print(f"Cartea cu ISBN {isbn} nu a fost găsită.")

    def afiseaza_carti(self):
        if not self.carti:
            print("Biblioteca este goală.")
        else:
            print("Cărțile din bibliotecă:")
            for carte in self.carti:
                print(carte)

# Exemplu de utilizare a claselor Carte și Bibliotecă

# Creare instanțe de Carte
carte1 = Carte("Enigma Otiliei", "George Calinescu", "12345")
carte2 = Carte("Camasutra", "Vātsyāyana", "67890")

# Creare instanță de Bibliotecă
biblioteca = Biblioteca()

# Adăugare cărți în bibliotecă
biblioteca.adauga_carte(carte1)
biblioteca.adauga_carte(carte2)

# Afișare cărți
biblioteca.afiseaza_carti()

# Eliminare carte
biblioteca.elimina_carte("12345")

# Afișare cărți după eliminare
biblioteca.afiseaza_carti()
