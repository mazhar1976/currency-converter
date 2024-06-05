import requests

def convert_currencies(amount):
    from_currency = input("Currency you want to convert from ").upper ()
    to_currency = input("Currency you want to conver to ").upper()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    response = requests.get(url)
    if response.status_code ==200:
        data = response.json()
        if to_currency in data ['rates']:
            exchange_rate = data["rates"][to_currency]
            converted_amount = amount * exchange_rate
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        else: 
            print(f"Exchange rate for {to_currency} not available ")
    else:
        print("Failed to fetch exchange rates")


amount = float (input("Enter the amount you want to convert "))

convert_currencies(amount)
