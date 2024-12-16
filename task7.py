class Country:
    def __init__(self, capital_name, language_spoken):
        self.capital = capital_name
        self.language = language_spoken

    def display_capital(self):
        print(f"the capital is {self.capital}")

    def display_language(self):
        print(f"the spoken language is {self.language}")