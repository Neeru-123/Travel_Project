import requests
import json

r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat};{lon_2},{lat_2}?overview=false""")

routes = json.loads(r.content)
route_1 = routes.get("routes")[0]

print("Enter List of Places you want to visit : ")
t = list(input().split(' '))

for i in t:
  print(i)
  


  
