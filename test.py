import requests

BASE = "http://127.0.0.1:4000/api/tours"

print("---------- Creating ----------")
created = []
for tour in [
    {"name": "Paris Getaway", "info": "Hello world", "image": "paris.jpg", "price": "300", "duration": "3 days", "rating": 4.5, "season": "Spring", "specialOffer": "None"},
    {"name": "Rome Adventure", "info": "Hello world 2", "image": "rome.jpg", "price": "250", "duration": "5 days", "rating": 4.2, "season": "Summer", "specialOffer": "10% off"},
    {"name": "Berlin Weekend", "info": "Hello world 1", "image": "berlin.jpg", "price": "150", "duration": "2 days", "rating": 3.8, "season": "Winter", "specialOffer": "None"},
    {"name": "Madrid Escape", "info": "Hello world 5", "image": "madrid.jpg", "price": "500", "duration": "7 days", "rating": 4.9, "season": "Autumn", "specialOffer": "None"},
    {"name": "Lisbon Trip", "info": "Hello world 0", "image": "lisbon.jpg", "price": "0", "duration": "1 day", "rating": 3.0, "season": "Spring", "specialOffer": "Free"},
]:
    res = requests.post(BASE, json=tour).json()
    print(res)
    created.append(res.get("_id"))

print("---------- Results ----------")
print(requests.get(BASE).json())

print("---------- Search By ID ----------")
print(requests.get(f"{BASE}/{created[0]}").json())
print(requests.get(f"{BASE}/{created[2]}").json())
print(requests.get(f"{BASE}/{created[4]}").json())

print("---------- Updating ----------")
print(requests.put(f"{BASE}/{created[3]}", json={"name": "Test Trip", "info": "This is good!"}).json())
print(requests.put(f"{BASE}/{created[1]}", json={"price": 500}).json())

print("---------- Deleting ----------")
print(requests.delete(f"{BASE}/{created[1]}").status_code)

print("---------- Results ----------")
print(requests.get(BASE).json())
