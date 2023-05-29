import requests
import json
from pprint import pprint

# Structure payload.
payload = {
    "source": "universal",
    "url": "https://www.ebay.com/itm/256082552198?hash=item3b9fb5a586:g:G20AAOSwm-9iUMjU&amdata=enc%3AAQAIAAAAsBVaJyw82KdZRRfIJpMYmmLIWty94MR%2FJXCYNOmilLafKM7iGdkVbac4c1CdxnzkJ9MhvAWumbBGriDQ%2BuRO5YtuapAckUKSwGnOjG3ITS4oP%2Bak%2FRPV%2B2mEba5veCK%2FpN2YYLn3rOyUjOoroU9Z1%2FBJ2xsih1S57d5U1yh%2B2o9m2L3lZFEe7flmjSKUbaVC%2BYPaSzZTYq%2BlNzVnk7sAniEurfuTzhiLHt58xBceAxUm%7Ctkp%3ABlBMUMSCmrWIYg",
    "geo_location": "United States",
    "parse": True,
    "parsing_instructions": {
        "title": {
            "_fns": [
                {
                    "_fn": "xpath_one",
                    "_args": ["//h1//span[@class='ux-textspans ux-textspans--BOLD']/text()"]
                }
            ]
        },
        "price": {
            "_fns": [
                {
                    "_fn": "xpath_one",
                    "_args": ["//div[@class='x-price-primary'][@data-testid='x-price-primary']//span[@class='ux-textspans']/text()"]
                },
                {
                    "_fn": "amount_from_string"
                }
            ]
        },
        "item_specifics": {
            "_fns": [
                {
                    "_fn": "xpath",
                    "_args": ["//div[@class='ux-layout-section-evo__col']"]
                }
            ],
            "_items": {
                "key": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [".//span[@class='ux-textspans']/text()"]
                        }
                    ]
                },
                "value": {
                    "_fns": [
                        {
                            "_fn": "xpath_one",
                            "_args": [".//div[@class='ux-labels-values__values']//text()"]
                        }
                    ]
                }
            }
        }
    }
}

# Get a response.
response = requests.request(
    "POST",
    "https://realtime.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),
    json=payload
)

# Write the JSON response to a .json file.
with open("ebay_product_page.json", "w") as f:
    json.dump(response.json(), f)

# Instead of a response with job status and results url, this will return the
# JSON response with the result.
pprint(response.json())
