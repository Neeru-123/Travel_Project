print("Enter List of Places you want to visit : ")
t = list(input().split(' '))

for i in t:
  print(i)


import requests, json
 
api_key = 'Your_API_key'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
query = input('Search query: ')
  
r = requests.get(url + 'query=' + query +
                        '&key=' + api_key)
  
x = r.json()
y = x['results']

for i in range(len(y)):
    print(y[i]['name'])
    
for x in range(len(y)):
    print(y[x]['location']
