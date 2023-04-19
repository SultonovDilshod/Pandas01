import requests
import json
url="https://graph.facebook.com/v16.0/112007835182080?fields=link%2Cimages&access_token=EAATfMgsOoJYBAAFbsZCwo5PcONkZBNIAihKGgRGkxf96j2ODUPPdi6Ft6DBgUxaZCIUUTdbXzA4yaLq5TGVKCJHWW75SXxLOGzSHa6ZBCnfLvmTDOTvfx40kzSFibqS93X0swBvRSQKsRU7DOPuLOFitsTVMYI3oXe5adl2tIB3JBhcgBcft3DXqYGuuOOZCyLRAnopv7tUodQL6uSjqPscAyEfrZC6wNqVfxLtgOAaXcn6BIEphP7Dmf5taqZCpxAZD"


response = requests.get(url)
data = response.text
new_data = json.loads(data)
img_url = new_data['images'][0]['source']
img_bytes = requests.get(img_url).content
with open('image.jpg', 'wb') as file:
    file.write(img_bytes)

