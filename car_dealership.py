from datetime import date
car_register = {
"toyotaBZ4X": {
"brand": "Toyota",
"model": "Corolla",
"price": 96_000,
"year": 2012,
"month": 8,
"new": False,
"km": 163_000
},
"pugeot408": {
"brand": "Pugeot",
"model": "408",
"price": 330_000,
"year": 2019,
"month": 1,
"new": False,
"km": 40_000
},
"audiRS3": {
"brand": "Audi",
"model": "RS3",
"price": 473_000,
"year": 2022,
"month": 2,
"new": True,
"km": 0
},
}
NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000

# Oppgave 1
def print_car_information(car):
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price: {car['price']},-")
    print(f"Manufactured: {car['year']}-{car['month']}")
    if car["new"] == True:  # sjekker om bilen er ny
        print("Condition: New")
    else:
        print("Condition: Used")
    print(f"km: {car['km']}")

# Oppgave 2
def create_car(car_register, brand, model, price, year, month, new, km):
    new_car = {
            "brand": brand,
            "model": model,
            "price": price,
            "year": year,
            "month": month,
            "new": new,
            "km": km
        }
    car_register.update(new_car)
    return

# Oppgave 3
def get_car_age(car):
    this_year = date.today().year #henter årets år
    car_age = this_year - car["year"] #så trekker vi fra årets årstall fra bilens alder
    return car_age #returnerer bilens alder

# Oppgave 4
def next_eu_control(car):
    year = car["year"] #henter både år og bilens måend som den ble produsert
    month = car["month"]
    next_eu_control_year = year + 2  #legger till 2 år på bilens år for å finne ut når neste eu kontrol blir da sidne det skal skje fra året og måneden bilen ble produsert
    next_eu_control_date = date(next_eu_control_year, month, 1) #setter sånn at neste eu kontorlll skjer på 1.måned
    return next_eu_control_date #returnerer neste eu kontrol dato

# Oppgave 5
def rent_car_monthly_price(car):
    yearly_price = car["price"] * 0.4 #regner ut årets pris som er 40 % av bilens totale pris
    if car["new"]:
        monthly_price = (yearly_price / 12 )+1000 #1000kr mer per måned for nye biler
    else: #ellers ingen tilleg for brukte biler
        monthly_price = yearly_price / 12
    return round(monthly_price, 2) #2 desimlaer avrundet

# Oppgave 6
cars_fee_table = {
    (0,3): 6681,
    (4,11): 4034,
    (12,29): 1729,
    (30, 100): 0
}

def calculate_total_price(car):
    car_price = car["price"] #henter bilens pris
    if car["new"]:
        total_price = car_price + 10783 #legger til avgift for nye biler her
    else:
        car_age = get_car_age(car)
        for car_age_based, fee in cars_fee_table.items(): #regner ut avgiften her baser på bilens alder
            if car_age_based[0] <= car_age <= car_age_based[1]:
                total_price = car_price + fee #legger til avigften for brukte biler basert på alderen sin
    return total_price

# Oppgave 7
class Car: #lager en klasse som skal kunne holde på informasjon om en bil
    def __init__(self, brand, model, price, year, month, new, km): #bilens oppskrift
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def next_eu_control(self): #tenker at denne passer bra her ettersom at den er en del av bilens alder i klassen
        next_eu_control_year = self.year + 2
        return date(next_eu_control_year, self.month, 1)

    def get_car_age(self): #denne er også bra ettersom at henter bilens alder som er veldig nyttig for klassen som er en oppskrift av en bil
        this_year = date.today().year
        return this_year - self.year

    def rent_car_monthly_price(self): #veldig nyttig ettersom at bilens månedlige leie pris er avhengig av bilen og dens oppskrift
        yearly_price = self.price *0.4
        if self.new:
            return round((yearly_price/12)+1000,2)
        else:
            return round(yearly_price/12,2)

    def calculate_total_price(self): #fordi den regner ut totalprisen for bilen og denne er relevant for bil klassen
        if self.new:
            return self.price + 10783
        else:
            car_age = self.get_car_age()
            if 0 <= car_age <= 3:
                return self.price+6681
            elif 4<= car_age <= 11:
                return self.price+4034
            elif 12<=car_age<=29:
                return self.price+1729
            else: #alt annet som er gammel som 30 og oppover
                return self.price

def is_new(car):
    if __name__ == '__main__':
        create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
        toyota = car_register['toyotaBZ4X']
        print_car_information(toyota)
        print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
        print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
        print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")
        audi = car_register['audiRS3']
        print_car_information(audi)
        print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
        print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
        print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")

cars = is_new(car_register)
print(cars)