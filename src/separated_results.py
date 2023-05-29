import requests
from pprint import pprint

payload = {
    "source": "universal",
    "url": "https://books.toscrape.com/catalogue/page-1.html",
    "parse": True,
    "parsing_instructions": {
        "titles": {
            "_fns": [
                {
                    "_fn": "xpath",
                    "_args": ["//h3//a/text()"]
                }
            ]
        },
        "prices": {
            "_fns": [
                {
                    "_fn": "xpath",
                    "_args": ["//p[@class='price_color']/text()"]
                }
            ]
        }
    }
}

response = requests.request(
    "POST",
    "https://realtime.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),
    json=payload
)

pprint(response.json())
