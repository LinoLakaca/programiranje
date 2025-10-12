# Funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try:
        # Kod za otvaranje datoteke ide ovdje
        with open (filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena.")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji

# Funkcija za pročišćavanje teksta
def ocisti_tekst(tekst):
    # Kod za pročišćavanje teksta ide ovdje
    if tekst is None:
        return [] # Dodana provjera za None kako bi se spriječila greška u kasnijim funkcijama
        
    tekst = tekst.lower()
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci

def broji_rijeci(lista_rijeci):
    #rječnik u koji ćemo spremiti svaku riječ i koliko se puta ta riječ ponovila u tekstu
    brojac_rijeci = {} 
    for rijec in lista_rijeci:
        if rijec in brojac_rijeci:
            brojac_rijeci[rijec] += 1
        else:
            brojac_rijeci[rijec] = 1
    return brojac_rijeci


# ZADATAK 1: Definiranje liste "Stop Words"
STOP_WORDS = [
    'i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 
    'pa', 'te', 'li', 'da', 'kao', 'iz', 'sa', 'od', 'do', 
    'mi', 'ti', 'on', 'ona', 'ono', 'koji', 'koja', 'koje', 
    'što', 'gdje', 'kada', 'kako'
]

# ZADATAK 1: Uklanjanje "stop-words"
def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    """Vraća novi rječnik frekvencija bez riječi koje se nalaze u stop_words_lista."""
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik

# ZADATAK 2 + BONUS: Sortiranje i ispis rezultata
def sortiraj_i_ispisi(rjecnik_frekvencija, broj_rijeci=15):
    """
    Sortira rječnik po frekvenciji (od najveće prema najmanjoj)
    i ispisuje zadani broj najčešćih riječi.
    """
    print(f"\n--- Top {broj_rijeci} najčešćih riječi ---")

    # Pretvaramo rječnik u listu parova (riječ, frekvencija) i sortiramo
    sortirana_lista = sorted(
        rjecnik_frekvencija.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    # Uzimamo samo prvih N elemenata
    top_rijeci = sortirana_lista[:broj_rijeci]

    # Ispis s rednim brojem (i+1)
    for i, (rijec, frekvencija) in enumerate(top_rijeci):
        print(f"{i+1}. {rijec}: {frekvencija}")
    
    print("-" * 30)


if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    
    # Učitavanje
    ucitani_tekst = ucitaj_tekst(filepath)
    
    if ucitani_tekst:
        print("Učitani tekst je:\n", ucitani_tekst) 
        
        # Pročišćavanje
        lista_rijeci = ocisti_tekst(ucitani_tekst)
        
        # Brojanje frekvencija
        rjecnik_frekvencija = broji_rijeci(lista_rijeci) # Poziv VAŠE originalne funkcije
        print("Broj riječi u teksu (prije filtriranja): ")
        print(rjecnik_frekvencija)
        
        # 4. FILTRIRANJE (Zadatak 1)
        print("\n--- FAZA 3: FILTRIRANJE I SORTIRANJE ---")
        rjecnik_bez_stop_words = ukloni_stop_words(rjecnik_frekvencija, STOP_WORDS)
        print(f"Ukupan broj jedinstvenih riječi (nakon filtriranja): {len(rjecnik_bez_stop_words)}")

        # 5. SORTIRANJE I ISPIS (Zadatak 2 i Bonus)
        # Prvi poziv za Top 15 (Zadatak 2)
        sortiraj_i_ispisi(rjecnik_bez_stop_words, broj_rijeci=15) 

        # Bonus: Demonstracija s različitim brojem riječi
        sortiraj_i_ispisi(rjecnik_bez_stop_words, broj_rijeci=5) 
        sortiraj_i_ispisi(rjecnik_bez_stop_words, broj_rijeci=20) 

    else:
        print("Greška pri učitavanju datoteke. Program se zaustavlja.")