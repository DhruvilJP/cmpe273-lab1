import requests
import asyncio

url = 'https://webhook.site/668115b7-a6c0-49cd-bda2-25066934b072'
all_responses = []

async def get_response(number):
    response = requests.get(url)
    response_date = response.headers.get('Date')
    return('Request #' + str(number + 1) + ' Date: ' + response_date)

async def print_response(all_responses):
    for response in asyncio.as_completed(all_responses):
        print(await response)

def main():
    for index in range(0,3):
        all_responses.append(get_response(index))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_response(all_responses))
    loop.close()

if __name__ == '__main__':
    main()
