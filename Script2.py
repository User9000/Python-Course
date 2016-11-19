def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars

rate = input("What is the rate of the euros?")
quantity = input("How many do you like to exchange?")

dollar = currency_converter(float(rate),float(quantity))

print("This is the amount of dollars you need:", dollar)