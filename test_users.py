import requests

BASE = "http://127.0.0.1:4000/api/users"


def show(res):
    print(res.status_code, end=" -> ")
    try:
        print(res.json())
    except ValueError:
        print("(no body)")


print("---------- Creating ----------")
created = []
for user in [
    {"name": "Matti Seppanen", "email": "matti@example.com", "password": "M@45mtg$", "phone_number": "+358401234567", "gender": "Male", "date_of_birth": "2000-01-15", "membership_status": "Active", "account_verified": True, "company": "Nordic Travel Ltd"},
    {"name": "Anna Virtanen", "email": "anna@example.com", "password": "A@78nna$", "phone_number": "+358401234568", "gender": "Female", "date_of_birth": "1995-05-20", "membership_status": "Active", "account_verified": False, "company": "Virtanen Consulting"},
    {"name": "Jari Korhonen", "email": "jari@example.com", "password": "J@12kor$", "phone_number": "+358401234569", "gender": "Male", "date_of_birth": "1988-11-02", "membership_status": "Inactive", "account_verified": True, "company": "Korhonen Oy"},
]:
    res = requests.post(BASE, json=user)
    show(res)
    body = res.json() if res.ok else {}
    created.append(body.get("_id"))

print("---------- Duplicate Email ----------")
show(requests.post(BASE, json={"name": "Dup", "email": "matti@example.com", "password": "x", "phone_number": "1", "gender": "Male", "date_of_birth": "2000-01-01", "membership_status": "Active", "account_verified": True, "company": "X"}))

print("---------- Missing Fields ----------")
show(requests.post(BASE, json={"name": "Incomplete"}))

print("---------- Results ----------")
show(requests.get(BASE))

print("---------- Search By ID ----------")
show(requests.get(f"{BASE}/{created[0]}"))
show(requests.get(f"{BASE}/{created[2]}"))

print("---------- Invalid / Not Found ID ----------")
show(requests.get(f"{BASE}/not-a-valid-objectid"))
show(requests.get(f"{BASE}/64b64b64b64b64b64b64b64b"))  # well-formed but non-existent

print("---------- Updating ----------")
show(requests.put(f"{BASE}/{created[1]}", json={"membership_status": "Inactive", "phone_number": "+358409999999"}))

print("---------- Deleting ----------")
show(requests.delete(f"{BASE}/{created[1]}"))
show(requests.delete(f"{BASE}/64b64b64b64b64b64b64b64b"))  # well-formed but non-existent

print("---------- Results ----------")
show(requests.get(BASE))
