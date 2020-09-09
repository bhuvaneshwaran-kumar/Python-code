import requests
from pprint import pprint
# pip install requests

URL = 'https://www.google.com/'
API_KEY = 'UoPu98cybYaHnihiXHK5HuOocdgjLVgyqkJdgBhvd1E'
orientation ='landscape'
count = 2
URL2 = f'https://api.unsplash.com/photos/random/?orientation={orientation}&count={count}&client_id={API_KEY}'

response = requests.get(URL2)
data = response.json()
# pprint(data)
image_links = list()

for image in data:
    image_links.append(image['urls']['full'])
    

print(image_links)
i =1 
for image in image_links:
    image_response = requests.get(image)
    file = open(f'image{i}.jpg','wb')
    file.write(image_response.content)
    file.close()
    i+=1


