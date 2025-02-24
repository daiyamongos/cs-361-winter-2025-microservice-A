# small test program 

import requests

URL = " http://localhost:5000/"
img_name = "example.jpg"

# # upload
# file = {"file": open(img_name, "rb")}
# response = requests.post(f"{URL}/upload", files=file)
# print(f"POST request response:\n", response.status_code, response.json())

# # retrieve
# response = requests.get(f"{URL}/images/{img_name}")
# print(f"GET request response:\n", response.status_code, response.json())
# if response.status_code == 200:
#     with open(f"downloaded_{img_name}", "wb") as file:
#         file.write(response.content)
# else:
#     print("failed to retrieve image")

# # delete image
# response = requests.delete(f"{URL}/images/{img_name}")
# print(f"DELETE request response:\n", response.status_code, response.json())