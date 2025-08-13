class Bok:
    def __init__(self, tittel: str, forfatter: str, utgivelsesaar: int):
        self._tittel = tittel  # Konvensjon: intern tittel
        self.forfatter = forfatter # Offentlig: kan aksesseres direkte
        self.__utgivelsesaar = utgivelsesaar # Navnemanglet: ment som "svært privat"

    def get_tittel(self) -> str:
        """En getter for å få tilgang til tittel på en kontrollert måte."""
        print("Aksesserer tittel via getter.")
        return self._tittel

    def set_tittel(self, ny_tittel: str):
        """En setter for å endre tittel med potensiell validering."""
        if len(ny_tittel) > 0:
            self._tittel = ny_tittel
            print(f"Tittel endret til: {self._tittel}")
        else:
            print("Tittel kan ikke være tom.")

    def get_utgivelsesaar(self) -> int:
        """En getter for den navnemanglede variabelen."""
        print("Aksesserer utgivelsesår via getter.")
        return self.__utgivelsesaar

    def _intern_metode(self):
        """En intern metode (konvensjonelt)."""
        print(f"Dette er en intern metode, forfatter er: {self.forfatter}")

    def __vis_hemmelig_info(self):
        """En navnemanglet metode (svært intern)."""
        print(f"Navnemanglet metode: Utgivelsesår: {self.__utgivelsesaar}")

    def vis_all_info(self):
        """En offentlig metode som bruker alle interne variabler."""
        print(f"\nInfo om bok:")
        print(f"Tittel: {self._tittel}")
        print(f"Forfatter: {self.forfatter}")
        print(f"Utgivelsesår: {self.__utgivelsesaar}")
        self._intern_metode()
        self.__vis_hemmelig_info() # Kan kalles internt i klassen

# Opprett et Bok-objekt
min_bok = Bok("Python for Dummies", "John Doe", 2023)

# Aksessering av variabler:

# 1. Offentlig variabel (ingen understrek)
print(f"\nForfatter (direkte aksess): {min_bok.forfatter}")
min_bok.forfatter = "Jane Smith" # Kan endres direkte
print(f"Forfatter (etter endring): {min_bok.forfatter}")

# 2. Enkel understrek (_tittel) - Konvensjonelt "Protected"
print(f"\nTittel (via getter): {min_bok.get_tittel()}")
min_bok.set_tittel("Effective Python") # Endre via setter (anbefalt)

# Direkte aksess er MULIG, men frarådet!
print(f"Tittel (direkte aksess - frarådet): {min_bok._tittel}")
min_bok._tittel = "Advanced Python Tricks" # Du KAN endre den direkte, men IKKE GJOR DET!
print(f"Tittel (etter direkte endring): {min_bok._tittel}")


# 3. Dobbel understrek (__utgivelsesaar) - Navnemanglet "Private"
print(f"\nUtgivelsesår (via getter): {min_bok.get_utgivelsesaar()}")

# Direkte aksess med opprinnelig navn vil feile:
try:
    print(min_bok.__utgivelsesaar)
except AttributeError as e:
    print(f"Feil ved direkte aksess av __utgivelsesaar: {e}")

# Aksess via det "manglede" navnet er MULIG, men frarådet og svært uvanlig:
print(f"Utgivelsesår (via manglet navn - frarådet): {min_bok._Bok__utgivelsesaar}")
min_bok._Bok__utgivelsesaar = 2025 # Du KAN endre den, men IKKE GJOR DET!
print(f"Utgivelsesår (etter manglet navn endring): {min_bok._Bok__utgivelsesaar}")


# Kalle metoder:
min_bok._intern_metode() # Kan kalles (konvensjonelt intern)

# Direkte kall til navnemanglet metode vil feile:
try:
    min_bok.__vis_hemmelig_info()
except AttributeError as e:
    print(f"Feil ved direkte kall av __vis_hemmelig_info: {e}")

# Kalle den offentlige metoden som bruker de interne
min_bok.vis_all_info()