api = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=2"

# Write a function that performs a HTTP GET request to this API.

# The response to a request is a JSON with the following 5 fields:
# * page: The current page of the results
# * per_page: The maximum number of transaction records returned per page.
# * total: The total number of transaction records available on all pages of the result.
# * total_pages: The total number of pages with results.
# * data: An array of objects containing transaction records on the requested page


import requests

def get_response(api):
    try:
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()["data"]
            for txn in data:
                print(txn["ip"])
        else:
            raise Exception("failed request")
    except Exception as e:
        print(e)

print(get_response(api))