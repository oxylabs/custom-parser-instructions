import requests
import json
from pprint import pprint

# Structure payload
payload = {
    "source": "universal_ecommerce",
    "url": "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=laptop&_sacat=0&LH_TitleDesc=0&_odkw=laptop&_osacat=0",
    "geo_location": "United States",
    "parse": True,
    "parsing_instructions": {
        "products": {
            "_fns": [
                {
                    "_fn": "xpath",
                    "_args": [
                        "//ul//li[@data-viewport]"
                    ]
                }
            ],
            "_items": {
                "title": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//span[@role='heading']/text()",
                                ".//span[@class='BOLD']/text()"
                            ]
                        }
                    ]
                },
                "price": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//span[@class='s-item__price']/text()"
                            ]
                        }
                    ]
                },
                "condition": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//span[@class='SECONDARY_INFO']/text()"
                            ]
                        }
                    ]
                },
                "seller": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [
                                ".//span[@class='s-item__seller-info-text']/text()"
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

# Get a response
response = requests.request(
    "POST",
    "https://realtime.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),
    json=payload
)

# Write the JSON response to a JSON file
with open("ebay_product_listings.json", "w") as f:
    json.dump(response.json(), f)

# Instead of a response with job status and results URL, this will return
# the JSON response with the result
pprint(response.json())
