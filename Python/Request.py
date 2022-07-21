import requests

#r = requests.get('https://catfact.ninja/fact')
r = requests.get('https://dog.ceo/api/breed/boxer/images')
#https://dog.ceo/api/breeds/image/random
#https://dog.ceo/api/breed/boxer/images
print(r.json())

#{'fact': 'Tabby cats are thought to get their name from Attab, 
# a district in Baghdad, now the capital of Iraq.', 
# 'length': 100}

#{'message': 'https://images.dog.ceo/breeds/poodle-toy/n02113624_6248.jpg', 'status': 'success'}