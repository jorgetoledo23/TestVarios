import requests

r = requests.get('https://catfact.ninja/fact')

print(r.json())

#{'fact': 
# 'Approximately 1/3 of cat owners think their pets are able to read their minds.', 
# 'length': 78}

#{'fact': 'Cats have 32 muscles that control the outer ear (humans have only 6). 
# A cat can independently rotate its ears 180 degrees.', 'length': 122}