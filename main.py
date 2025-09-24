#Funkcija za učitavanje teksta iz datoteke 
 def ucitaj_tekst(filepath):
    try:
        # KOd za otvaranje datoteke ide ovdje
        with open (filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji
      
      # Funkcija za proišćavanje teksta 
        def ocisti_tekst(tekst):
            #Kod za pročišćavanje teksta ide ovdje
            tekst = tekst.lower()

        
        
        
        if __name__=="__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
    else:
        print("Greška pri učitavanju datoteke.")
    ucitani_tekst = ocisti_tekst(ucitani_tekst)
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri očišćavanju tekst.")