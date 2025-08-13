class Person:
    def __init__(self, navn:str, alder:int, idrett:str):
        self.navn = navn
        self.alder = alder
        self.idrett = idrett
 
class Utøver(Person):
    def __init__(self, betalingstatus:bool, divisjon:int, navn, alder, idrett):
        super().__init__(navn, alder, idrett)
        self.betalingstatus = betalingstatus
        self.divisjon = divisjon

    def vis_info(self):
        return(f"Navn: {self.navn}, alder, {self.alder}, divisjon: {self.divisjon}, idrett: {self.idrett}")

jobis = Utøver(True, 3, "Jobis", 43, "Fotball")
print(jobis.vis_info())