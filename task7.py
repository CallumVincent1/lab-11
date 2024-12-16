class Country:
    def __init__(self, capital_name, language_spoken):
        self.capital = capital_name
        self.language = language_spoken

    def display_capital(self):
        print(f"the capital is {self.capital}")

    def display_language(self):
        print(f"the spoken language is {self.language}")


class UK(Country):
    def __init__(self, capital_name, language_spoken):
        super().__init__(capital_name, language_spoken)

    def display_capital(self):
        print("the capital of the UK is London")

    def display_language(self):
        print("Many different languages are spoken but the main language is English")

class Italy(Country):
    def __init__(self, capital_name, language_spoken):
        super().__init__(capital_name, language_spoken)

    def display_capital(self):
        print("the capital of Italy is Rome")

    def display_language(self):
        print("The main language in Italy is Italian")

class Qatar(Country):
    def __init__(self, capital_name, language_spoken):
        super().__init__(capital_name, language_spoken)

    def display_capital(self):
        print("the capital of Qatar is Doha")

    def display_language(self):
        print("The main language of Qatar is Arabic")