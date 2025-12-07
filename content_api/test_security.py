import requests
import time
import random
import string

BASE_URL = "http://127.0.0.1:8000/content"

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_auth_token(username, password):
    resp = requests.post(f"{BASE_URL}/api/login/", json={
        "username": username,
        "password": password
    })
    if resp.status_code == 200:
        return resp.json().get("token")
    return None

def register_user(username, password):
    requests.post(f"{BASE_URL}/register/", json={
        "username": username,
        "password": password,
        "email": f"{username}@example.com",
        "first_name": "Test",
        "last_name": "User"
    })

def test_security():
    print("Starting Security Test...")
    print("-" * 30)

    user_a = f"user_a_{generate_random_string(5)}"
    pass_a = "password123"
    user_b = f"user_b_{generate_random_string(5)}"
    pass_b = "password123"

    # Register users
    register_user(user_a, pass_a)
    register_user(user_b, pass_b)

    token_a = get_auth_token(user_a, pass_a)
    token_b = get_auth_token(user_b, pass_b)

    if not token_a or not token_b:
        print("Failed to get tokens. Aborting.")
        return

    # 1. Test Unauthenticated Access
    print("1. Testing Unauthenticated Access...")
    resp = requests.get(f"{BASE_URL}/api/items/")
    if resp.status_code == 401: # Or 403
        print("   PASS: Unauthenticated access denied (401)")
    else:
        print(f"   FAIL: Unauthenticated access allowed ({resp.status_code})")

    # 2. Test Data Isolation
    print("\n2. Testing Data Isolation...")
    # User A creates an item
    resp = requests.post(f"{BASE_URL}/api/items/", headers={"Authorization": f"Token {token_a}"}, json={
        "title": "User A Item",
        "body": "Private content"
    })
    item_id_a = resp.json().get("id")
    print(f"   User A created item {item_id_a}")

    # User B tries to list items (should not see User A's item)
    resp = requests.get(f"{BASE_URL}/api/items/", headers={"Authorization": f"Token {token_b}"})
    items = resp.json()
    found = any(item['id'] == item_id_a for item in items)
    if not found:
        print("   PASS: User B cannot see User A's item in list")
    else:
        print("   FAIL: User B CAN see User A's item in list")

    # User B tries to access User A's item directly
    resp = requests.get(f"{BASE_URL}/api/items/{item_id_a}/", headers={"Authorization": f"Token {token_b}"})
    if resp.status_code == 404:
        print("   PASS: User B cannot access User A's item detail (404)")
    else:
        print(f"   FAIL: User B accessed User A's item detail ({resp.status_code})")

    print("-" * 30)
    print("Security Test Complete.")

if __name__ == "__main__":
    test_security()
