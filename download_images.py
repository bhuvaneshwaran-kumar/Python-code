import requests
from pprint import pprint

URL = 'https://www.google.com/'# 
API_KEY = 'create and Replace your api key right here'
URL2 = f'https://api.unsplash.com/photos/?client_id={API_KEY}'


count = 3
orientation ='landscape'
apiUrl=f'https://api.unsplash.com/photos/random/?client_id={API_KEY}&count={count}&orientation={orientation}'
# comunicate to the url fetch the response

response = requests.get(apiUrl)
data = response.json()

# print(data)
images_link = list()
for i in data:
	images_link.append((i['urls']['raw']))

i = 4
name = 'image'

for link in images_link:
	image_response = requests.get(link)
	f = open(f'{name}_{i}.jpg','wb')
	f.write(image_response.content)
	print(f'image {i}  downloaded')
	i+=1

print("completed!")
# print(response.text)


