class Publication:
    def __init__(self, name):
        self.name = name

    def Prints(self):
        print(f"julkaisun nimi on {self.name}")

class Magazine(Publication):
    def __init__(self, name, publisher):
        self.publisher = publisher
        super().__init__(name)

    def Prints(self):
        super().Prints()
        print(f"Lehden päätoimittaja on {self.publisher}")

class Book(Publication):
    def __init__(self, name, writer, pages):
        self.writer = writer
        self.pages = pages
        super().__init__(name)

    def Prints(self):
        super().Prints()
        print(f"kirjailija on {self.writer} ja kirjassa on {self.pages} sivua")


publication1 = Magazine("Aku Ankka", "Aki Hyyppä")
publication2 = Book("hytti n:o 6", "rosa Liksom", 200)

publication1.Prints()
publication2.Prints()