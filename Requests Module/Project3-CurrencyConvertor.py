# Currency Converter using ExchangeRate-API

import requests  # For making HTTP requests to the API

from API import API_KEY  # Import your API key from a separate file for security (if applicable)
API_KEY = 'My_API_KEY'  # Alternatively, hardcode here if needed (not recommended for real projects)

# Base URL to get the latest exchange rates for a specific currency
BaseUrl = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Function to convert currency from one to another
def ConvertCurrency(fromCurr, toCurr, amount):
    try:
        # Construct the API endpoint URL using the base currency
        url = BaseUrl + fromCurr.upper()
        response = requests.get(url)  # Send GET request to the API

        # Check for successful connection
        if response.status_code != 200:
            print("Failed to connect to the API!")
            return

        data = response.json()  # Parse the response to JSON

        # Check if the API response indicates success
        if data['result'] != 'success':
            print(f"Error from the API: {data.get('error-type', 'Unknown error')}")
            return

        # Retrieve the dictionary of conversion rates
        rates = data.get("conversion_rates", {})
        toCurr = toCurr.upper()  # Normalize target currency to uppercase

        # Check if the target currency is supported
        if toCurr not in rates:
            print(f"{toCurr} is not supported.")
            return

        rate = rates[toCurr]  # Fetch the exchange rate
        convertedAmount = round(amount * rate, 2)  # Perform the conversion and round to 2 decimal places

        # Display the result
        print(f"\n{amount} {fromCurr.upper()} = {convertedAmount} {toCurr.upper()}")

    except ValueError:
        # Handle invalid numeric input for amount
        print("Invalid amount entered, please enter a valid one.")
    except Exception as e:
        # Handle all other unexpected errors
        print(f"Error: {e}")

# Main function to take user input and perform the conversion
def main():
    print("Currency Converter")
    print("=" * 20)

    # Input for source and target currencies
    fromCurr = input("Enter the FROM currency (e.g. USD): ").strip()
    toCurr = input("Enter the TO currency (e.g. EUR): ").strip()

    try:
        # Input for the amount to convert
        amount = float(input("Enter the amount to convert: "))

        # Disallow negative amounts
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
    except ValueError:
        # Handle invalid amount input
        print("Invalid amount entered, please enter a valid one.")
        return

    # Ensure both currencies are provided
    if not fromCurr or not toCurr:
        print("Invalid currency entered, please enter a valid one.")
        return

    # Call the converter function
    ConvertCurrency(fromCurr, toCurr, amount)

# Run the main function
main()
