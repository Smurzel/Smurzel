class Currency:
    def __init__(self, name, code, rate_to_currency):
        self.name = name
        self.code = code
        self.rate_to_currency = rate_to_currency
    def to_uah(self, amount):
        return amount * self.rate_to_currency
    def from_uah(self, amount_currency):
        return amount_currency / self.rate_to_currency
class UAH(Currency):
    def __init__(self):
        super().__init__("Гривня", "UAH", 1.0)
class USD(Currency):
    def __init__(self):
        super().__init__("Долар США", "USD", 41.5)
class EUR(Currency):
    def __init__(self):
        super().__init__("Євро", "EUR", 43.68)
class PLN(Currency):
    def __init__(self):
        super().__init__("Злотий", "PLN", 10.14)
class Converter:
    def __init__(self):
        self.currencies = {
            "UAH": UAH(),
            "USD": USD(),
            "EUR": EUR(),
            "PLN": PLN(),
        }
    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.currencies or to_currency not in self.currencies:
            raise ValueError("Валюта недоступна або її не існує.")
        from_currency = self.currencies[from_currency]
        to_currency = self.currencies[to_currency]
        amount = from_currency.to_uah(amount)
        return to_currency.from_uah(amount)
class UserInterface:
    def __init__(self, converter):
        self.converter = converter
    def user_input_currency(self, currency):
        currency = input(currency)
        if currency in self.converter.currencies:
            return currency
        else:
            print("Невідома валюта. Спробуйте ще раз.")
    def user_input_amount(self, currency_type):
        try:
            amount = float(input(f"Введіть суму в {currency_type}: "))
            return amount
        except ValueError:
            print("Будь ласка, введіть числове значення.")
    def display_result(self, result, currency_type):
        print(f"Результат: {result:.2f} {currency_type}")
    def run(self):
        print("Підтримувані валюти: UAH, USD, EUR, PLN")
        from_currency = self.user_input_currency("Введіть код валюти, з якої конвертувати: ")
        if not from_currency:
            return
        to_currency = self.user_input_currency("Введіть код валюти, в яку конвертувати: ")
        if not to_currency:
            return
        amount = self.user_input_amount(from_currency)
        if amount != 0:
            result = self.converter.convert(amount, from_currency, to_currency)
            self.display_result(result, to_currency)

if __name__ == "__main__":
    converter = Converter()
    ui = UserInterface(converter)
    ui.run()