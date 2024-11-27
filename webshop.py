
#oppgave 1
def print_ware_information(ware): #Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

#oppgave 2
def calculate_average_ware_rating(ware): #Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    rating_counter = 0
    total_rating = 0
    try: #legger til en try-except i tilfelle noe går galt som f.exe at den prøver å dele på 0,
        if 'ratings' in ware:
            for rating in ware['ratings']:
                rating_counter += 1
                total_rating += rating
            average_rating = total_rating / rating_counter
            return round(average_rating,1) #returnerer den gjennomsnittlige ratingen med en float verdi med en desimal for en gitt vare
    except ZeroDivisionError:
        print("There are no ratings available!")
        return 0

#oppgave 3
def get_all_wares_in_stock(all_wares): #Returnerer en dictionary med alle varer som er på lager.'''
    stock_wares = {} #lager en tom dictionary
    for ware_key, ware_value in all_wares.items():
        if ware_value["number_in_stock"] >0:
            stock_wares[ware_key] = ware_value

    return stock_wares #returnerer en dictionary med alle varer som er på lager

#oppgave 4
def is_number_of_ware_in_stock(ware, number_of_ware): #Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.'''
    if ware["number_in_stock"] >= number_of_ware and ware["number_in_stock"] >0: # sjekker om antall varer i lager for den spesifiserte varen om den er mer enn antallet som vil bli bestilt OG samtidig at den er mer enn 0, så det må være minst 1 på lager
        return True
    else:
        return False

#oppgave 5
def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware): #Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.'''
    stock = ware["number_in_stock"] #henter antall varer som er på lager
    if stock > 0: #sjekker hvis det det er noe i varehuset
        if number_of_ware > stock: #dersom antall bestilt varer er større enn det som er tilgjengelig i varehuset så skal den bare legge til det som er ledig, f.exe hvis 2 er bestilt men bare 1 er tilgjengelig så skal dem få 1
            print(f"Unfortunately your requested amount of {ware["name"]} is unavailable. Therefore only {stock} of {ware["name"]} will be added to your cart.")
            number_of_ware = stock #oppdaterer varehuset
        if ware_key in shopping_cart:
            shopping_cart[ware_key] += number_of_ware #legger til antall bestilte varer
        else:
            shopping_cart[ware_key] = number_of_ware #legger til varen

        ware["number_in_stock"] -= number_of_ware #oppdaterer varehuset
        print(f"The following has been added to your cart: {number_of_ware} of {ware["name"]}.")
    else:
        print(f"Unfortunately, the {ware["name"]} you requested is out of stock.")

    return shopping_cart

#oppgave 6
def calculate_shopping_cart_price(shopping_cart, all_wares, tax): #Returnerer prisen av en handlevogn basert på varene i den.'''
    total_price = 0 #holder på summen av handlevognen
    for ware_key, quantity in shopping_cart.items(): #iterer gjennom shopping_cart og antallet varer
        if ware_key in all_wares: #sjekker om varen finnes i all_wares, hvis ja, så skal den regne ut prisen for varen og legge til summen til total_price
            price_for_item = all_wares[ware_key]["price"]
            total_price += price_for_item * quantity
        else:
            print(f"The {ware_key} is not available!!") #dersom varen ikke finnes i all_wares så skal dette printes
    total_price_with_tax = total_price *(1+tax/100) #25% skatt #etter at alt av priser er samlet i total_price så skal skatt legges til
    return total_price_with_tax #returnerer prisen av en handlevogn basert på varene i den med skatt
