
import requests
import json

users_url = "https://tdsbasictest.vercel.app/api/db/users"
products_url = "https://tdsbasictest.vercel.app/api/db/products"
orders_url = "https://tdsbasictest.vercel.app/api/db/orders"

users_response = requests.get(users_url)
users_response.raise_for_status()
users_data = users_response.json()

products_response = requests.get(products_url)
products_response.raise_for_status()
products_data = products_response.json()

orders_response = requests.get(orders_url)
orders_response.raise_for_status()
orders_data = orders_response.json()

print("Users:", users_data)
print("Products:", products_data)
print("Orders:", orders_data)
