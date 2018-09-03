import requests

url = 'https://webhook.site/c60a63dd-dfea-4ab3-a85f-d03aab147fd5'

def get_response(number):
    response = requests.get(url)
    response_date = response.headers.get('Date')
    return('Request #' + str(number + 1) + ' Date: ' + response_date)

def main():
    for index in range(0,3):
        print(get_response(index))

if __name__ == "__main__":
    main()
