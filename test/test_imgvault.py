# small test program 

import requests
from PIL import Image

URL = " http://localhost:5000/"
img_name = "example.jpg"

# upload with POST method
file = {"file": open(img_name, "rb")}
response = requests.post(f"{URL}/upload", files=file)
print(f"POST request response:\n", response.status_code, response.json())

# # retrieve with GET method (also displays image)
# response = requests.get(f"{URL}/images/{img_name}")
# print(f"GET request response:\n", response.status_code)
# if response.status_code == 200:
#     with open(f"downloaded_{img_name}", "wb") as file:
#         file.write(response.content)

#     img = Image.open(f"downloaded_{img_name}")
#     img.show()
# else:
#     print("failed to retrieve image")

# # delete image with DELETE method
# response = requests.delete(f"{URL}/images/{img_name}")
# print(f"DELETE request response:\n", response.status_code, response.json())