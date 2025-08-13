class Dyr:
    def __init__(self, navn: str, art: str, alder: int, energi: int = 100):
        self._navn = navn  # Bruker _ for å indikere at den er "protected"
        self._art = art
        self._alder = alder
        self._energi = energi # Nytt attributt for matkjeder

    # Getter-metoder for å aksessere attributter
    def get_navn(self) -> str:
        return self._navn

    def get_art(self) -> str:
        return self._art

    def get_alder(self) -> int:
        return self._alder

    def get_energi(self) -> int:
        return self._energi

    # Setter-metode for energi, med validering (eksempel på innkapsling)
    def sett_energi(self, ny_energi: int):
        if ny_energi < 0:
            self._energi = 0
            print(f"{self._navn} har ingen energi igjen og dør.")
            # Her kunne vi kalt en 'dø'-metode
        elif ny_energi > 200: # Kan ha en maksgrense for energi
            self._energi = 200
        else:
            self._energi = ny_energi

    def spis(self, mat_energi: int):
        self.sett_energi(self._energi + mat_energi)
        print(f"{self._navn} spiser og har nå {self._energi} energi.")

    def sov(self):
        print(f"{self._navn} sover.")
        self.sett_energi(self._energi + 10) # Får litt energi av å sove

    def lag_lyd(self):
        # Dette er en generell lyd, vil bli overstyrt av underklasser
        print(f"{self._navn} lager en generell dyrelyd.")

    def metaboliser_energi(self, mengde: int = 5):
        """Simulerer energiforbruk over tid."""
        self.sett_energi(self._energi - mengde)
        if self._energi == 0:
            print(f"{self._navn} døde av mangel på energi.")
            return True # Indikerer at dyret døde
        return False # Indikerer at dyret fortsatt lever

    def __str__(self):
        return f"{self._navn} ({self._art}, {self._alder} år, Energi: {self._energi})"

# Eksempel på bruk:
dyr1 = Dyr("Fant", "Hund", 5)
print(dyr1)
dyr1.spis(30)
dyr1.lag_lyd()

class Pattedyr(Dyr):
    def __init__(self, navn: str, art: str, alder: int, pelsfarge: str, energi: int = 100):
        super().__init__(navn, art, alder, energi) # Kaller foreldreklassens konstruktør
        self._pelsfarge = pelsfarge

    def gi_melk(self):
        print(f"{self._navn} gir melk.")

    def lag_lyd(self):
        print(f"{self._navn} brøler!") # Overstyrer lag_lyd for pattedyr

class Fugl(Dyr):
    def __init__(self, navn: str, art: str, alder: int, vingespenn: float, energi: int = 100):
        super().__init__(navn, art, alder, energi)
        self._vingespenn = vingespenn

    def fly(self):
        print(f"{self._navn} flyr med et vingespenn på {self._vingespenn} meter.")

    def lag_lyd(self):
        print(f"{self._navn} kvitrer!") # Overstyrer lag_lyd for fugler

# Spesifikke arter som arver fra Pattedyr eller Fugl
class Løve(Pattedyr):
    def __init__(self, navn: str, alder: int, pelsfarge: str = "gulbrun", energi: int = 120):
        super().__init__(navn, "Løve", alder, pelsfarge, energi)

    def jakt(self, byttedyr: Dyr):
        if self._energi >= 30: # Krever energi for å jakte
            if byttedyr.get_art() in ["Kanin", "Geit"]: # Enkel diett-sjekk
                print(f"{self._navn} jakter på {byttedyr.get_navn()}.")
                if byttedyr.metaboliser_energi(50): # Byttedyr mister mye energi
                    print(f"{self._navn} fanget og spiste {byttedyr.get_navn()}.")
                    self.spis(byttedyr.get_energi() + 20) # Får energi fra byttedyr
                    return True
                else:
                    print(f"{byttedyr.get_navn()} slapp unna!")
                    self.sett_energi(self._energi - 10) # Mister litt energi
            else:
                print(f"{self._navn} jakter ikke på {byttedyr.get_navn()}.")
        else:
            print(f"{self._navn} er for trøtt til å jakte.")
        return False

    def lag_lyd(self):
        print(f"{self._navn} brøler mektig!") # Spesifikk lyd for løve

class Kanin(Pattedyr):
    def __init__(self, navn: str, alder: int, pelsfarge: str = "hvit", energi: int = 80):
        super().__init__(navn, "Kanin", alder, pelsfarge, energi)

    def beite(self, plante_energi: int = 15):
        self.spis(plante_energi)
        print(f"{self._navn} beiter på gress.")

    def lag_lyd(self):
        print(f"{self._navn} piper.")

class Ørn(Fugl):
    def __init__(self, navn: str, alder: int, vingespenn: float = 2.0, energi: int = 110):
        super().__init__(navn, "Ørn", alder, vingespenn, energi)

    def jakt(self, byttedyr: Dyr):
        if self._energi >= 25:
            if byttedyr.get_art() in ["Kanin"]: # Ørn spiser kanin
                print(f"{self._navn} stuper ned mot {byttedyr.get_navn()}.")
                if byttedyr.metaboliser_energi(40):
                    print(f"{self._navn} fanget og spiste {byttedyr.get_navn()}.")
                    self.spis(byttedyr.get_energi() + 15)
                    return True
                else:
                    print(f"{byttedyr.get_navn()} gjemte seg!")
                    self.sett_energi(self._energi - 5)
            else:
                print(f"{self._navn} jakter ikke på {byttedyr.get_navn()}.")
        else:
            print(f"{self._navn} er for sliten til å jakte.")
        return False

    def lag_lyd(self):
        print(f"{self._navn} skriker høyt!")

# Eksempel på bruk:
løve1 = Løve("Simba", 3, "gylden")
kanin1 = Kanin("Hoppsan", 1, "brun")
ørn1 = Ørn("Skygger", 7)

print(løve1)
print(kanin1)
print(ørn1)

løve1.lag_lyd()
kanin1.lag_lyd()
ørn1.lag_lyd()

løve1.jakt(kanin1) # Løven jakter på kaninen
print(kanin1) # Sjekk kaninens status etter jakt