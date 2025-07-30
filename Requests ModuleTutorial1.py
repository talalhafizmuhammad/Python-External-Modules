#External modules: Imported from outside of the python version

#Request module: making HTTP/HTTPS requests, to interact with web servers, APIs (Application Programming Interface)
#and websites

import requests

#basic request syntax

response = requests.get("https://api.github.com")
print(response)

#Status code: Informs us the status of the requested url
#200 --> 200 ok means successfully approached
#404 --> 404 not found means not available at all

#checking the status code
print(response.status_code)

#ERROR HANDLING

# We will run .raise_for_status() --> Raise an HTTP/HTTPS error (HTTPError) between status codes 400-600


from requests.exceptions import HTTPError

URLs = ['https://api.github.com', 'https://api.github.com/invalid']

for i in URLs:
    try:
        response = requests.get(i)
        response.raise_for_status()
    except HTTPError as httpError:
        print(f"HTTP Error occured: {httpError}")
    except Exception as error:
        print(f"Other error occured: {error}")
    else:
        print("Successful")

# Accessing the Response Content
# .content  → Raw bytes
# .json()   → Parsed JSON as a dictionary

response = requests.get('https://api.github.com')
print(type(response.content))  #gives the data in form of raw bytes <class 'bytes'>
print(response.content) #gives the data in JSON format
print(type(response.json())) #Dictionary


#Parse and exclude specified data from the JSON dictionary
respDict = response.json()
print(respDict['emojis_url'])
