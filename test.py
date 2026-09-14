import requests

print("---------- Creating ----------")
print(requests.post("http://127.0.0.1:4000/tours", json={"name":"Paris Getaway", "info":"Hello world", "image":"paris.jpg", "price":300, "location":"Paris"}).json())
print(requests.post("http://127.0.0.1:4000/tours", json={"name":"Rome Adventure", "info":"Hello world 2", "image":"rome.jpg", "price":250, "location":"Rome"}).json())
print(requests.post("http://127.0.0.1:4000/tours", json={"name":"Berlin Weekend", "info":"Hello world 1", "image":"berlin.jpg", "price":150, "location":"Berlin"}).json())
print(requests.post("http://127.0.0.1:4000/tours", json={"name":"Madrid Escape", "info":"Hello world 5", "image":"madrid.jpg", "price":500, "location":"Madrid"}).json())
print(requests.post("http://127.0.0.1:4000/tours", json={"name":"Lisbon Trip", "info":"Hello world 0", "image":"lisbon.jpg", "price":0, "location":"Lisbon"}).json())

print("---------- Results ----------")
print(requests.get("http://127.0.0.1:4000/tours").json())

print("---------- Search By ID ----------")
print(requests.get("http://127.0.0.1:4000/tours/1").json())
print(requests.get("http://127.0.0.1:4000/tours/3").json())
print(requests.get("http://127.0.0.1:4000/tours/7").json())

print("---------- Patching ----------")
print(requests.patch("http://127.0.0.1:4000/tours/4", json={"name": "Test Trip", "info": "This is good!"}).json())
print(requests.patch("http://127.0.0.1:4000/tours/2", json={"price": 500}).json())

print("---------- Deleting ----------")
print(requests.delete("http://127.0.0.1:4000/tours/2").status_code)

print("---------- Results ----------")
print(requests.get("http://127.0.0.1:4000/tours").json())