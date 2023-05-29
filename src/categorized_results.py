import requests
from pprint import pprint

payload = {
    "source": "universal",
    "url": "https://books.toscrape.com/catalogue/page-1.html",
    "parse": True,
    "parsing_instructions": {
        "products": {
            "_fns": [
                {
                    "_fn": "xpath",
                    "_args": [
                        "//ol//li"
                    ]
                }
            ],
            "_items": {
                "title": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//h3//a/text()"
                            ]
                        }
                    ]
                },
                "price": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//p[@class='price_color']/text()"
                            ]
                        }
                    ]
                },
                "availability": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                "normalize-space(.//p[contains(@class, 'availability')]/text()[last()])"
                            ]
                        }
                    ]
                },
                "url": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//a/@href"
                            ]
                        }
                    ]
                }
            }
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
