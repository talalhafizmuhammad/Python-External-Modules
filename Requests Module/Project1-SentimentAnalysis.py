"""
Sentiment Analysis Program using API Ninjas

What is Sentiment Analysis?
    Sentiment Analysis is a Natural Language Processing (NLP) technique used to determine
    whether a piece of text expresses a Positive, Negative, or Neutral sentiment.
    It is widely used in customer reviews, social media analysis, and chatbots.

In this script, we use the 'Sentiment API' provided by API Ninjas to perform sentiment analysis.

How to Get an API Key?
    1. Visit: https://api-ninjas.com
    2. Create a free account or log in.
    3. Go to the 'Sentiment API' section: https://api-ninjas.com/api/sentiment
    4. Copy your free API key from the dashboard.
    5. Paste it into the API_KEY variable below.
"""

import requests  # Used for sending HTTP requests to the API

# Replace this string with your actual API key obtained from API Ninjas
API_KEY = 'Your_API_KEY'

# The base URL endpoint for Sentiment Analysis API
URL = 'https://api.api-ninjas.com/v1/sentiment'


# Function to analyze sentiment using the API
def AnalyzeSentiments(text):
    """
    Sends text to the API and returns sentiment analysis result.

    Parameters:
    text (str): Input sentence or paragraph

    Returns:
    dict or None: A dictionary containing sentiment and confidence score, or None on error
    """
    # Reject empty input
    if not text.strip():
        print("❗ Input text cannot be empty.")
        return None

    try:
        # Send GET request to the API with proper headers and parameters
        response = requests.get(
            URL,
            headers={'X-API-Key': API_KEY},  # Required header for API access
            params={'text': text}  # Text to be analyzed
        )

        # Check if the response status is not OK (200)
        response.raise_for_status()

        # Return the JSON result as a Python dictionary
        return response.json()

    except requests.RequestException as e:
        # If an error occurs (e.g., network issue, invalid key), show the error
        print(f" Request failed for '{text}': {e}")
        return None


# Main interactive loop
print("=========== Sentiment Analyzer ===========")
print("Enter a sentence or paragraph to analyze.")
print("Type 'exit' to quit the program.\n")

while True:
    # Get user input
    userInput = input("Enter text: ").strip()

    # Check for exit condition
    if userInput.lower() == 'exit':
        print("Program exited. Thank you for using the analyzer!")
        break

    # Call the sentiment analysis function
    result = AnalyzeSentiments(userInput)

    # If result is valid, display it
    if result:
        print(f"\nSentiment Analysis for: \"{userInput}\"")
        print(f"Sentiment : {result.get('sentiment')}")
        print(f"Confidence: {result.get('confidence'):.2f}\n")


