import urllib.request
import json


query_url_snackers = 'https://s3.amazonaws.com/misc-file-snack/MOCK_SNACKER_DATA.json'
d_snackers= urllib.request.urlopen(query_url_snackers)
json_data_snackers = d_snackers.read()

data_snackers = json.loads(json_data_snackers)

query_url_products = 'https://ca.desknibbles.com/products.json?limit=250s'
d_products= urllib.request.urlopen(query_url_products)
json_data_products = d_products.read()

data_products = json.loads(json_data_products)
products = data_products['products']

fave_snack_stocked = []
emails = []
total_price = 0


for snacker in data_snackers:
    for product in products:
        if snacker['fave_snack'] == product['title']:
            emails.append(snacker['email'])

            if snacker['fave_snack'] not in fave_snack_stocked:
                fave_snack_stocked.append(snacker['fave_snack'])

            for variant in product['variants']:
                total_price += float(variant['price'])
                
print(fave_snack_stocked)
print(emails)
print(total_price)
